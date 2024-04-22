from sqlalchemy import PrimaryKeyConstraint, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.models import CustomBase
from src.track.models import Track


class User(CustomBase):

    __tablename__ = "user_table"

    name: Mapped[str] = mapped_column(String(), unique=True, nullable=False)
    track: Mapped[list["Track"]] = relationship(back_populates="user")

    __table_args__ = (
        PrimaryKeyConstraint("id", name="user_id")
    )
