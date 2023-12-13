from django.urls import path
from . import views, forms
from datetime import datetime
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', views.store, name="store"),

    path('news/', views.news, name="news"),
    path('catalog/', views.catalog, name="catalog"),
    path('contact/', views.contact, name="contact"),
    path('anketa/', views.anketa, name="anketa"),
    path('resurs/', views.resurs, name="resurs"),
    path('registration/', views.registration, name="registration"),
    path('blog/', views.blog, name="blog"),
    path('blogpost/<int:parametr>/', views.blogpost, name="blogpost"),
    path('newpost/', views.newpost, name="newpost"),
    path('videopost/', views.videopost, name="videopost"),
    path('login/',
         LoginView.as_view(
             template_name='store/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context={
                 'title': 'Авторизация',
                 'year': datetime.now().year,
             },
             next_page="/",
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name="logout"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()