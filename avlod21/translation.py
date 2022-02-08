from modeltranslation.translator import register, TranslationOptions
from .models import Team, Courses, Post

@register(Team)
class TeamTranslationOptions(TranslationOptions):
    fields = ('name', 'stack')


@register(Post)
class GenreTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Courses)
class MovieTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'davomiyligi')