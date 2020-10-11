from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=40,null=False)
    album_name = models.CharField(max_length=30,null=False)
    genre = models.CharField(max_length=40)
    created_date = models.DateField()

    def __str__(self):
        return self.album_name


class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    song_name = models.CharField(max_length=40)
    created_date = models.DateField()

    def __str__(self):
       return self.song_name