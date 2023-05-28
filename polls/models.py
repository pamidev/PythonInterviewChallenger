from django.db.models import BooleanField, CharField, DateTimeField, DO_NOTHING, ForeignKey, Model


class Question(Model):
    question = CharField(max_length=255)
    answer_1 = CharField(max_length=255)
    answer_2 = CharField(max_length=255)
    answer_3 = CharField(max_length=255)
    answer_4 = CharField(max_length=255)
    correct_answer = CharField(max_length=255)
    created = DateTimeField(auto_now_add=True)
    is_verified = BooleanField(default=False)
    experience = ForeignKey('stats.Experience', on_delete=DO_NOTHING)

    def __str__(self):
        return self.question
