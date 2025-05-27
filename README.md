# Task manager
___
## О проекте
Это мой пет проект менеджер задач. Создавался он для практики и для демонстрации навыков.
### Технологии использующиеся в проекте
 * [Python](https://www.python.org/)
 * [FastAPI](https://fastapi.tiangolo.com/)
 * [SQLAlchemy](https://www.sqlalchemy.org/)
 * [SQLite](https://www.sqlite.org/)
 * [Docker](https://www.docker.com/)
 * [Loguru](https://loguru.readthedocs.io/en/stable/)
 * [Poetry](https://python-poetry.org/)
 * [Pytest](https://docs.pytest.org/en/stable/)
 * [Alembic](https://alembic.sqlalchemy.org/en/latest/)
## Как запустить
1. Клонировать репозиторий.
    ```sh
    git clone https://github.com/Kozlovsky-RR/task_manager
    ```
2. Открыть файл .env.example, подставить значения баз данных. Сгенерировать приватный и публичный ключи (расставить знаки переноса сроки).
    ```
    DB_NAME='ENTER YOUR DATA BASE NAME '
    TEST_DB_NAME='ENTER YOUR TEST DATA BASE NAME'
    PRIVATE_KEY='ENTER YOUR PRIVATE KEY'
    PUBLIC_KEY='ENTER YOUR PUBLIC KEY'
    ```
3. Перейти в папку app/config.py, и в настройках класса Settings, заменить env_file.
    ```
    env_file=".env.example"
    ```
4. Создать докер образ приложения.
    ```sh
    docker build        
    ```
5. Запустить докер контейнер.
    ```sh
    docker compose up        
    ```
## Как пользоваться
[Перейти на документацию swagger](http://localhost:9000/docs#/)
1. Для проверки статуса работы приложения перейдите на /health, если все работает вы получите ответ.
    ```
    {"status": "ok"}
    ```
2. Чтобы войти нужно нажать на Authorize, в поле username ввести **rus@gmail.com**, в поле password ввести **12345**.
3. Если вы хотите сами зарегистрироваться перейдите на /auth/register/, зарегистрируйтесь и повторите второй пункт со своими данными.
4. После входа вы можете создать свою первую задачу перейдя на /tasks
5. Чтобы посмотреть все задачи сделайте get запрос на /tasks

## Тестирование
Для запуска тестов нужно ввести в терминале команду `pytest`