from random import SystemRandom
import string
from django.utils.text import slugify


def random_letters(ka=5):
    return ''.join(SystemRandom().choices(
        string.ascii_lowercase + string.digits,
        k=ka
    ))

def slugify_new(text, ka=5):
    return slugify(text) + '-' + random_letters(ka=ka)
