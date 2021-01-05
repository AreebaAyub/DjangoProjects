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
    path("commentreply",views.commentreply,name='commentreply'),
    path("howtouse", views.how, name='how'),
    path("about", views.aboutt, name='about'),
    path("mcat", views.mcat, name='mcat'),
    path("ecat", views.ecat, name='ecat'),
    path("contactus", views.contact, name='ecat'),
    path("annouce", views.annouce, name='annouce'),
]
urlpatterns=urlpatterns+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)