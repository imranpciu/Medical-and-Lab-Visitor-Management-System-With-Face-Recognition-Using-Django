from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views import View
from user_details.model.add_user_models import User

class DeleteUserView(View):
    def post(self, request, user_id):
        user = User.objects.get(id=user_id)
        user.delete()
        return HttpResponseRedirect(reverse("user_details:index"))  # Replace 'index' with the appropriate URL name for the index view
