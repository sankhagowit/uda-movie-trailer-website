import webbrowser

# Movie class holds the title, short storyline description, url string of
# title picture and url string of the movie trailer. Also includes a
# show_trailer method which opens the movie trailer in a web browser
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title =  movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)