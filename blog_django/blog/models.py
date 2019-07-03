from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default = timezone.now) # auto_now = True როცა პოსტი განახლდება დრო იყოს მიმდინარე(ახლანდელი)
    author = models.ForeignKey(User, on_delete=models.CASCADE) # რეგისტრირებულ მომხმარებლის წაშლისას მისი პოსტები *{წაიშალოს}* თუ დარჩეს.

    def __str__(self):
        return self.title