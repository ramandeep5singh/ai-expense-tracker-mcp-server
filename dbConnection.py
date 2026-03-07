import os
import asyncpg

pool = None


async def init_db():
    global pool

    try:
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
        print("Database pool creation error:", e)


async def get_connection():
    return pool