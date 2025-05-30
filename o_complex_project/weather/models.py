from django.db import models

# Create your models here.
class Town(models.Model):
    title = models.CharField(max_length=64)
    weather = models.CharField(max_length=1024)
    scan_time = models.DateTimeField()
    fact = models.CharField(max_length=1024, null=True)
    cnt = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
    
    def __str__(self):
        return self.title