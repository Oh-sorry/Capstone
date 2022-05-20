from django.urls import path as url, include

app_name = 'test_app'
urlpatterns = [
    url('', include('rest_framework.urls', namespace='rest_framework_category')),
]