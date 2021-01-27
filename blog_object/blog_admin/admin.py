from django.contrib import admin
from blog_admin import models


# Register your models here.

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'content',
        'sys_create_time',
        'sys_update_time',
        'click_nums',
        'category',
    )
    pass
