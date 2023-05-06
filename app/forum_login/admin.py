from django.contrib import admin
from .models import CustomUser, Address
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'name', 'is_staff',)
    list_filter = ('email', 'name', 'is_staff',)

    fieldsets = (
        (None, {'fields': ('email', 'password',)}),
        ('Personal info', {'fields': ('name', 'address', 'gender', 'description', 'avatar', )}),
        ('Permissions', {'fields': ('is_staff', 'tofu_credit',)}),
    )

    add_fieldsets = ( 
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'is_staff',
            )
        }),
    )

    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)