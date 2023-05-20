from django.contrib import admin

# Register your models here.
from django.contrib import admin
from user_details.model.add_user_models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass
