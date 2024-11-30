from django.db import models

class UniversityClasses(models.Model):
    Title = models.CharField(max_length=50)
    Course_Number = models.IntegerField()
    Instructor_Name = models.CharField(max_length=50)
    Duration = models.FloatField()

    # add model manager
    objects = models.Manager()

    # Define model metadata
    class Meta:
        # fixes plural form
        verbose_name_plural = "UniversityClasses"

    def __str__(self):
        return self.Title
