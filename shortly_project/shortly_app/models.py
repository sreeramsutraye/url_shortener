from django.db import models
import string
import random

def generate_random_short_url():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

class ShortURL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=6, unique=True, default=generate_random_short_url)
