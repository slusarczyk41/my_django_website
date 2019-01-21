from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Meme (models.Model):


    pic           = models.ImageField(upload_to='media/mems/%Y/%m/%d',
                                    height_field='pic_height',
                                    width_field='pic_width',
                                    max_length=155)

    creation_date = models.DateTimeField(verbose_name='date of creation',
                                         auto_now_add=True,
                                         editable=False,
                                         null=False,
                                         blank=False)

    def was_published_recently(self):
        now = timezone.now()
        return self.pub_date >= now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
