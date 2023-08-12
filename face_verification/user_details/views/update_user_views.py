import os
import base64
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from user_details.models import User
from django.conf import settings
from django.urls import reverse


class UpdateUserView(TemplateView):
    template_name = "update_user.html"

    def get(self, request, pk, *args, **kwargs):
        user = User.objects.get(user_id=pk)  # Update the parameter name here
        return render(request, self.template_name, {"user": user})

    def post(self, request, pk, *args, **kwargs):
        user = User.objects.get(user_id=pk)
        name = request.POST.get("user_name")
        email = request.POST.get("user_email")
        phone = request.POST.get("user_phone_number")
        gender = request.POST.get("user_gender")
        address = request.POST.get("user_address")
        image = request.POST.get("image")

        if not name:
            return render(
                request, self.template_name, {"error_message": "Name is required"}
            )

        # Update user details
        user.name = name
        user.email = email
        user.phone = phone
        user.gender = gender
        user.address = address

        if image:
            # Decode the base64 image data
            format, imgstr = image.split(";base64,")
            ext = format.split("/")[-1]
            data = base64.b64decode(imgstr)

            # Save the image to the file system
            img_path = os.path.join(settings.MEDIA_ROOT, "users")
            os.makedirs(img_path, exist_ok=True)

            # Construct the img_name with the user_id and modified format
            img_name = f"{user.user_id}.{ext}"

            img_file = os.path.join(img_path, img_name)

            with open(img_file, "wb") as f:
                f.write(data)

            # Update user image path
            user.image = os.path.join("users", img_name)

        user.save()

        return HttpResponseRedirect(reverse("user_details:index"))
