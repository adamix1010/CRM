from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Lead(models.Model):
    BEFORE_CONTACT = 'Before first contact'
    DURING_PROCESS = 'During process'
    AFTER_PROCESS = 'After process'
    SERVICE = 'Service'
    REJECTED = 'Rejected'
    STATUS = [
        (BEFORE_CONTACT, 'Before first contact'),
        (DURING_PROCESS, 'During process'),
        (AFTER_PROCESS, 'After process'),
        (SERVICE, 'Service'),
        (REJECTED, 'Rejected'),
    ]

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    cell_num = models.IntegerField()
    e_mail = models.CharField(max_length=50)
    status = models.CharField(max_length=32, choices=STATUS, default='before first contact')
    addons = models.FileField(blank=True, null=True)
    agent = models.ForeignKey(Agent, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.e_mail


def post_user_created_signal(sender, instance, created, **kwargs):
    print(instance, created)
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)
