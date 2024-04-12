from django.urls import path
from .views import RoomsView, RoomsUpdate, RoomsDelete, RoomsAdd

urlpatterns = [
    path('', RoomsView.as_view(), name='rooms_view'),
    path('<int:room_id>/', RoomsUpdate.as_view(), name='room_update'),  # Changed name to 'room_update'
    path('<int:room_id>/update/', RoomsUpdate.as_view(), name='room_update'),  # Changed name to 'room_update'
    path('<int:room_id>/delete/', RoomsDelete.as_view(), name='room_delete'),  # Changed name to 'room_delete'
    path('add/', RoomsAdd.as_view(), name='room_add'),  # Changed URL pattern to remove 'room_id'
]

