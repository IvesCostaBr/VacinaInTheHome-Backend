from django.contrib import admin
from .models import User, Endereco

from django.contrib.auth.admin import UserAdmin


from .models import User


class CustomUserAdmin(UserAdmin):
    model = User
    list_editable = ()
    list_display = ('cpf','card_sus','first_name','last_name','is_staff', 'is_active','adress')
    list_filter = ('email', 'is_staff', 'is_active','adress')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active','adress')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    


admin.site.register(User, CustomUserAdmin)
admin.site.register(Endereco)