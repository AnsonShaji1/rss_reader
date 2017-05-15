from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.home,name='home'),
    url(r'sign/$',views.sign_in,name='sign_in'),
    url(r'register/$',views.register,name="register"),
    url(r'add/$',views.add_data,name='add_data'),
    url(r'display/$',views.display_all,name="display_all"),
    url(r'content/(?P<pk>\d+)/$',views.content,name="content"),
    url(r'^logout/',views.logout_view,name='logout'),

]