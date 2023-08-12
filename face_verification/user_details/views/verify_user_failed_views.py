from django.views.generic import TemplateView
from user_details.model.add_user_models import User


class VerifyUserfailed(TemplateView):
    template_name = "verify_user_failed.html"
