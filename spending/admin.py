from django.contrib import admin
from .models import Category, Spending

admin.site.register(Category)

@admin.register(Spending)
class SpendingAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'description', 'display_category')

    fieldsets = (
        (None, {
            'fields': ('title', 'value')
        }),
        ('category', {
            'fields': ('category', )
        }),
        ('Summary', {
            'fields': ('description', )
        })
    )