from django.db import models

# Create your models here.
MAX_LENGTH = 255

# class Category(models.Model):
#     name = models.CharField(max_length=MAX_LENGHT, verbose_name='Название')
#     description = models.TextField(null=True, blank=True, verbose_name='Описание')

#     def __str__(self):
#         return self.name
    
#     class Meta: 
#         verbose_name = 'Категория'
#         verbose_name_plural = 'Категории'

# class Collection(models.Model):
#     name = models.CharField(max_length=MAX_LENGHT, verbose_name='Название')
#     description = models.TextField(null=True, blank=True, verbose_name='Описание') 
#     # collect = models.OneToOneField('Collection', on_delete=models.PROTECT, verbose_name='Коллекция', related_name='Коллекция')

#     def __str__(self):
#         return self.name

#     class Meta: 
#         verbose_name = 'Коллекция'
#         verbose_name_plural = 'Коллекции'

# class Cloth(models.Model):
#     name = models.CharField(max_length=MAX_LENGHT, verbose_name='Название')
#     description = models.TextField(null=True, blank=True, verbose_name='Описание')
#     price = models.FloatField(verbose_name='Цена')
#     color = models.CharField(max_length=MAX_LENGHT, verbose_name='Цвет')
#     min_size = models.PositiveBigIntegerField(default=36, verbose_name='Минимальный размер')
#     max_size = models.PositiveBigIntegerField(default=56, verbose_name='Максимальный размер')
#     photo = models.ImageField(upload_to='image%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
#     create_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления на сайт')
#     is_exists = models.BooleanField(default=True, verbose_name='В наличии?')

#     collection = models.ManyToManyField(Collection, verbose_name='Коллекция')
#     category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория')

#     def __str__(self):
#         return f'{self.name} - {self.price} руб.'
    
#     class Meta: 
#         verbose_name = 'Одежда'
#         verbose_name_plural = 'Одежды'


class Bicycle(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название')
    price = models.FloatField(verbose_name='Цена')
    brend = models.CharField(max_length=MAX_LENGTH, verbose_name='Бренд')
    is_exists = models.BooleanField(default=True, verbose_name='В наличии?')

    def __str__(self):
        return f'{self.name} - {self.brend} - {self.price} - {self.is_exists}'
    class Meta: 
        verbose_name = 'Велосипед'
        verbose_name_plural = 'Велосипеды'

class PhotoBicycle(models.Model):
    bicycle = models.ForeignKey(Bicycle, on_delete=models.PROTECT, verbose_name='Велосипед')
    photo = models.ImageField(upload_to='image%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return f'Фото для {self.bicycle.name}'
    
    class Meta:
        verbose_name = 'Фото велосипеда'
        verbose_name_plural = 'Фотографии велосипедов'

class Clients(models.Model):
    clint_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя клиента')
    email = models.CharField(max_length=MAX_LENGTH, verbose_name='Потча')
    phone = models.CharField(max_length=12, verbose_name='Телефон')

    def __str__(self):
        return f'{self.clint_name} - {self.email}'
    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Orders(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.PROTECT, verbose_name='Клиент')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата оформления')
    status = models.BooleanField(default=True, verbose_name='Статус')

    def __str__(self):
        return f'{self.status}'
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class OrderDetail(models.Model):
    client = models.ForeignKey(Clients, on_delete=models.PROTECT, verbose_name='Клиент')
    order = models.ForeignKey(Orders, on_delete=models.PROTECT, verbose_name='Заказ')
    count = models.IntegerField(verbose_name='Кол-во')
    price_for_count =  models.FloatField(verbose_name='Цена за штуку')

    def __str__(self):
        return f'{self.order} - {self.count} - {self.price_for_count}'
    
    class Meta:
        verbose_name = 'Подробности заказа'
        verbose_name_plural = 'Подробности заказа'

class Employee(models.Model):
    employee_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя работника')
    status = models.CharField(max_length=MAX_LENGTH, verbose_name='Должность')
    employee_phone = models.CharField(max_length=12, verbose_name='Телефон')

    def __str__(self):
        return f'{self.employee_name} - {self.status}'
    
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

class Review(models.Model):
    bicycle = models.ForeignKey(Bicycle, on_delete=models.PROTECT, verbose_name='Велосипед')
    client = models.ForeignKey(Clients, on_delete=models.PROTECT, verbose_name='Клиент')
    rating = models.IntegerField(verbose_name='Рейтинг')
    comment = models.CharField(max_length=MAX_LENGTH, verbose_name='Комментарий')

    def __str__(self):
        return f'{self.bicycle} - {self.rating} - {self.comment}'
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class Galery(models.Model):
    name = models.TextField(max_length=MAX_LENGTH, verbose_name='Название')
    comment = models.CharField(max_length=MAX_LENGTH, verbose_name='Описание')
    photo = models.ImageField(upload_to='image%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return f'{self.name} - {self.comment}'
    
    class Meta:
        verbose_name = 'Галерея'
        verbose_name_plural = 'Галереии'