from django.conf.urls import url
from interventions.views import InterventionListView,InterventionDetailView

urlpatterns = [
    url(r'^$', InterventionListView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', InterventionDetailView.as_view()),
]