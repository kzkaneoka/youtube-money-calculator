from flask import Blueprint, jsonify
# from app.youtube_money_calculator.services import ChannelService
# from app.youtube_money_calculator.services import PlayListService
# from app.youtube_money_calculator.services import VideoService

channels = Blueprint("channels", __name__)


# @channels.route("<channel_id>", methods=["GET", "POST"])
# def channels_by_id(channel_id):
#     channel = ChannelService.get(channel_id)
#     data = {}
#     channel_data\
#         = {attr: getattr(channel, attr)
#            for attr in vars(channel) if attr != "_sa_instance_state"}
#     data["channel"] = channel_data
#     video_datas = {}
#     video_ids = PlayListService.search(channel.uploads)
#     for video_id in video_ids:
#         video = VideoService.get(video_id)
#         video_datas[video.video_id]\
#             = {attr: getattr(video, attr)
#                for attr in vars(video) if attr != "_sa_instance_state"}
#     data["videos"] = video_datas
#     return jsonify(data)

@channels.route("<channel_id>", methods=["GET", "POST"])
def channels_by_id(channel_id):
    d = {
        "channel": {
            "channel_id": "UCmJz2DV1a3yfgrR7GqRtUUA",
            "icon_url_default":
                "https://yt3.ggpht.com/a/AGF-l7_wIIwHUqeI6tns85nf1B-X1nPfDgndnP_Lkw=s88-c-k-c0xffffffff-no-rj-mo",
            "icon_url_high":
                "https://yt3.ggpht.com/a/AGF-l7_wIIwHUqeI6tns85nf1B-X1nPfDgndnP_Lkw=s800-c-k-c0xffffffff-no-rj-mo",
            "icon_url_medium":
                "https://yt3.ggpht.com/a/AGF-l7_wIIwHUqeI6tns85nf1B-X1nPfDgndnP_Lkw=s240-c-k-c0xffffffff-no-rj-mo",
            "money": 2167.206,
            "subscriber_count": 29900,
            "title": "Back To Back SWE",
            "uploads": "UUmJz2DV1a3yfgrR7GqRtUUA",
            "video_count": 93,
            "view_count": 1083603
        },
        "videos": {
            "otDBXXEhrk8": {
                "channel_id": "UCmJz2DV1a3yfgrR7GqRtUUA",
                "duration": "PT15M43S",
                "icon_url_default":
                    "https://i.ytimg.com/vi/otDBXXEhrk8/default.jpg",
                "icon_url_high":
                    "https://i.ytimg.com/vi/otDBXXEhrk8/hqdefault.jpg",
                "icon_url_medium":
                    "https://i.ytimg.com/vi/otDBXXEhrk8/mqdefault.jpg",
                "money": 12.476,
                "title":
                    "8 Things Interning At Twitter Taught Me (Software Engineering)",
                "video_id": "otDBXXEhrk8",
                "view_count": 6238
            }
        }
    }
    return jsonify(d)
