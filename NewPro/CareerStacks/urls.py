from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path("",views.home,name='home'),
    path("login.html", views.loginredircect, name='login'),
    path("userreg.html",views.registerdirect, name='userreg'),
    path("reg",views.UserRegistration,name='userreg'),
    path("login",views.UserLogin,name='userlogin'),
    path("query",views.query,name='query'),
    path("commentpost",views.query,name='query2'),
    path("commentreply",views.commentreply,name='commentreply')
]
urlpatterns=urlpatterns+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)