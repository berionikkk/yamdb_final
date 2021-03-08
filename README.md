![YaMDb workflow](https://github.com/berionikkk/yamdb_final/workflows/yamdb_workflow/badge.svg)

# Докеризация проекта YaMDb
Деплой API проекта YaMDb на базе Django REST Framework с базой данных PostgreSQL. YaMDb представляет собой интеренет-сервис отзывов о произведениях (например, фильмы, книги и т.д.).

## Документация

Полная документация API представлена (http://84.201.129.36/redoc/)

## Установка
Проверьте установлен ли у вас Docker и docker-compose на сервере

`docker -v`

Если Docker не установлен, то на Linux воспользуйтесь скриптом:

`sudo apt-get update`

`sudo apt-get install docker-ce docker-ce-cli containerd.io`

Если же у вас другая ОС, то воспользуйтесь официальной инструкцией.

Далее также проверяем наличие docker-compose:

`docker-compose -v`

Если у вас не установлен docker-compose и вы пользователь системы Linux, то вы можете установить его из официального репозитория:

 `sudo curl -L "https://github.com/docker/compose/releases/download/1.28.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose`

1.28.2 последняя на текущий момент версия.

 `sudo chmod +x /usr/local/bin/docker-compose`

Изменение доступа.


## Подготовка репозитория на GitHub

Для использования Continuous Integration и Continuous Deployment необходимо в репозитории на GitHub прописать Secrets - переменные доступа к вашим сервисам.
Переменые прописаны в workflows/yamdb_workflow.yaml

* DOCKER_PASSWORD, DOCKER_USERNAME - для загрузки и скачивания образа с DockerHub 
* USER, HOST, PASSPHRASE, SSH_KEY - для подключения к удаленному серверу 
* TELEGRAM_TO, TELEGRAM_TOKEN - для отправки сообщений в Telegram


## Развертывание приложения

 При пуше в ветку main при помощи CI/CD приложение пройдет тесты, обновит образ на DockerHub и сделает деплой на сервер. Дальше необходимо подлкючиться к серверу.
```
ssh <USER>@<HOST>
```
 Выведите список запущенных контейнеров при помощи команды:
```
docker ps
```
 Перейдите в запущенный контейнер приложения berionikkk/yamdb_final командой:
```
docker container exec -it <CONTAINER ID> bash
```
 Внутри контейнера необходимо выполнить миграции и собрать статику приложения:
```
python manage.py collectstatic --no-input
python manage.py migrate
```

## Стек технологий

[Python (v.3.8.5)](https://www.python.org/)

[Django (v.3.0.8)](https://www.djangoproject.com/)

[Django REST Framework (v.3.11.0)](https://www.django-rest-framework.org/)

[Django REST Framework Simple JWT (v.4.3.0)](https://django-rest-framework-simplejwt.readthedocs.io)

[PostgreSQL (v.12.4)](https://www.postgresql.org/)

[Gunicorn (v. 20.0.4)](https://gunicorn.org/)

[Docker (v.20.10.3)](https://www.docker.com/)

[Docker-compose (v.1.27.1)](https://docs.docker.com/compose/)

[Nginx](https://nginx.org/ru/)


## Об авторе

[Махмутов Артур](https://github.com/berionikkk/) - студент курса "Python-разработчик" Яндекс.Практикума.

