from django.contrib import admin

from .models import Poll, Question, Choice

admin.site.site_header = "System Administration"
admin.site.site_title = "System Administration"
admin.site.index_title = "Welcome to System Administration"
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),]
    inlines = [ChoiceInline]

admin.site.register(Poll)
admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question) 
# admin.site.register(Choice)