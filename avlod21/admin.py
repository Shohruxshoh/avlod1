from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Post, Contact, Courses, Team, Galereya
# Register your models here.


@admin.register(Courses)
class CoursesAdmin(TranslationAdmin):
    list_display = ('name',)


@admin.register(Post)
class BlogAdmin(TranslationAdmin):
    list_display = ('title', )


@admin.register(Team)
class TeamAdmin(TranslationAdmin):
    list_display = ('name',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Galereya)
class GalereyaAdmin(admin.ModelAdmin):
    list_display = ('created', )