from django.contrib import admin

# Register your models here.

from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sex', 'profession', 'email', 'qq', 'phone', 'status', 'created_time')
    list_filter = ('sex', 'status', 'created_time')
    search_fields = ('name', 'profession')
    search_fieldsets = ('name', 'profession')
    fieldsets = (
        (
            None, {
                'fields': (
                    'name',
                    ('sex', 'profession'),
                    ('email', 'qq', 'phone'),
                    'status',
                )
            }
        ),
    )


admin.site.register(Student, StudentAdmin)