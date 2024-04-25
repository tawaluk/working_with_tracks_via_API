from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import CustomBase, Track
from config import settings

track_engine = create_engine(
    url=settings.database_url_async_psycopg,
    echo=True,
)

session = sessionmaker(
    autoflush=False,
    bind=track_engine,
)

def get_user_tracks(api_token: str):

    connect_db = session()
    tracks = connect_db.query(Track).filter(Track.api_token == api_token).all()

    return tracks


def create_track(track):
    connect_db = session()
    connect_db.add(track)
    connect_db.commit()
    connect_db.refresh(track)
    return track


def delete_all():
    CustomBase.metadata.drop_all(bind=track_engine)

def create_all():
    CustomBase.metadata.create_all(bind=track_engine)

test_case = Track(
        api_token="5b3ce3597851110001cf62488de5fbe05d8d40adb594a97fe7716bb8",
        name="Test Track2",
        description="This is a test track",
        start_point="Start Point",
        finish_point="Finish Point",
        start_datetime=datetime.now(),
        finish_datetime=datetime.now(),
        travel_duration=2.5
    )
