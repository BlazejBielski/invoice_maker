from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManagaer(BaseUserManager["CustomUser"]):

    """Custom manager for CustomUser"""

    use_in_migrations = True

    def create_user(self, email, password, username="", **kwargs):
        """Create a user with the given email and password.

        :param str email: Email address of the user
        :param str password: <PASSWORD>
        :param str username: Username
        :return users.models.CustomUser: User object
        :raises ValueError: If email not set
        """

        if not email:
            raise ValueError("Email address is required")

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **kwargs)
        user.is_active = False
        user.password = make_password(password)
        user.save()


class CustomUser(AbstractUser):
    """
    CustomUser place holder
    """
    pass
