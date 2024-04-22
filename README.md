# anverali

## Overview

Тестовое задание для Anverali по ТЗ:

"Необходимо создать сайт с админ панелью и 2-мя кабинетами на Flask или Django. Сайт может быть не оформлен красиво. Структура на выбор. Можно взять за основу сайт kwork.ru. На сайте помимо админки должны быть два кабинета заказчика и исполнителя. Минимальный набор полей в профилях (имя, контактные данные, опыт). БД PostgreSQL"

Для удобства тестирования проверяющими завернул всё в Docker compose. 

## Инструкция по запуску:

## 1. Клонируйте репозиторий на локальную машину.
git clone https://github.com/FourZd/anverali.git
## 2. Перейдите в терминале внутрь папки /{репозиторий}/dev_tools/ 
cd anverali/dev_tools
## 3. Поднимите контейнеры
docker-compose up --build
## 4. Приложение готово к тестированию. Адрес на 8000 порту.
http://localhost:8000

API Endpoints Documentation
/admin/ - Админка. Необходимо создать суперюзера.
/customers/profile/<int:id>/ - Эндпоинт для просмотра профиля заказчика.
/freelancers/profile/<int:id>/ - Эндпоинт для просмотра профиля фрилансера.


## Насчет более сложных реализаций
В ТЗ нет прямого упоминания какого-либо другого функционала, 
из-за чего я не стал тратить время даже на авторизацию. Но при получении фидбека про необходимость подобного - я без проблем реализую.