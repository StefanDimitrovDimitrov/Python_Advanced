from project.song import Song


class Album:

    name: str



    def __init__(self, name, *args):
        self.name = name
        self.songs = args

        self.published = False

    def song(self, song: Song):
        pass

    def remove_song(self, song_name: str):
        pass

    def publish(self):
        pass

    def details(self):
        pass

