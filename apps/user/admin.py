from django.contrib import admin
from apps.user.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUser(UserAdmin):
    #adjustments
    list_display = (
        'username',
        'email',
        'get_city',
        'is_staff',

    )
    @admin.display(description = "Cities")
    def get_city(self,obj):
        return ", ".join([location.city for location in obj.location.all()])
    


admin.site.register(User, CustomUser)