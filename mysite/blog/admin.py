from django.contrib import admin

# Register your models here.

from .models import Post, Project

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'created_on')
    list_filter = ('author', 'status')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name_repo', 'ower', 'status')
    list_filter = ('owner', 'status')
    search_fields = ['title', 'description', 'owner']
    
admin.site.register(Project)