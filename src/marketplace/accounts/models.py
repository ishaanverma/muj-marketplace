from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# MyUser Model Manager Class
class MyUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name=None, password=None,
                        is_active=True, is_staff=False, is_admin=False,
                        is_confirm=False):
        # checks all the required fields with creating a user
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        if not first_name:
            raise ValueError("Users must have a first name")

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
        )
        user.set_password(password) # also used for change password
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.confirm = is_confirm
        user.save(using=self._db)

        return user

    # sub methods used for other kind of users
    def create_staffuser(self, email, first_name, last_name=None, password=None):
        user = self.create_user(
            email,
            first_name,
            last_name = last_name,
            password = password,
            is_staff = True,
        )
        return user

    def create_superuser(self, email, first_name, last_name=None, password=None):
        user = self.create_user(
            email,
            first_name,
            last_name = last_name,
            password = password,
            is_staff = True,
            is_admin = True,
            is_confirm = True,
        )
        return user

# MyUser defines all the fields for a user account
class MyUser(AbstractBaseUser):
    email           = models.EmailField(max_length=255, unique=True)
    first_name      = models.CharField(max_length=255, blank=True, null=True)
    last_name       = models.CharField(max_length=255, blank=True, null=True)
    active       = models.BooleanField(default=True)
    staff        = models.BooleanField(default=False)
    admin        = models.BooleanField(default=False)
    timestamp       = models.DateTimeField(auto_now_add=True)
    confirm         = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    # email and password are required by default
    REQUIRED_FIELDS = ['first_name']

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        if self.last_name:
            full_name = self.first_name + ' ' + self.last_name
            return full_name
        return self.first_name

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def get_email(self):
        return self.email

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_confirm(self):
        return self.confirm
