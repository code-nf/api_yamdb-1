from django.contrib import admin
from reviews.models import User
from reviews.models import Categories, Genres, Titles

@admin.register(User)
class UsersAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
        'role',
        'bio',
        'first_name',
        'last_name',
    )
    search_fields = ('username', 'role',)
    list_filter = ('username',)
    empty_value_display = '-пусто-'


admin.site.register(Categories)
admin.site.register(Genres)
admin.site.register(Titles)
