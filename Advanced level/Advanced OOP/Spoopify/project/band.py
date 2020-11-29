# from typing import List

from project.album import Album


class Band:
    name: str
    albums = []
        # List[Album]

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album.name in map(lambda a: a.name, self.albums):
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        albums = [a for a in self.albums if a.name == album_name]

        if not albums:
            return f"Album {album_name} is not found."

        if albums[0].published:
            return f"Album has been published. It cannot be removed."

        self.albums.remove(albums[0])
        return f"Album {album_name} has been removed."

    def details(self):
        return '\n'.join([f'Band {self.name}'] + [a.details() for a in self.albums]) + '\n'
