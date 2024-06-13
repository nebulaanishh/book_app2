from .base import BaseModel, models
from books.helpers.auth_utils import hash_raw_password

class Author(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'User'

    def save(self, *args, **kwargs):
        if not self.pk or not Author.objects.filter(pk=self.pk).exists():
            self.password = hash_raw_password(self.password)
        super().save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    