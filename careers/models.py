from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    employment_type = models.CharField(
        max_length=50,
        choices=[
            ("Full Time", "Full Time"),
            ("Internship", "Internship"),
        ],
    )
    description = models.TextField()
    requirements = models.TextField()
    posted_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title