from datetime import datetime

from sqlalchemy import Float, create_engine, func
from sqlalchemy.orm import sessionmaker

from models import CustomBase, Track
from config import settings
from constants import TEST_API_TOKEN

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


def get_statistics(api_token: str, day_of_week: int):

    connect_db = session()
    statistics = connect_db.query(
        func.extract('dow', Track.start_datetime).label('day_of_week'),
        func.sum(func.cast(Track.travel_time, Float)).label('total_distance'),
        func.sum(
            func.cast(Track.travel_duration, Float)
        ).label('total_travel_time'),
        func.avg(
            func.cast(Track.travel_duration, Float) /
            func.cast(Track.travel_time, Float)
        ).label('average_speed')
    ).filter(
        Track.api_token == api_token,
        func.extract('dow', Track.start_datetime) == day_of_week
    ).group_by('day_of_week').all()

    result: list = []
    for stat in statistics:
        result.append({
            'day_of_week': int(stat.day_of_week),
            'total_distance': round(float(stat.total_distance), 3),
            'total_travel_time': round(float(stat.total_travel_time), 3),
            'average_speed': round(float(stat.average_speed), 3)
        })

    return result


# for dev and tests

def delete_all():

    CustomBase.metadata.drop_all(bind=track_engine)


def create_all():

    CustomBase.metadata.create_all(bind=track_engine)


test_case = Track(
        api_token=TEST_API_TOKEN,
        name="Test Track2",
        description="This is a test track",
        start_point="Start Point",
        finish_point="Finish Point",
        start_datetime=datetime.now(),
        finish_datetime=datetime.now(),
        travel_duration=2.5
    )
