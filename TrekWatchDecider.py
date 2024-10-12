# This is a script that chooses what episode of Star Trek to watch.
# The simplest version just chooses a random episode of all Trek.
# More complex versions may allow for choosing favorite show, characters, subjects.


import random
shows_info = {
    "The Original Series": {"seasons": 3, "episodes": [29, 26, 24]},
    "The Animated Series": {"seasons": 2, "episodes": [16, 6]},
    "The Next Generation": {"seasons": 7, "episodes": [26, 22, 26, 26, 26, 26, 26]},
    "Deep Space Nine": {"seasons": 7, "episodes": [20, 26, 26, 26, 26, 26, 26]},
    "Voyager": {"seasons": 7, "episodes": [16, 26, 26, 26, 26, 26, 26]},
    "Enterprise": {"seasons": 4, "episodes": [26, 26, 24, 22]},
    "Discovery": {"seasons": 5, "episodes": [15, 14, 13, 13, 10]},
    "Short Treks": {"seasons": 2, "episodes": [4, 6]},
    "Picard": {"seasons": 3, "episodes": [10] * 3},
    "Lower Decks": {"seasons": 4, "episodes": [10] * 4},
    "Prodigy": {"seasons": 2, "episodes": [20, 20]},
    "Strange New Worlds": {"seasons": 2, "episodes": [10] * 2}
}

show = random.choice(list(shows_info.keys()))
if show in shows_info:
    show_info = shows_info[show]
    season = random.randint(1, show_info["seasons"])
    max_episode = show_info["episodes"][season - 1]
    episode = random.randint(1, max_episode)
    print(f"Let's watch season {season}, episode {episode} of {show}!")