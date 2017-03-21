import webbrowser

# this class is the class depicting movie


class Movie():
    def __init__(self, curMovieName, curMovieStory, curPosterImage,
				curTrailer):
        self.title=curMovieName
        self.storyline=curMovieStory
        self.poster_image_url=curPosterImage
        self.trailer_youtube_url=curTrailer

def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)
