from django.contrib import admin
from .models import Books

# Register your models here.

@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id', 'book_name', 'book_price', 'book_time')
    list_display_links = ('book_name',)
    list_per_page = 20
    list_filter = ('book_name', 'book_price')
    search_fields = ('book_name',)