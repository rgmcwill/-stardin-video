import uuid
from django.db import models

class Episode_Data(models.Model):
    show_title = models.CharField(max_length=200)
    season = models.IntegerField()
    episode = models.IntegerField()

    def __str__(self):
        return str(self.show_title) + " S" + str(self.season) + "E" + str(self.episode)

class Video(models.Model):
    MOVIE = 'MV'
    EPISODE = 'EP'

    VIDEO_TYPE_CHOICES = [
        (MOVIE, 'Movie'),
        (EPISODE, 'Episode'),
    ]

    title = models.CharField(max_length=200)
    location = models.URLField(max_length=200)
    # location = models.FilePathField(max_length=200)
    type = models.CharField(
        max_length=2,
        choices=VIDEO_TYPE_CHOICES,
        default=MOVIE,
    )
    extra_data = models.ForeignKey(
        Episode_Data,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        if (self.extra_data):
            return str(self.extra_data)
        else:
            return self.title
