import media
import fresh_tomatoes

toystory=media.Movie("ToyStory", "A Dumb Story", "http://www.disney.co.uk/sites/default/files/toy-story/GENERIC/Character%20Section/1240x620-toystory-characters-bullseye.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print(toystory.moviestory)
#toystory.show_trailer()
movies=[toystory];
fresh_tomatoes.open_movies_page(movies)
