from django.contrib import admin

from .models import Post, Tag

# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ['id', '__str__','updated_at', 'created_at', ]
	search_fields = ['id', 'title', 'author']

	class Meta:
		model = Post

admin.site.register(Post, PostAdmin)

admin.site.register(Tag)