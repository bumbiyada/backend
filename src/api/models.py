from django.db import models
from django.utils import timezone

# Create your models here.


class ListAll(models.Model):
    Foiv = models.CharField(
        verbose_name='ФОИВ',
        max_length=64,
        default='',
        blank=True
    )
    Document_type = models.CharField(
        verbose_name='Тип документа',
        max_length=64,
        default='',
        blank=True
    )
    Document_number = models.CharField(
        verbose_name='Номер документа',
        max_length=64,
        default='',
        blank=True
    )
    Document_init_data = models.DateTimeField(
        verbose_name='Дата создания документа',
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True
    )
    Stage_name = models.CharField(
        max_length=64,
        verbose_name='Этап',
        blank=True
    )
    Stage_data = models.DateTimeField(
        verbose_name='Дата проведения этапа',
        auto_now=False,
        auto_now_add=False,
        null=True,
        blank=True

    )
    Stage_user = models.CharField(
        verbose_name='Исполнитель',
        blank=True,
        default='',
        max_length=64
    )
    Is_aborted = models.BooleanField(
        verbose_name='Прервана',
        default=False
    )
    Is_done = models.BooleanField(
        verbose_name='Выполнена',
        default=True
    )
    Marked_on_delete = models.BooleanField(
        verbose_name='Пометка на удаление',
        default=False
    )

    class Meta:
        db_table = 'documents'

    # def __str__(self):
    #     name = str(self.Document_number) + ' ' + str(self.Stage_name) + ' ' + str(self.Stage_data)
    #     return name
