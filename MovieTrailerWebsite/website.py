import media
import fresh_tomatoes

# this list contains the movie data
movielist = [media.Movie("The Godfather",
			"The aging patriarch of an organized crime dynasty transfers"
			" control of his clandestine empire to his reluctant son.",
			"https://images-na.ssl-images-amazon.com/images/M/"
			"MV5BZTRmNjQ1ZDYtNDgzMy00OGE0LWE4N2YtNTkzNWQ5ZDhlNGJmL2ltYWdlL"
			"2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,704,1000_"
			"AL_.jpg",
			"https://www.youtube.com/watch?v=sY1S34973zA"
			),
			media.Movie("The Shawshank Redemption",
			"Two imprisoned men bond over a number of years, finding "
			"solace and eventual redemption through acts of common decency.",
			"https://images-na.ssl-images-amazon.com/images/M/"
			"MV5BODU4MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._V1_SY1000_CR0,"
			"0,672,1000_AL_.jpg",
			"https://www.youtube.com/watch?v=6hB3S9bIaco"
			),
			media.Movie("Inception",
			"A thief, who steals corporate secrets through use of "
			"dream-sharing technology, is given the inverse task of"
			" planting an idea into the mind of a CEO.",
			"https://images-na.ssl-images-amazon.com/images/M/"
			"MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@."
			"_V1_SY1000_CR0,0,675,1000_AL_.jpg",
			"https://www.youtube.com/watch?v=YoHD9XEInc0"
			),
			media.Movie("The Dark Knight",
			"When the menace known as the Joker wreaks havoc and chaos "
			"on the people of Gotham, the caped crusader must come to "
			"terms with one of the greatest psychological tests of his "
			"ability to fight injustice.",
			"https://images-na.ssl-images-amazon.com/images/M/"
			"MV5BMTMxNTMwODM0NF5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_SY1000_CR0,"
			"0,675,1000_AL_.jpg",
			"https://www.youtube.com/watch?v=EXeTwQWrcwY"
			),
			media.Movie("The Lord of the Rings: The Return of the King",
			"Gandalf and Aragorn lead the World of Men against Sauron's"
			" army to draw his gaze from Frodo and Sam as they approach"
			" Mount Doom with the One Ring.",
			"https://images-na.ssl-images-amazon.com/images/M/"
			"MV5BYWY1ZWQ5YjMtMDE0MS00NWIzLWE1M2YtODYzYTk2OTNlYWZmXkEy"
			"XkFqcGdeQXVyNDUyOTg3Njg@._V1_SY1000_SX668_AL_.jpg",
			"https://www.youtube.com/watch?v=r5X-hFf6Bwo"
			),
			media.Movie("Se7en",
			"Two detectives, a rookie and a veteran, hunt a serial "
			"killer who uses the seven deadly sins as his modus operandi.",
			"https://images-na.ssl-images-amazon.com/images/M/"
			"MV5BOTUwODM5MTctZjczMi00OTk4LTg3NWUtNmVhMTAzNTNjYjcyXkEyXkFq"
			"cGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,639,1000_AL_.jpg",
			"https://www.youtube.com/watch?v=znmZoVkCjpI"
			),
			media.Movie("Schindler's List",
			"In German-occupied Poland during World War II, Oskar Schindler"
			" gradually becomes concerned for his Jewish workforce after "
			"witnessing their persecution by the Nazi Germans.",
			"https://images-na.ssl-images-amazon.com/images/M/"
			"MV5BNDE4OTMxMTctNmRhYy00NWE2LTg3YzItYTk3M2UwOTU5Njg4XkEy"
			"XkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
			"https://www.youtube.com/watch?v=JdRGC-w9syA"
			),
			media.Movie("Forrest Gump",
			"Forrest Gump, while not intelligent, has accidentally been "
			"present at many historic moments, but his true love, Jenny "
			"Curran, eludes him.",
			"https://images-na.ssl-images-amazon.com/images/M/"
			"MV5BYThjM2MwZGMtMzg3Ny00NGRkLWE4M2EtYTBiNWMzOTY0YTI4XkEyXkF"
			"qcGdeQXVyNDYyMDk5MTU@._V1_SY1000_CR0,0,757,1000_AL_.jpg",
			"https://www.youtube.com/watch?v=uPIEn0M8su0"
			),
			media.Movie("Gladiator",
			"When a Roman general is betrayed and his family murdered"
			" by an emperor's corrupt son, he comes to Rome as a gladiator"
			" to seek revenge.",
			"https://images-na.ssl-images-amazon.com/images/M/"
			"MV5BMTgwMzQzNTQ1Ml5BMl5BanBnXkFtZTgwMDY2NTYxMTE@._V1_SY1000_CR0"
			",0,675,1000_AL_.jpg",
			"https://www.youtube.com/watch?v=owK1qxDselE"
			)
		]

# This functions calls the html generator function
fresh_tomatoes.open_movies_page(movielist)
