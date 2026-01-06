from django.db import models


class Products(models.Model):
    name_product = models.CharField(max_length=40,verbose_name='Продукт')
    image = models.ImageField(upload_to='products/',verbose_name='фото продукта')
    description = models.TextField(verbose_name='описание продукта')
    TYPE_PRODUCT = (
        ('Для детей','Для детей'),
        ('Для взрослых','Для взрослых'),
        ('Для всех','Для всех')
    )
    count = models.IntegerField(default=1,verbose_name='Колчиество:')
    price = models.IntegerField(default=100,verbose_name='Цена:')

    Who_is_the_product_for = models.CharField(max_length=20,choices=TYPE_PRODUCT,default='Для всех',verbose_name='Котегория продукта:')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name_product
    class Meta():
        verbose_name = 'Список продуктов'
        verbose_name_plural = 'Список продутов'