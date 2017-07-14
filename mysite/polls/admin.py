from django.contrib import admin

from .models import Choice, Question

#makes Choice objects editable on the Question admin page.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date'] #adds a filter sidebar

admin.site.register(Question, QuestionAdmin)
#tells the admin that Question objects have an admin interface
