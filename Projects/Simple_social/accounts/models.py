from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User, PermissionsMixin


class User(auth.models.User, auth.models.PermissionsMixin):

    def __str__(self):
        return "@{}".format(self.username)
