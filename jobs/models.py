from django.db import models


class Job(models.Model):
    employer = models.ForeignKey('users.User')
    # resumes = FILES
    description = models.TextField()
    apply_instructions = models.TextField()
