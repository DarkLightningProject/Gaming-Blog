from django.contrib import admin
from .models import PostModel,Comment 

class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created', 'approved', 'gaming_image')
    list_filter = ('approved', 'date_created')
    search_fields = ('title', 'content')



admin.site.register(PostModel, PostModelAdmin)
admin.site.register(Comment)

