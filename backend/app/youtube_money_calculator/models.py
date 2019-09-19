from app import db


class Channel(db.Model):
    __tablename__ = 'channel'

    channel_id = db.Column(db.String(), primary_key=True)
    title = db.Column(db.String())
    subscriber_count = db.Column(db.Integer)
    view_count = db.Column(db.Integer)
    video_count = db.Column(db.Integer)
    icon_url_default = db.Column(db.String())
    icon_url_medium = db.Column(db.String())
    icon_url_high = db.Column(db.String())
    uploads = db.Column(db.String())
    money = db.Column(db.Float)
    videos = db.relationship('Video', backref='channel', lazy=True)

    def __init__(self, iterable=(), **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return "channel_id={}\ttitle={}".format(self.channel_id, self.title)


class Video(db.Model):
    __tablename__ = 'video'

    video_id = db.Column(db.String(), primary_key=True)
    title = db.Column(db.String())
    view_count = db.Column(db.Integer)
    duration = db.Column(db.String())
    money = db.Column(db.Float)
    icon_url_default = db.Column(db.String())
    icon_url_medium = db.Column(db.String())
    icon_url_high = db.Column(db.String())
    channel_id = db.Column(db.String(), db.ForeignKey('channel.channel_id'))

    def __init__(self, iterable=(), **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __repr__(self):
        return "video_id={}\ttitle={}".format(self.video_id, self.title)
