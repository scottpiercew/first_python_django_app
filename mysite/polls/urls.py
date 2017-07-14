from django.conf.urls import url

from . import views

urlpatterns = [
    # /polls/
    url(r'^$', views.index, name='index'),
    #Using the parentheses around a pattern “captures” the text matched by that pattern and sends it as an argument to the view function
    # /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
