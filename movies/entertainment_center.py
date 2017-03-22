import media
import fresh_tomatoes

# Create and populate movie objects containing my favorite movies
matrix = media.Movie("The Matrix",
                     "Computer hackers learn the truth of the world in which their bodies reside",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "Humans destroying an alien planet for profit",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

# Create array containing movie objects for open_movies_page method
movies = [matrix, toy_story, avatar]

# use fresh_tomatoes.open_movies_page method which creates html and css
# for each movie object creating fresh_tomatoes.html
fresh_tomatoes.open_movies_page(movies)