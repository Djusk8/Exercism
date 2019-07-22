import random
from string import ascii_uppercase as upper

s_random = random.SystemRandom()


class Robot(object):
    def __init__(self):
        self.name = s_random.choice(upper) + s_random.choice(upper) + str(s_random.randint(100, 999))

    def reset(self):
        self.__init__()
