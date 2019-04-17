from django.contrib import admin
from .models import Book, Hero


class HeroInline(admin.StackedInline):
    model = Hero
    # 关联个数
    extra = 2


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'hero_name', 'content', 'pub_date']
    search_fields = ['name']
    inlines = [HeroInline, ]
    list_per_page = 1


class HeroAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'book_id']
    list_filter = ['gender']


# Register your models here.
admin.site.register(Book, BookAdmin)
admin.site.register(Hero, HeroAdmin)
