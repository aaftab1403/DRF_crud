from django.db import models

class Task(models.Model):

    class StatusChoices(models.TextChoices):
        DONE = 'done',
        IN_PROGRESS = 'inprogress',
        PENDING = 'pending',
        BLOCKER = 'blocker',

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    status = models.CharField(
        max_length=20, 
        choices=StatusChoices.choices, 
        default=StatusChoices.PENDING
    )
