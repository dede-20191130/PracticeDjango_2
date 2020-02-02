from django.contrib import admin

from blog.models import Entry, User

admin.site.register(Entry)
admin.site.register(User)
