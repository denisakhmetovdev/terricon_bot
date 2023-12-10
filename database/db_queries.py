import sqlite3

import aiosqlite

from src.config.default import db_path


async def create_user(user_id: int, user_name: str):
    async with aiosqlite.connect(db_path) as aio_base:
        async with aio_base.cursor() as cur:
            try:
                await cur.execute("INSERT INTO users (user_id, user_name) VALUES (?, ?)",
                                  (user_id, user_name)
                                  )
                await aio_base.commit()
            except sqlite3.IntegrityError:
                print("Такой пользователь уже зарегистрирован")


async def get_all_users():
    async with aiosqlite.connect(db_path) as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM users")
            users = await cur.fetchall()
    return users
