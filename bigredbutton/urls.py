from django.urls import path

from .views import (
    SessionDelete,
    SessionList,
)


urlpatterns = [
    path('', SessionList.as_view(), name='list_sessions'),
    path('delete/others/', SessionDelete.as_view(), name='delete_other_sessions'),
]
