from django.contrib import admin
from Core.models import UserProfile, UserDonateMoMo

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["__str__", "id", "dateofbirth", "userpic", "gender", "contact", "nationality", "levelofeducation"]
    list_filter = ["id"]
    list_display_links = ["dateofbirth"]
    search_fields = ["contact", "levelofeducation"]  # this will make the title and content searchable

    class Meta:
        model = UserProfile


class UserDonateAdmin(admin.ModelAdmin):
    list_display = ["__str__", "id", "phonenumber", "email", "comment", "transactionId", "amount", "statusCode"]
    list_filter = ["phonenumber", "email", "transactionId"]
    list_display_links = ["phonenumber"]
    search_fields = ["phonenumber", "email", "transactionId"]  # this will make the title and content searchable

    class Meta:
        model = UserDonateMoMo


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserDonateMoMo, UserDonateAdmin)
