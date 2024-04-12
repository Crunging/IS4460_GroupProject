from django.urls import path
from .views import BuildingList, BuildingDetail, BuildingAdd, BuildingUpdate, BuildingDelete

urlpatterns = [
    path('', BuildingList.as_view(), name='building_list'),
    path('<int:BuildingID>/', BuildingDetail.as_view(), name='building_detail'),
    path('create/', BuildingAdd.as_view(), name='building_create'),
    path('<int:BuildingID>/update/', BuildingUpdate.as_view(), name='building_update'),
    path('<int:BuildingID>/delete/', BuildingDelete.as_view(), name='building_delete'),
]
