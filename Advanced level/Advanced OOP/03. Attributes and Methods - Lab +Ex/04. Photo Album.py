class PhotoAlbum:

    pages: int
    photos: list

    def __init__(self, pages: int):
        self.pages = pages

        self.photos = [[] for _ in range(pages)]

        self.free_page_row = 0
        self.free_slot_col = 0

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(int(photos_count / 4))

    def add_photo(self, label: str):

        if self.free_slot_col <= 4:
            if (self.free_slot_col == 4 and self.free_page_row == self.pages - 1) or self.pages == 0:
                return "No more free spots"

            if self.free_slot_col == 4:
                self.free_page_row += 1
                self.free_slot_col = 0

            self.photos[self.free_page_row].append(label)
            self.free_slot_col += 1
            return f"{label} photo added successfully on page {self.free_page_row + 1} slot {self.free_slot_col}"

    def display(self):
        result = ''

        for r in range(len(self.photos)):
            result += "-" * 11 + "\n"
            result += ("[] " * len(self.photos[r]))
            result = result.strip()
            if len(self.photos[r]) == 0:
                result += "\n"
            result += "\n"
        if self.pages != 0:
            result += ("-" * 11) + "\n"

        return result




# album = PhotoAlbum(9)
album = PhotoAlbum.from_photos_count(18)
print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.add_photo("wedding"))
print(album.photos)
print(album.add_photo("wedding"))
print(album.display())
