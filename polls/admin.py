from django.contrib import admin
from polls.models import Question, Choice
# Register your models here.


class ChoiceInLine(admin.TabularInline):
    model = Choice
    readonly_fields = ('votes',)
    extra = 3

class QuestionAdmin(admin.ModelAdmin):

    inlines = [ChoiceInLine]


admin.site.register(Question,QuestionAdmin)

admin.site.register(Choice)
