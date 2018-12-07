from services.VideoService import VideoService
from models.Video import Video

class SalesmanUi:

    def __init__(self):
        self.__video_service = VideoService()

    def main_menu(self):

        action = ""
        while(action != "q"):
            print("You can do the following: ")
            print("1. Add a video")
            print("2. List all videos")
            print("press q to quit")

            action = input("Choose an option: ").lower()

            if action == "1":
                title = input("Movie title: ")
                genre = input("Genre: ")
                length = input("Length in minutes: ")
                new_video = Video(title, genre, length)
                self.__video_service.add_video(new_video)

            elif action == "2":
                videos = self.__video_service.get_videos()
                print(videos)
                    