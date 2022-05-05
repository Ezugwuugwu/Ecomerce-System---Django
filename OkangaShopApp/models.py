from django.db import models


# Create your models here.

class Okanga(models.Model):
    item_title = models.CharField(max_length=80)
    item_description = models.TextField(max_length=15000)
    item_image = models.TextField(default="")

    item_amount = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    initial_item_amount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.item_title
