import random
import string
from random import randint


def get_pic(width=100, height=200):
    return 'http://placekitten.com/%s/%s' % (width, height)

def get_words(length=100):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(length))

def get_random(min=0, max=100):
    return randint(min, max)
