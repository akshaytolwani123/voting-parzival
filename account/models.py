from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User , on_delete = models.CASCADE)
    has_voted_for_captain = models.BooleanField(default=False)
    has_voted_for_vice_captain = models.BooleanField(default=False)
    voted_for_captain = models.TextField(max_length= 50, blank = True)
    voted_for_vice_captain = models.TextField(max_length= 50, blank = True)


@receiver(post_save, sender = User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

@receiver(post_save, sender = User)
def save_user_profile(sender,instance, **kwargs):
    instance.profile.save()
    