import os

from django.conf import settings
from django.conf.urls import patterns, url


if settings.DEBUG:
    urlpatterns = patterns(
        '',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': os.path.join(os.path.dirname(os.path.dirname(__file__)), 'media/'), 'show_indexes': True}),
    ) + urlpatterns
