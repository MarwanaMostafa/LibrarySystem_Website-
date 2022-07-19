from django.contrib import admin
from .models import Book, Borrow
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'active']
    list_editable = ['active']
    search_fields = ['name']
    list_filter = ['category', 'price', 'publication_year']

admin.site.register(Book, BookAdmin)

admin.site.site_header = 'University Library Adminstration'
admin.site.site_title = 'University Library Adminstration'

admin.site.register(Borrow)

