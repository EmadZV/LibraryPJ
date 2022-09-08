from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, AbstractUser
from django.urls import reverse
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField
# from django.contrib.auth.models import User
from django.conf import settings

from mycontent.models import Book

User = settings.AUTH_USER_MODEL


class Category(models.Model):
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('mycontent',
                       args=[self.slug])

    def __str__(self):
        return self.title


class MyUser(AbstractUser):
    GENDER = (
        ('male', 'Male'),
        ('female', 'Female')
    )
    STATUS = (
        ('normal', 'Normal'),
        ('premium', 'Premium'),
        ('author', 'Author'),
        ('admin', 'Admin')
    )
    REQUIRED_FIELDS = ['email', ]
    USERNAME_FIELD = 'username'

    # uid = models.UUIDField(
    #     default=None,
    #     blank=True,
    #     null=True,
    #     unique=True,
    # )

    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=50, unique=True, default=None, blank=True, null=True, )
    email = models.EmailField(null=True, )
    password = models.CharField(max_length=20, null=True, )
    age = models.PositiveIntegerField(null=True, )
    gender = models.CharField(choices=GENDER, max_length=6, null=True, )
    phone_number = PhoneNumberField(default='0')
    last_seen = models.DateTimeField(default=None, null=True)
    profile_image = models.ImageField(upload_to='forum/images', default=None)

    is_staff = models.BooleanField(null=True)
    is_admin = models.BooleanField(null=True)
    is_premium = models.BooleanField(null=True)

    def set_password(self, raw_password):
        AbstractUser.set_password(self, raw_password=raw_password)

    def premium(self):
        self.is_premium = True
        self.save()

    def admin(self):
        self.is_admin = True
        self.save()

    def staff(self):
        self.is_staff = True
        self.save()

    objects = UserManager()

    def get_current_user(self):
        return self

    def __str__(self):
        return self.username

    # class Meta:
    #     permissions = (
    #         ("is_premium", "Premium User"))


class Author(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ManyToManyField(Category, )

    def __str__(self):
        return self.name


class Translator(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=True)
    description = models.TextField()
    category = models.ManyToManyField(Category, )

    def save(self, *args, **kwargs):
        self.is_staff = True
        return super().save(*args, **kwargs)

    user.is_staff = True

    def __str__(self):
        return self.user.username

# class PremiumUser(models.Model):
#     user = models.OneToOneField(MyUser, on_delete=models.CASCADE, null=True)
