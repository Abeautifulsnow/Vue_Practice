from django.db import models

# Create your models here.


class Books(models.Model):
    book_name = models.CharField('书名', max_length=50)
    book_price = models.DecimalField('价格', max_digits=5, decimal_places=2)
    book_time = models.DateTimeField('保存日期', auto_now_add=True)

    class Meta:
        verbose_name = '书籍信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.book_name