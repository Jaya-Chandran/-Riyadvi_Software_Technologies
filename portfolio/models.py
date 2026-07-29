from django.db import models
from django.urls import reverse

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    client = models.CharField(max_length=200)

    image = models.ImageField(upload_to='portfolio/')

    short_description = models.CharField(max_length=250)

    problem = models.TextField()

    solution = models.TextField()

    result = models.TextField()

    tools = models.CharField(max_length=250)

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})