from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nome = models.CharField(max_length=100)
    username = models.CharField(unique=True, max_length=150)
    
    def __str__(self):
        return self.email  # Ou qualquer outro campo que você queira usar como representação do usuário
