from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    referent = models.IntegerField(null=True)
    refnumber = models.IntegerField(default=0)
    reflink = models.CharField(null=True,max_length=100)
    refdate = models.DateField(null=True)
    paid = models.BooleanField(null=True)
    paiddate =  models.DateField(null=True)

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()


class Transaction(models.Model):
    transactionid = models.IntegerField()
    userid = models.IntegerField()
    ammount = models.IntegerField()
    paiddate =  models.DateField()