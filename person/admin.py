from django.contrib import admin
from .models import Question
from .models import Person
from .models import Choice
from .models import Category
admin.site.register(Question)
admin.site.register(Person)
admin.site.register(Choice)
admin.site.register(Category)
# Register your models here.
