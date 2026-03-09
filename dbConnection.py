# 
print("dbConnection.py loaded")
from dotenv import load_dotenv
load_dotenv()

import os
import asyncpg

pool = None


async def init_db():
    global pool

    try:
        print("Trying to create DB pool...")

        print("DB_HOST:", os.getenv("DB_HOST"))
        print("DB_NAME:", os.getenv("DB_NAME"))
        print("DB_USER:", os.getenv("DB_USER"))
        print("DB_PORT:", os.getenv("DB_PORT"))

        pool = await asyncpg.create_pool(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT", "5432"),
            ssl="require",
            min_size=1,
            max_size=10
        )

        print("Database pool created successfully")

    except Exception as e:
        print("DATABASE CONNECTION ERROR:", e)


async def get_connection():
    global pool

    if pool is None:
        await init_db()

    return pool