from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateView
from .views import DetailsView
from .views import UserView, UserDetailsView

urlpatterns = {
	path('auth/', include('rest_framework.urls', namespace='rest_framework')),
	path('v1/', CreateView.as_view(), name="create"),
	path('v1/<int:pk>/', DetailsView.as_view(), name="details"),
	path('users/', UserView.as_view(), name="users"),
	path('users/<int:pk>/', UserDetailsView.as_view(), name="user_details"),
	path('get-token/', obtain_auth_token),
}

urlpatterns = format_suffix_patterns(urlpatterns)