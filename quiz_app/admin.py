from django.contrib import admin
from .models import Quiz, Question

# Register your models here.

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('status', 'created_at')
