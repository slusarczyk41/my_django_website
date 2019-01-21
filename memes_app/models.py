from django.db import models
from django.utils import timezone
import datetime
# Create your models here.


class Meme (models.Model):
    def __str__(self):
        return self.name

    pic           = models.ImageField(upload_to='media/memes/%Y/%m/%d',
                                      max_length=155)

    creation_date = models.DateTimeField(verbose_name='date of creation',
                                         auto_now_add=True,
                                         editable=False,
                                         null=False,
                                         blank=False)

    name          = models.CharField(verbose_name='Name of the meme',
                                     max_length=50)

    views         = models.IntegerField(verbose_name='Number of views',
                                        default=0)

    rating        = models.FloatField(verbose_name='rating of a meme, from 0 to 1',
                                      default=0.5)

    language      = models.CharField(verbose_name='language of a meme',
                                     choices=[('pl', 'Polski'), ('en', 'English')],
                                     max_length=10,
                                     null=False,
                                     blank=False)

    tags          = models.ManyToManyField(verbose_name='tags relation',
                                           to='memes_app.Tag')

    def get_tags(self):
        return self.tags.split(',')

    def was_published_recently(self):
        now = timezone.now()
        return self.pub_date >= now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Tag (models.Model):
    def __str__(self):
        return self.name

    name         = models.CharField(verbose_name='name of a tag',
                                    max_length=50,
                                    null=False,
                                    blank=False)



