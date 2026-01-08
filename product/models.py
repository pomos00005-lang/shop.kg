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
class Reviews(models.Model):
    choice_blog = models.ForeignKey(Products, on_delete=models.CASCADE,related_name="review")
    MARKS = (
        ('🌟','🌟'),
        ('🌟🌟','🌟🌟'),
        ('🌟🌟🌟','🌟🌟🌟'),
        ('🌟🌟🌟🌟','🌟🌟🌟🌟'),
        ('🌟🌟🌟🌟🌟','🌟🌟🌟🌟🌟'),
    )
    marks = models.CharField(max_length=100,choices=MARKS,default='🌟🌟🌟🌟🌟')
    text = models.TextField(verbose_name='Отзыв',max_length=100)
    created_ad = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.choice_blog}-{self.marks}'
    
    class Meta():
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'