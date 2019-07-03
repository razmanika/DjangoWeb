import datetime
from django.db import models
from django.utils import timezone
from django.shortcuts import reverse

class User(models.Model):
    email = models.EmailField(max_length =70, blank = True)
    pswd = models.CharField(max_length=70, blank=True)

    def __str__(self):
        return self.email

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    publish_time = models.DateTimeField('Date Published')
    content = models.TextField(default=timezone.now)

    # def get_absolute_url(self):
    #     return reverse('blog:detail', kwargs={'pk':self.pk}) # აქ მოდის HTML_ში არსებული pk და აბრუნებს შესაბამის პოსტს
        # და ამ პოსტს აგზავნის detail ის url _ზე

    def __str__(self):
        return self.title


class Comment(models.Model):
    comm_author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_time = models.DateTimeField('Date Published')
    content = models.TextField(default=timezone.now)
    on_post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.comm_author)