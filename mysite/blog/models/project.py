from django.db import models
from django.contrib.auth.models import User # Importante poder vincular um projeto a um autor

STATUS = [
    (0, "private"),
    (1, "public"),
    (2, "beta"),
    (3, "done"),
    (4, "archived")
]

class Project(models.Model):
    
    # Campos de dados de um projeto
    name_repo = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects_list")
    description = models.CharField(max_length=250)
    content = models.TextField()
    status = models.IntegerField(choices= STATUS, default=0)
    
    class Meta:
        ordering = ["status"]
        
    def __str__(self):
        return f"{self.name_repo} by {self.owner} | {self.description}"