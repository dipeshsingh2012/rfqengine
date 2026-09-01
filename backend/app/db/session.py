from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

class DatabaseManager:
    """
    Manages the lifecycle of the SQLAlchemy async engine and session factory.
    """
    def __init__(self, database_url: str):
        self.database_url = database_url
        self.engine = create_async_engine(
            self.database_url,
            echo=False,
            pool_pre_ping=True,
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
            class_=AsyncSession,
        )

    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        """
        Dependency provider that yields an async session.
        Ensures the session is closed after the request/context is finished.
        """
        async with self.session_factory() as session:
            try:
                yield session
            finally:
                await session.close()

    async def close(self) -> None:
        """Closes the engine connection pool."""
        await self.engine.dispose()
