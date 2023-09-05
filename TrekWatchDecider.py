# This is a script that chooses what episode of Star Trek to watch.
# The simplest version just chooses a random episode of all Trek.
# More complex versions may allow for choosing favorite show, characters, subjects.

# enterprise 4 seasons
# s1: 26
# s2: 26
# s3: 24
# s4: 22
# The code is supposed to choose an episode within the range of 4 seasons and within the range of 26 (approx) episodes
# Let's start with the first season.

# season = random.randint(1, 4)
# if season == 1 or season == 2:
#     episode = random.randint(1, 26)
# elif season == 3:
#     episode = random.randint(1, 24)
# else:
#     episode = random.randint(1, 22)
# print(f"Let's watch season {season}, episode {episode}!")


import random
shows = ["The Original series",
         "The Animated Series",
         "The Next Generation",
         "Deep Space Nine",
         "Voyager",
         "Enterprise",
         "Discovery",
         "Short Treks",
         "Picard",
         "Lower Decks",
         "Prodigy",
         "Strange New Worlds"]

# def get_random_show():
#     return random.choice(shows)

show = random.choice(shows)
print(show)

# get_random_show()
# season = random.randint(1, 4)
#
# if season == 1 or season == 2:
#     max_episode = 26
# elif season == 3:
#     max_episode = 24
# else:
#     max_episode = 22
#
# episode = random.randint(1, max_episode)
# print(f"Let's watch season {season}, episode {episode}!")
