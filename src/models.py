from sqlalchemy import (
    DateTime, Float,
    PrimaryKeyConstraint, String
)

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


class Track(CustomBase):

    __tablename__ = "track_table"

    api_token: Mapped[str] = mapped_column(String(), unique=False)
    name: Mapped[str] = mapped_column(String(), nullable=False)
    description: Mapped[str] = mapped_column(String(), nullable=True)
    start_point: Mapped[str] = mapped_column(String(), nullable=False)
    finish_point: Mapped[str] = mapped_column(String(), nullable=False)
    start_datetime: Mapped[str] = mapped_column(DateTime(), nullable=False)
    finish_datetime: Mapped[str] = mapped_column(DateTime(), nullable=True)
    travel_time: Mapped[str] = mapped_column(String(), nullable=False)
    travel_duration: Mapped[str] = mapped_column(Float(), nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint("id", name="track_id"),
    )

    def __str__(self):
        return (
            f"Track name: {self.name}, "
            f"description: {self.description}, "
            f"start_point: {self.start_point}, "
            f"finish_point name: {self.finish_point}, "
            f"finish_point: {self.finish_point}, "
            f"start_datetime: {self.start_datetime}, "
            f"finish_datetime: {self.finish_datetime}, "
            f"travel_time: {self.travel_time}, "
            f"travel_duration: {self.travel_duration}"
        )
