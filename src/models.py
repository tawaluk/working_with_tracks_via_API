from sqlalchemy.orm import (
    DeclarativeBase, Mapped, declared_attr, mapped_column
)


class CustomBase(DeclarativeBase):

    __abstract__ = True

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        """Generate table name based on lowercase class name.

        Returns:
            str: The table name for the class.
        """
        return f"{cls.__name__.lower()}"
