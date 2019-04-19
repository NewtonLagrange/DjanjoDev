from django.contrib import admin
from .models import Choice, Question


# Register your models here.
class ChoiceInline(admin.StackedInline):
    """ 创建问题关联选项 """
    model = Choice
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


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
