from django.contrib import admin
from .models import Movie, Rating


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'rated',
                    'director', 'released_on', 'genre']
    list_filter = ['year', 'rated', 'genre']
    search_fields = ['title', 'year', 'rated',
                     'director', 'released_on', 'genre']


admin.site.register(Rating)
