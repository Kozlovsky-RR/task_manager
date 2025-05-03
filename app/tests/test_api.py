from httpx import AsyncClient
import pytest


async def test_add_user(ac: AsyncClient):
    response = await ac.post(
        "/users", params={"name": "Yan", "email": "Yan@mail.com", "password": "12345"}
    )
    data = response.json()
    print(data)
    assert response.status_code == 200


async def test_auth_user_issue_jwt(ac: AsyncClient):
    response = await ac.post(
        "/jwt/login/", data={"username": "Yan", "password": "12345"}
    )
    data = response.json()
    print(data)
    assert response.status_code == 200


# async def test_get_users(ac: AsyncClient):
#     response = await ac.get(
#         url="/users",
#         headers={
#             "access_token": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjQsInVzZXJuYW1lIjoiWWFuIiwiZW1haWwiOiJZYW5AbWFpbC5jb20iLCJleHAiOjE3NDYyNjI3NjQsImlhdCI6MTc0NjI2MTg2NH0.MGGfBw23rzGZhMOo0hyZ5Biu606P2K5zlX26r9j_CqOyeMIbJQZ7yR2Q4eUoEjQQrFe1DZYE9MrH72G5vyK5zfCtXDU5dJgAnjERmyD9JAjrPI8iM7SA2vMoTNOVxknPmQ4a0Q5tkNoZ7fLRSgG_dieeNSivZS_uR0ApdwCJsKPSEmTv4qkrPrKUuORFnS4gzMkrlwuwPKuTEPb2Sx-RNRSPnuRd_m7pPq_zuqLq84u9iFeC5T_iXTIJqzMZc-zjcqmJs4QBd79efCwyQ79tIS-t31bIbPzQnHgXGUCsVk3-GVhBTuo_XjKU0i4UUprr99Gknc3HRj7zw2aH-wXJlQ",
#             "token_type": "Bearer",
#         },
#     )
#
#     assert response.status_code == 200
