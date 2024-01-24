from django.db import models

class Shop(models.Model):
    name = models.CharField('Имя продукта', max_length=50)
    info = models.TextField('Описание продукта')
    img = models.TextField('ссылка к картинке')
    price = models.IntegerField('стоимость')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Shop'
        verbose_name_plural = 'Shop'
