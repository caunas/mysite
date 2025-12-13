from django.db import models
from django.contrib.auth.models import User

# se parece com um enum
STATUS = [
    (0, 'draft'),
    (1, 'published')
]

class Post(models.Model):
    # atributos
    title = models.CharField(max_length=250, unique = True)
    slug = models.SlugField(max_length = 250, unique = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'blog_posts')
    updated = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices = STATUS, default = 0)
    
    # classe aux
    class Meta:
        ordering = ['created_on']

    # metodos
    def __str__(self):
        return self.title
    