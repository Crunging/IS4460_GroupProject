from django.urls import path
from .views import AccessRecordsListView, AccessRecordsDetailView, AccessRecordsCreateView, AccessRecordsUpdateView, AccessRecordsDeleteView

urlpatterns = [
    # URL pattern for the list view of access permissions
    path('', AccessRecordsListView.as_view(), name='accessrecord_list'),
    
    # URL pattern for the detail view of a specific access permission
    path('<int:pk>/', AccessRecordsDetailView.as_view(), name='accessrecord_detail'),
    
    # URL pattern for creating a new access permission
    path('create/', AccessRecordsCreateView.as_view(), name='accessrecord_form'),
    
    # URL pattern for updating an existing access permission
    path('<int:pk>/update/', AccessRecordsUpdateView.as_view(), name='accessrecord_form'),
    
    # URL pattern for deleting an access permission
    path('<int:pk>/delete/', AccessRecordsDeleteView.as_view(), name='accessrecord_confirm_delete'),
]
