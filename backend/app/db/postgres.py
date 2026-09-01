from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from typing import AsyncGenerator

class DatabaseManager:
    def __init__(self, url: str):
        self.engine = create_async_engine(url, echo=False)
        self.session_factory = async_sessionmaker(
            self.engine, 
            expire_on_commit=False, 
            class_=AsyncSession
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """Dependency provider for database sessions."""
        async with self.session_factory() as session:
            try:
                yield session
            finally:
                await session.close()

    async def close(self):
        """Close the engine connection pool."""
        await self.engine.dispose()
