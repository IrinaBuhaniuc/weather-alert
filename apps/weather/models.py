from django.db import models


from apps.core.models import CreatedModifiedAtBase

# Create your models here.

class Location(CreatedModifiedAtBase):
    city = models.CharField(max_length=100, null = False, help_text="Add city to receive alerts")
    country = models.CharField(max_length=50, null= False, default = "")
    lat = models.CharField(max_length=100)
    long = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.country},{self.city}"

 
class User_Location(CreatedModifiedAtBase):
    user_id = models.ForeignKey("user.User", on_delete=models.CASCADE)   
    location_id = models.ForeignKey("weather.Location", on_delete=models.CASCADE)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                'user_id',
                'location_id',
                name = 'user_location_unique',
                violation_error_message = "This City was already added to specified user"
            )
        ]

    
class Log(CreatedModifiedAtBase):
    modified_at = None
    user_id = models.ForeignKey("user.User", null = False, on_delete=models.CASCADE)
    location_id = models.ForeignKey("weather.Location", on_delete=models.CASCADE)
    
class Weather_Status(CreatedModifiedAtBase):
    modified_at = None
    status = models.CharField(max_length=100) 
    location_id = models.ForeignKey("weather.Location", on_delete=models.CASCADE) 