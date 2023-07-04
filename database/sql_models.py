from typing import Optional

from sqlmodel import Field, SQLModel

from sqlalchemy.ext.asyncio import create_async_engine

from sqlalchemy.orm import declarative_base

import asyncio

from datetime import datetime

Base = declarative_base()

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: str
    completed: Optional[bool] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

async def main():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)



if __name__ == "__main__":
    engine = create_async_engine("sqlite+aiosqlite:///database_async.db")
    asyncio.run(main())