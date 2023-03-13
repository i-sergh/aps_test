# aps_test

Тестовое задание для apsolutions.ru

# Руководство по установке и запуску

1. Клонируем репозиторий в рабочую папку и переходим в папку проекта
```bash
git clone  https://github.com/i-sergh/aps_test.git
```
2. Собираем докер-контейнеры 
```bash
sudo docker-compose up -d --build
```
3. Проводим миграции базы данных через alembic
* Генерируем ревизию 
```bash
sudo docker-compose exec fastapi bash -c "cd .. && alembic revision --autogenerate " 
```
* Обновляем до последней ревизии
```bash
sudo docker-compose exec  fastapi bash -c "cd .. && alembic upgrade head"
```
4. Заполняем базу postgres исходными данными
```bash
sudo docker-compose exec  fastapi bash -c "cd ../utils && python converter_postgres.py"
```
5. Теперь заполняем базу elastic исходными данными
```bash
sudo docker-compose exec  fastapi bash -c "cd ../utils && python converter_elastic.py"
```




