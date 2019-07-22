import random
from string import ascii_uppercase


class Robot(object):
    def __init__(self):
        self.name = random.choice(ascii_uppercase) + random.choice(ascii_uppercase) + str(random.randint(100, 999))

    def reset(self):
        self.name = " "
        self.__init__()

