from django.db import models


class Directory(models.Model):

    """Модель справочника"""

    name = models.CharField(max_length=100, verbose_name='Наименование')
    short_name = models.CharField(max_length=50, verbose_name='Короткое наименование')
    description = models.CharField(max_length=500, verbose_name='Описание')
    version = models.CharField(max_length=50, null=False, verbose_name='Версия')
    date = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Дата начала действия')

    def __str__(self):
        return "{} Версия:{}".format(self.name, self.version)

    class Meta:
        verbose_name = 'Справочник'
        verbose_name_plural = 'Справочники'


class DirectoryElement(models.Model):

    """Модель элемента справочника"""

    directory_id = models.ForeignKey(Directory, verbose_name='ID справочника', on_delete=models.CASCADE)
    element_code = models.CharField(max_length=25, null=False, verbose_name='Код элемента')
    element_value = models.CharField(max_length=100, null=False, verbose_name='Значение элемента')

    def __str__(self):
        return self.element_code

    class Meta:
        verbose_name = 'Элемент справочника'
        verbose_name_plural = 'Элементы справочника'
