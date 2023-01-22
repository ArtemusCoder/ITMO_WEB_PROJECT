from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ProfileRegisterForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from .models import Profile
from Blog import models as post_models


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        form_profile = ProfileRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            profile = form_profile.save(commit=False)
            profile.user = user
            user.is_active = False
            user.save()
            profile.save()
            current_site = get_current_site(request)
            mail_subject = 'Активируйте свой аккаунт'
            message = render_to_string('Users/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            messages.success(request, f'Аккаунт создан')
            context = {'title': 'Подтверждение'}
            return render(request, 'Users/confirm_start.html')
    else:
        form = UserRegisterForm()
        form_profile = ProfileRegisterForm()
    context = {
        'title': 'Регистрация',
        'form': form,
        'form_profile': form_profile
    }
    return render(request, 'Users/register.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        context = {'title': 'Спасибо'}
        return render(request, 'Users/confirm.html')
    else:
        return HttpResponse('Что-то пошло не так !!!')


@login_required
def profile(request, user, *args, **kwargs):
    profile_user = User.objects.filter(username=user)
    real_user = User.objects.filter(username=user).first()
    link = False
    id = 0
    if profile_user.exists():
        if request.user == profile_user[0]:
            context = {
                'title': 'Profile',
                'profile_user': profile_user[0],
                'id': id
            }
        else:
            user_posts = post_models.Post.objects.filter(author=profile_user[0])
            context = {
                'title': 'Profile',
                'profile_user': profile_user[0],
                'user_posts': user_posts,
                'id': id
            }
        return render(request, 'Users/profile.html', context)


@login_required
def profile_edit(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Профиль изменен')
            return redirect(f'/profile/{request.user.username}')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'title': 'Profile Edit',
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'Users/profile_edit.html', context)
