from django.db import models

# Create your models here.
class Work(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    work = models.CharField(max_length=100, blank=True, null=True)
    birthday_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'work'