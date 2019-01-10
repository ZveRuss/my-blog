from django.conf.urls import url
from . import views

urlpatterns = [
    url('blog/', views.post_list, name='post_list'),        
]
