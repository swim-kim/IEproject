from django.db import models


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    writer = models.CharField(max_length=100)
    body = models.TextField()
    image = models.ImageField(upload_to = "blog/", blank=True, null=True)

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:20]

class Photo(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    