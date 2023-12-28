from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Dps(models.Model):
    divorced = models.BooleanField(default=False)
    date_checked = models.DateTimeField(default=timezone.now) #uses the system timezone settings
    current_user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        user = self.current_user
        divorce_status = self.divorced
        if divorce_status == True:
           status = 'Divorced'
        else:
           status = "Not Divorced"
        return f'Username: {str(user).upper()} || Divorce Status: {str(status).upper()}'
    
