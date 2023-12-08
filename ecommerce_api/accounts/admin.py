from django.contrib import admin
from .models import CustomUser,Profile
from .forms import CustomUserChangeForm,CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser
    list_display=[
        "name",
        "email",
        "address",
        "phone_number",
        "is_staff",
        "is_active",
        "is_superuser",
        "date_joined",
    ]
    fieldsets=UserAdmin.fieldsets+((None,{"fields":("name","address","phone_number",)}),)
    add_fieldsets=UserAdmin.fieldsets+((None,{"fields":("name","address","phone_number",)}),)
    ordering=["name"]
    list_filter=["is_staff","is_active","is_superuser"]
    search_fields=["name","email","address","phone_number"]

admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['user','photo']
    list_filter=['date_joined']
