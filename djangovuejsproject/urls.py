from django.conf.urls import url
from catalog import views


urlpatterns = [
    url(r'^api/public/', views.public),
    url(r'^api/private/', views.private)
]