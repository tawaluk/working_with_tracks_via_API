from sqlalchemy import (
    DateTime, Float, ForeignKey,
    PrimaryKeyConstraint, String
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import CustomBase
from src.users.models import User


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
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    __table_args__ = (
        PrimaryKeyConstraint("id", name="track_id")
    )
