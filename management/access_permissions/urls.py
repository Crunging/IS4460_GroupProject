from django.urls import path
from .views import access_permission_report, AccessPermissionList, AccessPermissionDetail, AccessPermissionCreate, AccessPermissionUpdate, AccessPermissionDelete


urlpatterns = [
    path('', AccessPermissionList.as_view(), name='accesspermission_list'),
    path('<int:AccessID>/', AccessPermissionDetail.as_view(), name='accesspermission_detail'),
    path('create/', AccessPermissionCreate.as_view(), name='accesspermission_create'),
    path('<int:AccessID>/update/', AccessPermissionUpdate.as_view(), name='accesspermission_update'),
    path('<int:AccessID>/delete/', AccessPermissionDelete.as_view(), name='accesspermission_delete'),
    path('apr', access_permission_report, name='access_permission_report'),
]
