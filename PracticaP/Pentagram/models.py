from uuid import uuid1

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
# Create your models here.
from django.dispatch.dispatcher import receiver


def photos_directory(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'photos/user_{0}/{1}_{2}'.format(instance.user.username, str(uuid1()), filename)


class Photo(models.Model):
    user = models.ForeignKey(User)
    photo = models.ImageField(upload_to=photos_directory, null=True)


class Comment(models.Model):
    user_id = models.ForeignKey(User)
    photo_id = models.ForeignKey(Photo)
    text = models.TextField(null=False)

class Like(models.Model):
    photo = models.ForeignKey(Photo)
    user = models.ForeignKey(User, null=False)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
