from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from rest_framework.authtoken import views as authtoken_views
from django.views.generic.base import TemplateView


from django.conf.urls import url
from django.contrib import admin
from Pentagram.views import users, comment, photos, like

urlpatterns = [
    url(r'^api/v1/login/$', authtoken_views.obtain_auth_token),
    url(r'^api/v1/photos/$', photos, name='photos'),
    url(r'^api/v1/users/$', users, name='users'),
    url(r'^api/photos/(?P<id_photo>[0-9]*)/comments/$', comment, name='comments'),
    url(r'^api/photos/(?P<id_photo>[0-9]*)/like/$', like, name='likes'),
    url(r'^admin/', admin.site.urls),
    url(r'^user/login', auth_views.login, {'template_name': 'login.html'}, name="login"),
    url(r'^$', TemplateView.as_view(template_name='index.html'), name="homepage"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

