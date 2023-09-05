from django.contrib import admin
from apps.weather import models

# Register your models here.

class CustomLocation(admin.ModelAdmin):
    list_display = (
        'city',
        'country',
        'lat',
        'long'
    )
    

class CustomUser_Location(admin.ModelAdmin):
    list_display = (
        'get_username',
        'get_city_country',
    )
    @admin.display(description='username')
    def get_username(self,obj):
        return obj.user_id.username
    
    @admin.display(description='city, country')
    def get_city_country(self,obj):
        return f"{obj.location_id.city}({obj.location_id.country})"

class CustomWeather_Status(admin.ModelAdmin):
    list_display =(
        'created_at',
        'status',
        'get_city_country',
    )
    @admin.display(description='City, Country')
    def get_city_country(self,obj):
        return f"{obj.location_id.city}({obj.location_id.country})"


admin.site.register(models.Location, CustomLocation)
admin.site.register(models.Log)
admin.site.register(models.User_Location, CustomUser_Location)
admin.site.register(models.Weather_Status, CustomWeather_Status)