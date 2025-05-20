from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class URL(Base):
    __tablename__ = "urls"

    id: Mapped[int] = mapped_column(primary_key=True)
    original_url: Mapped[str]
    short_url: Mapped[str]
    created_at: Mapped[str]
    updated_at: Mapped[str]
    is_active: Mapped[bool] = mapped_column(default=True)
    times_accessed: Mapped[int] = mapped_column(default=0)
