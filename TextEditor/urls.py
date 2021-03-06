from django.conf.urls import include, url
import django.contrib.auth.views
from django.contrib import admin
from . import views
from webapps import settings
from django.views.static import serve
from TextEditor.forms import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.loadDashboard),
    #url(r'^$', views.signup),#django.contrib.auth.views.login, {'template_name':'login.html'}),
    url(r'^login$', django.contrib.auth.views.login, 
        {'template_name':'signup.html', 
        'extra_context': {'signupform': SignupNewUser()}},
        name='login'),
	url(r'^signup$', views.signup, name = 'signup'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^update_profile$', views.updateProfile, name='profile'),
    url(r'^save_document/(?P<docID>\d+)', views.saveDocument, name='save_document'),
    url(r'^dashboard', views.loadDashboard, name = 'dashboard'),
    url(r'^editor/(?P<docID>\d+)', views.loadEditor),
    url(r'^share/(?P<docID>\d+)', views.share, name='share'),
    url(r'^load_document/(?P<docID>\d+)', views.loadDocument),
    url(r'^confirm/(?P<token>\S+)', views.confirm_registration, name = 'confirm'),
    url(r'^translate/(.+?)/(\S+)', views.translate),
    url(r'^lookup/(.*)', views.lookup),
    url(r'^logout$', django.contrib.auth.views.logout_then_login, name='logout'),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^delete_document/(?P<docID>\d+)', views.deleteDocument, name='delete_document'),
    url(r'^email-for-password-reset$',views.email_for_password_reset, name='email_for_password_reset'),
    url(r'^reset-password/(?P<token>\S+)$', views.reset_password, name = 'reset_password'),

]