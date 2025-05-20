# interface for the factory repository using generic repository pattern
from typing import Type, TypeVar
from sqlalchemy.ext.asyncio import AsyncSession
from server.repositories.repository import Repository

T = TypeVar("T")


class RepositoryFactory:
    """
    Factory class to create instances of repositories dynamically.

    This factory ensures that each repository instance gets the correct model
    and session while maintaining type safety.
    """

    @staticmethod
    def get_repository(model: Type[T], db_session: AsyncSession) -> Repository[T]:
        """
        Creates and returns a repository instance for a given model.

        Args:
            model (Type[T]): The SQLAlchemy model class.
            db_session (AsyncSession): The SQLAlchemy async session.

        Returns:
            PostgresRepository[T]: The repository instance for the model.
        """
        return Repository[T](model=model, session=db_session)
