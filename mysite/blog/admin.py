from django.contrib import admin

# Register your models here.

from .models import Post, Project, Comment


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


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):  # Corrigido nome da classe
    list_display = ("name", "body", "post", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]  

    def approve_comments(self, request, queryset):
        queryset.update(active=True)