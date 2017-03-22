import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

print(toy_story.storyline)

avatar = media.Movie("Avatar",
                     "Humans destroying an alien planet for profit",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

print(avatar.storyline)
avatar.show_trailer()