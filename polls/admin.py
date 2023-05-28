from django.contrib import admin

from .models import Question


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['created']}),
        (None, {'fields': ['question']}),
        (None, {'fields': ['answer_1']}),
        (None, {'fields': ['answer_2']}),
        (None, {'fields': ['answer_3']}),
        (None, {'fields': ['answer_4']}),
        (None, {'fields': ['correct_answer']}),
        (None, {'fields': ['experience']}),
        (None, {'fields': ['is_verified']}),
    ]
    list_display = ['id', 'question', 'correct_answer', 'created', 'experience', 'is_verified']
    list_display_links = ['id', 'question', 'created', 'is_verified']
    list_filter = ['created', 'is_verified']
    list_per_page = 25
    search_fields = ['question', 'correct_answer']

# admin.site.register(Question)
