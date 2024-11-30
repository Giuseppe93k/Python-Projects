from django.db import models

# Create your models here.
class UniversityCampus(models.Model):
    CampusName = models.CharField(max_length=50)
    State = models.CharField(max_length=2)
    CampusID = models.IntegerField()

    # adding model manager
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "University Campus"

    def __str__(self):
        return self.CampusName