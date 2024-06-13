from .base import BaseModel, models

class Author(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'User'
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    