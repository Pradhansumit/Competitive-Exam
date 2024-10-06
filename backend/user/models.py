import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, user_name, email, mobile, password=None, **extra_fields):
        if not user_name and not email and not mobile:
            raise ValueError("Email and mobile is required.")

        email = self.normalize_email(email)
        user = self.model(
            user_name=user_name,
            mobile=mobile,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_name, email, mobile, password=None, **extra_fields):
        user = self.create_user(
            user_name=user_name,
            email=email,
            mobile=mobile,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


def user_directory_path(instance, filename):
    """
    Storing of the user profile picture
    in the media root folder.
    """
    return f"user_{0}/{1}".format(instance.user.user_name, filename)


class CustomUser(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_name = models.CharField(max_length=50, null=False, blank=False, unique=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=12)
    registered = models.DateField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True, upload_to=user_directory_path)
    email = models.EmailField()

    USERNAME_FIELD: str = "user_name"
    REQUIRED_FIELDS: list[str] = [
        "email",
        "mobile",
    ]

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin
