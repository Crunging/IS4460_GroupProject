from django.urls import path
from .views import AccessPermissionListView, AccessPermissionDetailView, AccessPermissionCreateView, AccessPermissionUpdateView, AccessPermissionDeleteView

urlpatterns = [
    # URL pattern for the list view of access permissions
    path('', AccessPermissionListView.as_view(), name='access_permission_list'),
    
    # URL pattern for the detail view of a specific access permission
    path('<int:pk>/', AccessPermissionDetailView.as_view(), name='access_permission_detail'),
    
    # URL pattern for creating a new access permission
    path('create/', AccessPermissionCreateView.as_view(), name='access_permission_create'),
    
    # URL pattern for updating an existing access permission
    path('<int:pk>/update/', AccessPermissionUpdateView.as_view(), name='access_permission_update'),
    
    # URL pattern for deleting an access permission
    path('<int:pk>/delete/', AccessPermissionDeleteView.as_view(), name='access_permission_delete'),
]

