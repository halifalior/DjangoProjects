from django.contrib import admin
from books.models import Book ,Bookrank

class BookAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)

class BookrankAdmin(admin.ModelAdmin):
    pass

admin.site.register(Bookrank, BookrankAdmin)
