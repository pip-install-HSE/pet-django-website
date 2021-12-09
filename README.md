# pet-django-website

source env/bin/activate
python3 manage.py runserver 0.0.0.0:<port>
пример: python3 manage.py runserver 0.0.0.0:8080

Если при заходе на сайт по IP пишет, что Disallowed host, нужно в PetQuiz/settings.py в лист allowed_hosts  добавить ваш ip/домен в виде строки и перезагрузить сервер
