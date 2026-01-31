from django.contrib import admin

# Register your models here.

from .models import Post, Project


# Gerenciamento de Posts
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created_on")
    list_filter = ("author", "created_on", "status")
    search_fields = ["title", "content"]
    prepopulated_fields = {'slug': ("title",)}
    
admin.site.register(Post)

# Gerenciamento de Projetos
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name_repo", "description" "owner", "status")
    list_display = ("owner", "status")
    search_fields = ["name_repo", "description", "owner", "status", "content"]
    
admin.site.register(Project)