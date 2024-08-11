from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TaskList(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    # owner = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    # owner_id = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    # another = models.CharField(max_length=10, default='Stuff')

    def __str__(self):
        return f'{self.task} - {self.done}'
