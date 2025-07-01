Данный проект представляет собой веб-приложение, реализованное на основе фреймворка FastAPI , которое позволяет:
  Парсить товары с сайта Wildberries по заданному пользователем запросу
  Отображать результаты парсинга на веб-странице
  Сохранять спарсенные данные в базу данных PostgreSQL через ORM SQLAlchemy 

Для запуска приложения необходимо:
  ```
  git clone https://github.com/ <ваш_аккаунт>/test_project_of_weather.git
  ```

  ```
  cd test_project_of_weather
  ```
  Установить зависимости:
  ```
    pip install -r requirements.txt
  ```


  Далее небходимо установить docker
  ```
  sudo apt update && sudo apt install docker.io docker-compose
  ```

  После этого нужно зайти в папку с докер файлом и создать контейнеры.
  ```
    docker-compose up -d
  ```

Далее можно перейти по сслыке http://localhost:8000/
