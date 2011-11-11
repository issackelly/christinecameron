from django.db import models
from model_utils.models import TimeStampedModel

class Rsvp(TimeStampedModel):
    invitation_name = models.CharField(max_length=128, verbose_name="Name on invitation")
    dinner_dancing = models.BooleanField("Will you be joining us on February 4th?")
    email = models.EmailField()
    comments = models.TextField(blank=True, null=True, verbose_name="Comments and names of guests attending")
