import webbrowser

class Movie():
    def __init__(self,curmoviename,curmoviestory, curposterimage,curtraileryoutube):
        self.title=curmoviename
        self.storyline=curmoviestory
        self.poster_image_url=curposterimage
        self.trailer_youtube_url=curtraileryoutube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

        
        
