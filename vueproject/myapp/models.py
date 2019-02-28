from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField('书名', max_length=64)
    add_time = models.DateTimeField('添加时间', auto_now_add=True)


    class Meta:
        verbose_name = '书籍信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book_name
