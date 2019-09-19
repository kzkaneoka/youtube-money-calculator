from app import db
from flask import current_app, g
from app.youtube_money_calculator.models import Channel, Video
from googleapiclient.discovery import build


class ChannelService:
    def fetch(channel_id):
        try:
            youtube = get_youtube_service()
            response = youtube\
                .channels()\
                .list(part="snippet,contentDetails,statistics",
                      id=channel_id)\
                .execute()
            snippet = response["items"][0]["snippet"]
            contentDetails = response["items"][0]["contentDetails"]
            statistics = response["items"][0]["statistics"]
        except Exception as e:  # TODO
            print(e)
        fetched_data = {
            "channel_id": channel_id,
            "title": snippet["title"],
            "subscriber_count": statistics["subscriberCount"],
            "view_count": statistics["viewCount"],
            "video_count": statistics["videoCount"],
            "icon_url_default": snippet["thumbnails"]["default"]["url"],
            "icon_url_medium": snippet["thumbnails"]["medium"]["url"],
            "icon_url_high": snippet["thumbnails"]["high"]["url"],
            "uploads": contentDetails["relatedPlaylists"]["uploads"],
            "money": float(statistics["viewCount"]) * 0.002  # TODO
        }
        return fetched_data

    def get(channel_id):
        channel = Channel.query.get(channel_id)
        if not channel:
            fetched_data = ChannelService.fetch(channel_id)
            channel = Channel(**fetched_data)
            db.session.add(channel)
            db.session.commit()
        return channel


class PlayListService:
    def search(playlist_id):
        next_page_token = None
        video_ids = set()
        while True:
            youtube = get_youtube_service()
            try:
                response = youtube\
                    .playlistItems()\
                    .list(
                          part='contentDetails',
                          playlistId=playlist_id,
                          pageToken=next_page_token)\
                    .execute()
                for item in response['items']:
                    video_ids.add(item['contentDetails']['videoId'])
            except Exception as e:  # TODO
                print(e)
            if 'nextPageToken' in response:
                next_page_token = response['nextPageToken']
            else:
                break
        return video_ids


class VideoService:
    def fetch(video_id):
        try:
            youtube = get_youtube_service()
            response = youtube\
                .videos()\
                .list(part="snippet,contentDetails,statistics",
                      id=video_id)\
                .execute()
            snippet = response["items"][0]["snippet"]
            contentDetails = response["items"][0]["contentDetails"]
            statistics = response["items"][0]["statistics"]
        except Exception as e:  # TODO
            print(e)
        fetched_data = {
            "video_id": video_id,
            "title": snippet["title"],
            "view_count": statistics["viewCount"],
            "duration": contentDetails["duration"],
            "channel_id": snippet["channelId"],
            "icon_url_default": snippet["thumbnails"]["default"]["url"],
            "icon_url_medium": snippet["thumbnails"]["medium"]["url"],
            "icon_url_high": snippet["thumbnails"]["high"]["url"],
            "money": float(statistics["viewCount"]) * 0.002  # TODO
        }
        return fetched_data

    def get(video_id):
        video = Video.query.get(video_id)
        if not video:
            fetched_data = VideoService.fetch(video_id)
            video = Video(**fetched_data)
            db.session.add(video)
            db.session.commit()
        return video


def get_youtube_service():
    if "youtube" not in g:
        g.youtube = build(
                          current_app.config["YOUTUBE_API_SERVICE_NAME"],
                          current_app.config["YOUTUBE_API_VERSION"],
                          developerKey=current_app.config["DEVELOPER_KEY"])
    return g.youtube
