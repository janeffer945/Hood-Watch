from django.contrib import admin
from .models import Post, Business, NeighborHood

# Register your models here.

admin.site.register(NeighborHood)
admin.site.register(Business)
admin.site.register(Post)
