from django.contrib import admin
from . import models
from django.db.models import Q
from django.contrib.admin import SimpleListFilter


class TypeFilter(SimpleListFilter):
    title = 'type'  # or use _('country') for translated title
    parameter_name = 'type'

    def lookups(self, request, model_admin):
        types = set()
        for c in model_admin.model.objects.all():
            if c.type.parent == None:
                types.add(c.type)
            else:
                types.add(c.type.parent)
        return [(c.id, c.title) for c in types]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(Q(type_id=self.value()) | Q(type__parent_id=self.value()))
        return queryset


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'file')


@admin.register(models.Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    prepopulated_fields = {
        'slug': ('title',)
    }

    def formfield_for_foreignkey(self, db_field, request, obj=None, **kwargs):
        if db_field.name == "parent":
            kwargs["queryset"] = models.Type.objects.filter(parent=None)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(models.Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'level', 'type')
    prepopulated_fields = {
        'slug': ('title',)
    }
    list_filter = (TypeFilter,)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['type'].widget.can_add_related = False
        form.base_fields['type'].widget.can_delete_related = False
        form.base_fields['type'].widget.can_change_related = False

        return form

    def formfield_for_foreignkey(self, db_field, request, obj=None, **kwargs):
        if db_field.name == "type":
            kwargs["queryset"] = models.Type.objects.exclude(parent=None)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    prepopulated_fields = {
        'slug': ('title',)
    }


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'rating')


@admin.register(models.SocialAccount)
class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'icon', 'url')


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'message')


@admin.register(models.Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'bio')

    def has_add_permission(self, request, obj=None):
        from .models import Home
        if Home.objects.all():
            return False
        return True


@admin.register(models.Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'email',)
