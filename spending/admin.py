from django.contrib import admin
from .models import Category, Spending

admin.site.register(Category)

@admin.register(Spending)
class SpendingAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'description', 'display_category', 'date')

    fieldsets = (
        (None, {
            'fields': ('title', 'value')
        }),
        ('category', {
            'fields': ('category', )
        }),
        ('Date', {
            'fields': ('date', )
        }),
        ('Summary', {
            'fields': ('description', )
        })
    )