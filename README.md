# [Сайт доставки еды Star Burger](https://dvmn.space/)

Это сайт сети ресторанов Star Burger. Здесь можно заказать превосходные бургеры с доставкой на дом. Перейти
на [сайт](https://dvmn.space/)

![скриншот сайта](https://dvmn.org/filer/canonical/1594651635/686/)

Сеть Star Burger объединяет несколько ресторанов, действующих под единой франшизой. У всех ресторанов одинаковое меню и
одинаковые цены. Просто выберите блюдо из меню на сайте и укажите место доставки. Мы сами найдём ближайший к вам
ресторан, всё приготовим и привезём.

На сайте есть три независимых интерфейса. Первый — это публичная часть, где можно выбрать блюда из меню, и быстро
оформить заказ без регистрации и SMS.

Второй интерфейс предназначен для менеджера. Здесь происходит обработка заказов. Менеджер видит поступившие новые заказы
и первым делом созванивается с клиентом, чтобы подтвердить заказ. После оператор выбирает ближайший ресторан и передаёт
туда заказ на исполнение. Там всё приготовят и сами доставят еду клиенту.

Третий интерфейс — это админка. Преимущественно им пользуются программисты при разработке сайта. Также сюда заходит
менеджер, чтобы обновить меню ресторанов Star Burger.

## Окружение

### Добавление чувствительных данных в `.env`

Создать файл `.env` в папке `backend` и добавить следующее(есть пример заполнения в `backend/.example_env`):

Для Django:

- `SECRET_KEY` - Обязательная секретная настройка Django. Это соль для генерации хэшей. Значение может быть любым, важно
  лишь, чтобы оно никому не было
  известно. [Документация Django](https://docs.djangoproject.com/en/3.2/ref/settings/#secret-key).

- `ALLOWED_HOSTS` - Настройка Django со списком разрешённых адресов. Если запрос прилетит на другой адрес, то сайт
  ответит ошибкой 400. Можно перечислить несколько адресов через запятую,
  например `127.0.0.1, 192.168.0.1, site.test`. [Документация Django](https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts).

- `DEBUG` - Настройка Django для включения отладочного режима. Принимает значения `TRUE`
  или `FALSE`. [Документация Django](https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-DEBUG).

Для Яндекс карт:

- `YANDEX_GEOCODER_API_TOKEN` - Получите токен от [Yandex geocoder API](https://developer.tech.yandex.ru/) для карт
  JavaScript API и HTTP Геокодер.

Для БД Postgres:

- `DB_URL` - Fдрес для подключения к базе данных PostgreSQL. Другие СУБД сайт не
  поддерживает. [Формат записи](https://github.com/jacobian/dj-database-url#url-schema).

- `POSTGRES_DB` - Название бд при создании контейнера с базой данных

- `POSTGRES_USER` - Имя для бд при создании контейнера с базой данных

- `POSTGRES_PASSWORD` - Пароль для бд при создании контейнера с базой данных

Для Rollbar(не обязательные):

- `ROLLBAR_TOKEN` - Получите токен [Rollbar](https://rollbar.com/) для отслеживания ошибок в программном коде
  веб-приложений.

- `ROLLBAR_ENVIRONMENT` - Значение для отображения, где произошла ошибка(development, production и т.д.).

После заполения данных, можно прочитать файл `.env` можно увидеть примерно следующее:

```bash
$ cat .env

SECRET_KEY='your_django_key'
ALLOWED_HOSTS='127.0.0.1'
DEBUG='True'

YANDEX_GEOCODER_API_TOKEN='your_api_token'

POSTGRES_DB='project'
POSTGRES_USER='user'
POSTGRES_PASSWORD='password'
DB_URL='postgres://user:password@db/project'

ROLLBAR_TOKEN='your_token'
ROLLBAR_ENVIRONMENT='your_env'
```

## Запуск веб-приложения локально

Установить [docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)
и [docker-compose](https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-18-04).

Установить `DEBUG=TRUE` в файле `backend/.env` и собрать приложение:

```sh
$ docker-compose -f docker-compose.local.yml up
```

Сайт будет доступен по адресу: [127.0.0.1:8080](http://127.0.0.1:8080/)

## Запуск веб-приложения на хостинге

Приобрести сервер. Например, на [timeweb](https://timeweb.cloud/r/yx52009)(есть возможность получить до 2000р на баланс
аккаунта).

В файле `nginx/default.conf` изменить `server_name` на свой.

Собрать приложение:

```sh
$ docker-compose -f docker-compose.production.yml up
```

По необходимости пересобрать статику.

## Установка SSL сертификата

Перейти в `контейнер nginx`, обновить пакеты `apt`, установить пакет `certbot`, получить сертификат:

```sh
$ docker ps # Посмотреть id nginx
$ docker exec -it <id-контейнера> sh # Войти в nginx
$ apt update # Обновление пакетов apt
$ apt install certbot python3-certbot-nginx -y # Установка пакетов для certbot
$ certbot --nginx # Получение сертификата
```

## Дополнительные команды для docker-compose, docker и django

Для docker-compose и docker:

```sh
$ docker ps # Показать все контейнеры
$ docker exec -it <id-контейнера> sh # Войти в нужный контейнер
$ docker-compose -f docker-compose.yml up # Развернуть приложение
$ docker-compose -f docker-compose.yml down # Закрыть приложение
$ docker rmi $(docker images -a -q) # Удалить все images
$ docker volume rm $(docker volume ls -q) # Удалить все volumes
```

Для django. После входа в контейнер, войти в папку где находится `manage.py` :

```sh
$ python manage.py collectstatic # Собрать статику, обновит данные в volumes
$ python manage.py migrate # Сделать миграции
$ python manage.py createsuperuser # Создать суперпользователя
```

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org). За основу
был взят код проекта [FoodCart](https://github.com/Saibharath79/FoodCart).