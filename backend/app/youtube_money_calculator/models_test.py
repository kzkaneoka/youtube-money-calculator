from pytest import fixture
from flask_sqlalchemy import SQLAlchemy
from app.test.fixtures import db
from app.youtube_money_calculator.models import Channel, Video


@fixture
def channel() -> Channel:
    return Channel(
                   channel_id="test channel_id",
                   title="test title",
                   subscriber_count=1,
                   view_count=1,
                   video_count=1,
                   icon_url_default="test icon_url_default",
                   icon_url_medium="test icon_url_medium",
                   icon_url_high="test icon_url_high",
                   uploads="test uploads")


@fixture
def video(channel) -> Video:
    return Video(
                 video_id="test video_id",
                 title="test title",
                 view_count=1,
                 duration="test duration",
                 money=1,
                 channel_id=channel.channel_id)


def test_Channel_create(channel: Channel):
    assert channel


def test_Channel_retrieve(channel: Channel, db: SQLAlchemy):
    db.session.add(channel)
    db.session.commit()
    obj = db.session.query(Channel).get(channel.channel_id)
    assert obj.__dict__ == channel.__dict__


def test_Video_create(video: Video):
    assert video
