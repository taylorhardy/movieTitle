import media
import fresh_tomatoes

#create movie variables and pass movie info to contructor

toy_story = media.Movie("Toy Story",
						"A story about a boy and his toys that come to life",
						"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
					 "A marine on an alien planet",
					 "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
					 "https://www.youtube.com/watch?v=d1_JBMrrYw8")

school_of_rock = media.Movie("School of Rock",
					 "Band member teaches students rock music",
					 "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
					 "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
ratatouille = media.Movie("Ratatouille",
					 "Rat becomes cheif",
					 "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
					 "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
					 "Midnight in Paris",
					 "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
					 "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
					 "girl has to compete in deadly games",
					 "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
					 "https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

fresh_tomatoes.open_movies_page(movies)