from django.contrib import admin
from . import models


# Register your models here.
class ChoiceInline(admin.StackedInline):
    """ 创建问题关联选项 """
    model = models.Choice
    # 关联个数
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 4
    inlines = [ChoiceInline]
    search_fields = ['name']


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'num', 'ques']
    list_filter = ['num']
    list_per_page = 4
    search_fields = ['name', 'num']


admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Choice, ChoiceAdmin)
admin.site.register(models.Host)
admin.site.register(models.Account)
admin.site.register(models.PhoneNumber)
admin.site.register(models.Application)