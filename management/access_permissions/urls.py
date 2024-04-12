from django.urls import path
from .views import (
    AccessPermissionList,
    AccessPermissionDetail,
    AccessPermissionCreate,
    AccessPermissionUpdate,
    AccessPermissionDelete,
)

urlpatterns = [
    path('', AccessPermissionList.as_view(), name='access_permission_list'),
    path('<int:AccessID>/', AccessPermissionDetail.as_view(), name='access_permission_detail'),
    path('create/', AccessPermissionCreate.as_view(), name='access_permission_create'),
    path('<int:AccessID>/update/', AccessPermissionUpdate.as_view(), name='access_permission_update'),
    path('<int:AccessID>/delete/', AccessPermissionDelete.as_view(), name='access_permission_delete'),
]
