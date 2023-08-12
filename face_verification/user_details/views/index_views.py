from django.views.generic import TemplateView
from django.shortcuts import render
from user_details.model.add_user_models import User


class IndexView(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        all_users = User.objects.all()
        return self.render_to_response({'all_users': all_users})


# from django.shortcuts import render
# from user_details.model.add_user_models import User
# from django.views.generic import TemplateView


# def index(request):
#     all_users = User.objects.all()
#     return render(request, 'index.html', {'all_users': all_users})

# index_views.py


# def index(request):
#     users = User.objects.all()
#     print(users)  # Add this line to check if data is being retrieved successfully
#     return render(request, 'index.html', {'all_users': users})


# class IndexView(TemplateView):
#     template_name = 'user_details/index.html'

#     def get(self, request, *args, **kwargs):
#         all_users = User.objects.all()
#         print(all_users)
#         return self.render_to_response({'all_users': all_users})
