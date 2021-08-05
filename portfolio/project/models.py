from django.db import models

# Create your models here.


class ProjectInfo(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    github = models.URLField()
    demo = models.URLField(blank=True)
    image = models.ImageField(blank=True)
    show = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Project Info'
        verbose_name_plural = 'Projects Info'

    def __str__(self):
        return self.name
