from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager["CustomUser"]):

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

        return user

    def create_superuser(self, email, username, password=None, **kwargs):
        """"Create a superuser with the given email and password.Superuser have admin permissions, and his active.

        :param str email: email address of the superuser
        :param str username: email adress as username
        :param str password: <PASSWORD>
        :return users.models.CustomUser: Superuser object
        """

        user = self.model(email=email, username=username, password=password)

        user.is_active = True
        user.is_superuser = True
        user.is_staff = True
        user.is_admin = True
        user.save()
        return user


class CustomUser(AbstractUser):
    """Overrides default Django user model with custom user model.
    Custom user uses email field as the USERNAME_FIELD for authentication.
    It is still possible use the username but it is not necessary.

    Inherits from AbstractUser.
        * username
        * first_name
        * last_name
        * email
        * is_active
        * is_staff
        * is_superuser
        * date_joined
        * last_login
        * password
        * groups

    :param str email: user email
    :param str optional username: username
    :param str password: user password
    """

    id: models.UUIDField = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True, db_index=True)
    email = models.EmailField(_("email adress"), unique=True)
    username = models.CharField(max_length=100, validators=[UnicodeUsernameValidator()])

    USERNAME_FIELD: str = "email"
    REQUAIRED_FIELDS: list[str] = [
        "email adress",
    ]

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email
