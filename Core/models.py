from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True, null=True)
    userpic = models.ImageField(upload_to='UserProfile_Pic', null=True, blank=True, verbose_name=str(user)+str(id))
    dateofbirth = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=1, null=True)
    levelofeducation = models.CharField(max_length=100, null=True)
    contact = models.CharField(max_length=20, null=True)
    nationality = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username


class UserDonateMoMo(models.Model):
    phonenumber = models.IntegerField(null=True)
    email = models.CharField(max_length=999)
    comment = models.TextField()
    transactionId = models.IntegerField()
    statusCode = models.IntegerField
    amount = models.IntegerField()

    def __str__(self):
        return self.transactionId


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()