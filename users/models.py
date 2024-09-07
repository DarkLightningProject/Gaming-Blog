from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.png', upload_to='profile', validators=[FileExtensionValidator(['png', 'jpg','jpeg'])])

    def __str__(self):
        return self.user.username
