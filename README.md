# ITMO_WEB_PROJECT

## Запуск проекта

### Сборка локального Docker

0) Установить Docker, Docker-compose (если нужно)

1) Переходим в корневую папку и создаем новый образ и запускаем контейнеры командой:

<code>docker-compose up -d --build</code>

2) После применяем migrations

<code>docker-compose exec web python manage.py makemigrations --noinput</code> 

<code>docker-compose exec web python manage.py migrate --noinput</code>

3) После создаем superuser, чтобы иметь доступ к Django admin

<code>docker-compose exec web python manage.py createsuperuser</code>

### Использование хостинга 

[http://artemusitmo.pythonanywhere.com](http://artemusitmo.pythonanywhere.com)

## Проект
<ul>
<li>Страница регистрации (/register)</li>
 - Создание пользователей, необходимо подтвердить почтой либо поставить галочку напротив Active в панеле администратора у пользователя
<img width="1440" alt="Screenshot 2023-01-23 at 05 10 33" src="https://user-images.githubusercontent.com/33132419/213955035-6acaf581-f59b-46e0-8c49-6efe04f5a56a.png">
<li>Главная страница с постами</li>
 - Использовался Flexbox
<img width="1440" alt="Screenshot 2023-01-23 at 05 20 39" src="https://user-images.githubusercontent.com/33132419/213955828-af60a588-427d-44cf-b96a-530fdbb334b1.png">
<img width="333" alt="Screenshot 2023-01-23 at 05 20 56" src="https://user-images.githubusercontent.com/33132419/213955832-6b68a380-5459-48a8-86eb-dea52d3e16d3.png">
<li> Профиль (/profile && /profile-edit) </li>
<img width="1440" alt="Screenshot 2023-01-23 at 05 22 36" src="https://user-images.githubusercontent.com/33132419/213956062-cd7e7d72-ba8a-46a6-b0d2-2a722ed50230.png">
<img width="334" alt="Screenshot 2023-01-23 at 05 22 50" src="https://user-images.githubusercontent.com/33132419/213956070-6f6d455f-0acd-40a6-ac33-4240556522d0.png">
</ul>
