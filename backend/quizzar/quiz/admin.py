from django.contrib import admin
from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

from .models import Question, Quiz, Choice


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 0
    fields = ["get_edit_link", "title", "description"]
    readonly_fields = ["get_edit_link"]

    def get_edit_link(self, obj=None):
        if obj.pk:
            url=reverse('admin:{}_{}_change'.format(obj._meta.app_label, obj._meta.model_name), args=[force_text(obj.pk)])
            return mark_safe("""<a href="{url}">{text}</a>""".format(
                url=url,
                text="Edit this {} separately".format(obj._meta.verbose_name),
            ))
        return "(save and continue editing to create a link)"

    get_edit_link.short_description = "Edit link"
    get_edit_link.allow_tags = True


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 0


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    save_on_top = True
    inlines = [QuestionInline]