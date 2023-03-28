from django.contrib import admin

from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        (None,               {'fields': ['answer_1']}),
        (None,               {'fields': ['answer_2']}),
        (None,               {'fields': ['answer_3']}),
        (None,               {'fields': ['answer_4']}),
        ('Correct answer',   {'fields': ['correct_answer']}),
        ('To verify',        {'fields': ['is_verified']}),
        ('Experience',       {'fields': ['experience']}),
    ]
    list_display = ['id', 'question', 'correct_answer', 'pub_date', 'is_verified', 'experience',
                    'was_published_recently']
    list_display_links = ['id', 'question', 'pub_date']
    list_filter = ['pub_date', 'is_verified']
    list_per_page = 5
    search_fields = ['question']


admin.site.register(Question, QuestionAdmin)
