from django.contrib import admin
from .models import Actor, Movie, Review


class ActorAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Actor, ActorAdmin)


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Movie, MovieAdmin)



class ReviewAdmin(admin.ModelAdmin):
    list_display = ('content',)

admin.site.register(Review, ReviewAdmin)