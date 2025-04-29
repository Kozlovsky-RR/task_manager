from fastapi import FastAPI

# from contextlib import asynccontextmanager
from app.database import create_tables, delete_tables
from app.router.tasks_router import router as tasks_router
from app.router.user_router import router as user_router
from app.auth.jwt_auth import router as jwt_router


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await delete_tables()
#     print("база очищена")
#     await create_tables()
#     print("база готова к работе")
#     yield
#     print("Выключение")


app = FastAPI()

app.include_router(tasks_router)
app.include_router(user_router)
app.include_router(jwt_router)
