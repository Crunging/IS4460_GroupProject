from django.urls import path
from . import views
from .views import RoomList, RoomDetail, RoomUpdate, RoomDelete, RoomCreate

urlpatterns = [
    path('', RoomList.as_view(), name='rooms.view'),
    path('<int:room_id>/', RoomDetail.as_view(), name='rooms_detail'),  # Changed name to 'room_update'
    path('<int:RoomID>/update/', RoomUpdate.as_view(), name='rooms_update'),  # Changed name to 'room_update'
    path('<int:RoomID>/delete/', RoomDelete.as_view(), name='rooms_delete'),  # Changed name to 'room_delete'
    path('add/', RoomCreate.as_view(), name='rooms_add'),  # Changed URL pattern to remove 'room_id'
]

