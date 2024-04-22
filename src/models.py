from sqlalchemy import (
    DateTime, Float, ForeignKey,
    PrimaryKeyConstraint, String
)


from sqlalchemy.orm import (
    DeclarativeBase, Mapped, declared_attr, mapped_column,
    relationship,
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


class User(CustomBase):

    __tablename__ = "user_table"

    name: Mapped[str] = mapped_column(String(), unique=True, nullable=False)
    track: Mapped[list["Track"]] = relationship(back_populates="user")

    __table_args__ = (
        PrimaryKeyConstraint("id", name="user_id"),
    )


class Track(CustomBase):

    __tablename__ = "track_table"

    name: Mapped[str] = mapped_column(String(), nullable=False)
    description: Mapped[str] = mapped_column(String(), nullable=True)
    start_point: Mapped[str] = mapped_column(String(), nullable=False)
    finish_point: Mapped[str] = mapped_column(String(), nullable=False)
    start_datetime: Mapped[str] = mapped_column(DateTime(), nullable=False)
    finish_datetime: Mapped[str] = mapped_column(DateTime(), nullable=True)
    travel_duration: Mapped[str] = mapped_column(Float(), nullable=True)

    user: Mapped["User"] = relationship(back_populates="track")
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))

    __table_args__ = (
        PrimaryKeyConstraint("id", name="track_id"),
    )
