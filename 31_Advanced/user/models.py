# User model
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class AccountManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, username, password, **extra_fields):
        values = [username]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('_can_downvote_tip', False)
        extra_fields.setdefault('_can_remove_tip', False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('_can_downvote_tip', True)
        extra_fields.setdefault('_can_remove_tip', True)
        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length=40, unique=True)
    reputation = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_staff = models.BooleanField(default=False)

    # Set privileges in tha admin panel
    _can_downvote_tip = models.BooleanField(default=False)
    _can_remove_tip = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ["password"]

    objects = AccountManager()

    def get_reputation(self):
        return self.reputation

    def gain_reputation(self, amount):
        self.reputation += amount
        self.save()

    def lose_reputation(self, amount):
        self.reputation -= amount
        self.save()

    def can_downvote(self, tip):

        """
        An user can downvote a tip if it's the author of the tip,
        if his reputation is greater than 15, or if he has the
        permission to downvote tips.
        """

        if tip.author == self:
            return True
        elif self.reputation >= 15:
            return True
        elif self._can_downvote_tip:
            return True
        return False

    def can_delete_tip(self, tip):

        """
        An user can delete a tip if it's the author of the tip,
        if his reputation is greater than 30, or if he has the
        permission to delete tips.
        """

        if tip.author == self:
            return True
        elif self.reputation >= 30:
            return True
        elif self._can_remove_tip:
            return True
        return False

    def __str__(self):
        return self.username
