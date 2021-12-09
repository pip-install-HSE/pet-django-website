from django.contrib import admin

# Register your models here.

from .models import *


@admin.register(FilterQuestion)
class FilterQuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(FilterQuestionUnit)
class FilterQuestionUnitAdmin(admin.ModelAdmin):
    pass


@admin.register(PersonalQuestion)
class PersonalQuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(PersonalQuestionUnit)
class FilterQuestionUnitAdmin(admin.ModelAdmin):
    pass


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass

