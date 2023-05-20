import random
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from user_details.model.add_user_models import User
from django.urls import reverse
import os
import base64
from django.conf import settings


class AddUserView(TemplateView):
    template_name = "add_user.html"

    def post(self, request, *args, **kwargs):
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

        # Generate a random 8-digit number
        random_number = str(random.randint(10000000, 99999999))

        # Construct the user ID with "LQ" and the random number
        user_id = "LQ" + random_number

        # Decode the base64 image data
        format, imgstr = image.split(";base64,")
        ext = format.split("/")[-1]
        data = base64.b64decode(imgstr)

        # Save the image to the file system
        img_path = os.path.join(settings.BASE_DIR, "media", "users")
        os.makedirs(img_path, exist_ok=True)

        # Construct the img_name with the modified format
        img_name = f"{user_id}.{ext}"

        img_file = os.path.join(img_path, img_name)

        with open(img_file, "wb") as f:
            f.write(data)

        # Save the user object to the database
        user = User(
            user_id=user_id,
            name=name,
            email=email,
            phone=phone,
            gender=gender,
            address=address,
            image=os.path.join("users", img_name),
        )
        user.save()

        return HttpResponseRedirect(reverse("user_details:index"))
