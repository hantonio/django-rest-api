from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView

urlpatterns = {
	path('v1/', CreateView.as_view(), name="create"),
	path('v1/<int:pk>/', DetailsView.as_view(), name="details")
}

urlpatterns = format_suffix_patterns(urlpatterns)