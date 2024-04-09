# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.utils import timezone
from django.db import models
from django.contrib.postgres.fields import ArrayField


class AlembicVersion(models.Model):
    version_num = models.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'alembic_version'


class Carts(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'carts'


class Order(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)  # This assumes User model is exists
    address = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    products = models.TextField()
    status = models.BooleanField(default=False)
    create_date = models.DateTimeField(default=timezone.now)

    class Meta:
        managed = False
        db_table = 'orders'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ от {self.user} по адресу {self.address} на сумму {self.price} рублей'


class Cartsitems(models.Model):
    cart = models.ForeignKey(Carts, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'cartsitems'


class Categories(models.Model):
    name = models.CharField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField()
    description = models.CharField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    photo_url = models.CharField()
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)
    subcategory = models.ForeignKey('Subcategories', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name}, {self.category.name}, {self.subcategory.name}'


class Subcategories(models.Model):
    name = models.CharField(unique=True, blank=True, null=True)
    category = models.ForeignKey(Categories, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subcategories'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return f'{self.name}'


class Question(models.Model):
    question_text = models.CharField(max_length=255)
    answer = models.TextField()

    class Meta:
        managed = False
        db_table = 'question'
        verbose_name_plural = 'Вопросы'

    def __str__(self):
        return f'{self.question_text}'


class Users(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(blank=True, null=True)
    phone = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'@{self.username},{self.user_id}'
