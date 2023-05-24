# Скрипт для получения данных с Yandex Metric и TopVisor

Скрипт проходится по заданным доменам и получает данные с топвизора по ТОПам, и данные с метрики по посещениям с поисковых страниц
## Шаги использования

Клонируем репозиторий
```
git clone https://github.com/useless-apple/topvisor_metric_info
```
Переходим в рабочий каталог
```
cd topvisor_metric_info
```
Устанавливаем виртуальное окружение
```
python3 -m venv venv
```
Активируем его
```
source venv/bin/activate
```
Устанавливаем зависимости
```
pip install -r requirements.txt
```
Для работы бота, ему необходимо добавить .env

- **USER_ID_TOPVISOR** - id сайта в топвизоре
- **TOKEN_TOPVISOR** - Токен пользователя ТопВизора (важно что бы сайт был доступен по данному токену)
- **TOKEN_METRIC** - Токен аккаунта в Yandex Metric


Добавляем файл .env в корень проекта


## Запуск v.1

Заполняем в корне файл domain.xlsx и запускаем скрипт
```shell
python main.py
```

## Запуск v.2

Заполняем ``dist/domain.xlsx`` и запускаем скрипт через EXE файл
```shell
/dist/main.exe
```
