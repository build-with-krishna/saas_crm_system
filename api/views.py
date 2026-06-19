from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from leads.models import Lead
from customers.models import Customer
from deals.models import Deal

from tasks_app.models import Task
from followups.models import FollowUp
from companies.models import Company
from accounts.models import User
from rest_framework.response import Response

from rest_framework.views import APIView

from .serializers import (
    LeadSerializer,
    CustomerSerializer,
    DealSerializer
)

from .serializers import (
    TaskSerializer,
    FollowUpSerializer,
    CompanySerializer,
    UserSerializer
)


class LeadViewSet(viewsets.ModelViewSet):

    serializer_class = LeadSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
         # Swagger schema generation ke liye
        if getattr(self, 'swagger_fake_view', False):
            return Lead.objects.none()

        if not self.request.user.is_authenticated:
            return Lead.objects.none()
        
        return Lead.objects.filter(
            company=self.request.user.company
        )
    


class CustomerViewSet(viewsets.ModelViewSet):

    serializer_class = CustomerSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        # Swagger schema generation ke liye
        if getattr(self, 'swagger_fake_view', False):
            return Customer.objects.none()

        if not self.request.user.is_authenticated:
            return Customer.objects.none()

        return Customer.objects.filter(
            company=self.request.user.company
        )


class DealViewSet(viewsets.ModelViewSet):

    serializer_class = DealSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):

        # Swagger schema generation ke liye
        if getattr(self, 'swagger_fake_view', False):
            return Deal.objects.none()

        if not self.request.user.is_authenticated:
            return Deal.objects.none()

        return Deal.objects.filter(
            company=self.request.user.company
        )
    


class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer

    def get_queryset(self):

        # Swagger schema generation ke liye
        if getattr(self, 'swagger_fake_view', False):
            return Task.objects.none()

        if not self.request.user.is_authenticated:
            return Task.objects.none()

        return Task.objects.filter(
            company=self.request.user.company
        )
    



class FollowUpViewSet(viewsets.ModelViewSet):

    serializer_class = FollowUpSerializer

    def get_queryset(self):

        # Swagger schema generation ke liye
        if getattr(self, 'swagger_fake_view', False):
            return FollowUp.objects.none()

        if not self.request.user.is_authenticated:
            return FollowUp.objects.none()

        return FollowUp.objects.filter(
            company=self.request.user.company
        )
    


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = CompanySerializer

    def get_queryset(self):

        # Swagger schema generation ke liye
        if getattr(self, 'swagger_fake_view', False):
            return Company.objects.none()

        if not self.request.user.is_authenticated:
            return Company.objects.none()

        return Company.objects.filter(
            id=self.request.user.company.id
        )
    



class ProfileViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):

        # Swagger schema generation ke liye
        if getattr(self, 'swagger_fake_view', False):
            return User.objects.none()

        if not self.request.user.is_authenticated:
            return User.objects.none()

        return User.objects.filter(
            id=self.request.user.id
        )
    



from leads.models import Lead
from customers.models import Customer
from deals.models import Deal


class DashboardAPIView(APIView):

    def get(self, request):

        company = request.user.company

        data = {

            'leads': Lead.objects.filter(
                company=company
            ).count(),

            'customers': Customer.objects.filter(
                company=company
            ).count(),

            'deals': Deal.objects.filter(
                company=company
            ).count(),

            'tasks': Task.objects.filter(
                company=company
            ).count(),

        }

        return Response(data)