def play_instrument(instruments):
    return instruments.play()


class Piano:
    def play(self):
        print("playing the piano")


piano = Piano()
play_instrument(piano)
