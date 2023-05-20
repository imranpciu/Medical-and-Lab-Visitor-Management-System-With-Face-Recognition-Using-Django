from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage

class User(models.Model):
    user_id = models.CharField(max_length=10, unique=True, default='LQ00000011')
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(max_length=254, verbose_name="Email Address")
    phone = models.CharField(max_length=15, verbose_name="Phone Number")
    gender = models.CharField(max_length=10, verbose_name="Gender")
    address = models.TextField(verbose_name="Address")
    image = models.ImageField(
        upload_to="users/", blank=True, null=True, verbose_name="Profile Image"
    )

    def delete(self, *args, **kwargs):
        # Delete the associated image file
        if self.image:
            # Construct the path to the image file
            path = f"{settings.MEDIA_ROOT}/users/{self.user_id}.png"

            # Delete the file from storage
            if default_storage.exists(path):
                default_storage.delete(path)

        # Call the delete method of the parent class
        super().delete(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return self.name

