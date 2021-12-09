# pet-django-website

```shell
source env/bin/activate
```
```shell
nohup python3 manage.py runserver 0.0.0.0:<port> &
```

> пример: **python3 manage.py runserver 0.0.0.0:8088**
> В браузере в адресной строке указать server IP:порт/catalog/f <br />
> Пример *12.34.56.67:8088/catalog/f*

> Если при заходе на сайт по IP пишет, что **DISALLOWED_HOST**, нужно в PetQuiz/settings.py в лист allowed_hosts  добавить ваш ip/домен в виде строки и перезагрузить сервер
