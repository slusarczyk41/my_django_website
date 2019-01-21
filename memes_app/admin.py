from django.contrib import admin

# Register your models here.
from .models import Meme, Tag


admin.site.register(Meme)
admin.site.register(Tag)
