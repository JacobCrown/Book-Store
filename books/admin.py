from django.contrib import admin
from .models import Book, Review

class ReviewsInline(admin.TabularInline):
    model = Review

class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewsInline,
    ]
    list_display = ['title', 'author', 'price']

admin.site.register(Book, BookAdmin)