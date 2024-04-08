from django.urls import path
from .views import BuildingList, BuildingDetail, BuildingCreate, BuildingUpdate, BuildingDelete

urlpatterns = [
    path('', BuildingList.as_view(), name='building_list'),
    path('<int:BuildingID>/', BuildingnDetail.as_view(), name='building_detail'),
    path('create/', BuildingCreate.as_view(), name='building_create'),
    path('<int:BuildingID>/update/', BuildingUpdate.as_view(), name='building_update'),
    path('<int:BuildingID>/delete/', BuildingDelete.as_view(), name='building_delete'),
]
