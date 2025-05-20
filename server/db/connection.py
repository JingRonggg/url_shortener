import threading
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from server.config import get_settings


class DatabaseConnectionPool:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super(DatabaseConnectionPool, cls).__new__(cls)
                    cls._instance._initialize_pool()
        return cls._instance

    def _initialize_pool(self):
        settings = get_settings()

        print("Initializing database connection pool")
        self.engine = create_engine(
            settings.DB_URL.get_secret_value(),
            pool_size=5,
            max_overflow=10,
        )
        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )

    def get_session(self):
        return self.SessionLocal()


def get_db():
    db = DatabaseConnectionPool().get_session()
    try:
        yield db
    finally:
        db.close()
