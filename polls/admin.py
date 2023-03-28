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
        ('Verified',         {'fields': ['is_verified']}),
        ('Experience',       {'fields': ['experience']}),
    ]
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']


admin.site.register(Question, QuestionAdmin)
