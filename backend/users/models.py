from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


class MainRouter:
    """
    A router to control all database operations on models in the
    application.
    """

    def db_for_read(self, model, **hints):
        """
        """
        if model._meta.app_label == 'users':
            return 'default'
        elif model._meta.app_label == 'shop':
            return 'shop_db'
        return None

    def db_for_write(self, model, **hints):
        """
        #write only to default
        """

        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        """
        """
        return True

    def allow_migrate(self, db, app_label, model_name = None, **hints):
        """
        if False will not proceed
        """
        if app_label == 'shop':
            return False
        return True

class CustomUser(AbstractUser):
    pass

User = get_user_model()
class Favorites(models.Model):
    """
    Django doesn't currently provide any support for foreign key
    or many-to-many relationships spanning multiple databases.
    If you have used a router to partition models to different databases,
    any foreign key and many-to-many relationships defined
    by those models must be internal to a single database.
    """
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='favorites')
    product_id = models.BigIntegerField('product_id_write_manually')

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['user', 'product_id'],
                name='uniq_user_product'),
        ]
