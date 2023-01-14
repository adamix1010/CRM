from CRM.urls import path
from .views import LeadList, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView

app_name = "Leads"
urlpatterns = [
    path('', LeadList.as_view(), name='lead-list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-detail'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),
    path('create/', LeadCreateView.as_view(), name='lead-create'),
]
