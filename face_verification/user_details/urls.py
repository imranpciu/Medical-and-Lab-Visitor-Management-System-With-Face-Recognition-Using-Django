from django.urls import path
from .views.index_views import IndexView
from .views.add_user_views import AddUserView
from .views.verify_user_views import VerifyUserView
from .views.verify_user_success_views import VerifyUserSuccess
from .views.verify_user_failed_views import VerifyUserfailed
from .views.update_user_views import UpdateUserView
from .views.delete_user_views import DeleteUserView

app_name = "user_details"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("add_user/", AddUserView.as_view(), name="add_user"),
    path(
        "verify_user_success/", VerifyUserSuccess.as_view(), name="verify_user_success"
    ),
    path("verify_user_failed/", VerifyUserfailed.as_view(), name="verify_user_failed"),
    path("verify_user/", VerifyUserView.as_view(), name="verify_user"),
    path("delete_user/<int:user_id>/", DeleteUserView.as_view(), name="delete_user"),
    # path("update_user/<str:user_id>/", UpdateUserView.as_view(), name="update_user"),
    path("update_user/<str:pk>/", UpdateUserView.as_view(), name="update_user"),
    # other URL patterns go here
]
