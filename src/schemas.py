from datetime import datetime

from pydantic import BaseModel

from constants import TEST_API_TOKEN, TEST_START_POINT, TEST_FINISH_POINT


class TrackResponse(BaseModel):

    id: int
    api_token: str
    name: str
    description: str
    start_point: str
    finish_point: str
    start_datetime: datetime
    finish_datetime: datetime
    travel_duration: float


class TrackRequest(BaseModel):

    api_token: str = TEST_API_TOKEN
    name: str = "default"
    description: str = "default"
    start_point: list[float] = TEST_START_POINT
    finish_point: list[float] = TEST_FINISH_POINT
    start_datetime: datetime = datetime.now()
    finish_datetime: datetime = datetime.now()
    profile: str = "driving-car"
    maximum_speed: int = 80
