from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Status(models.Model):
    name = models.CharField(max_length=40, verbose_name='Статус')

    def __str__(self):
        return f'{self.name}'


class Types(models.Model):
    type = models.CharField(max_length=50, verbose_name='Типы')

    class Meta:
        db_table = 'types'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


    def __str__(self):
        return f'{self.type}'





class List(BaseModel):

    title = models.CharField(max_length=50, blank=False, null=False, verbose_name='заголовка')

    description = models.TextField(null=False, blank=False, verbose_name='Описание')

    status = models.ForeignKey('webapp.Status', max_length=200, null=False, blank=False, related_name='lists',
                              verbose_name='Status', on_delete=models.PROTECT)

    types = models.ManyToManyField('webapp.Types',

                           related_name ='lists',

                           # on_delete = models.PROTECT,

                           null = False,
                           #
                           blank = False

                           )

    about_list = models.TextField(max_length=3000, null=True, blank=True)

    class Meta:
        db_table = 'the_lists'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f'{self.id}, {self.status},{self.created_at}'


