from rest_framework import serializers

from leads.models import Lead
from customers.models import Customer
from deals.models import Deal

from tasks_app.models import Task
from followups.models import FollowUp
from companies.models import Company
from accounts.models import User


class LeadSerializer(serializers.ModelSerializer):

    class Meta:

        model = Lead

        exclude = ('company',)


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:

        model = Customer

        fields = '__all__'


class DealSerializer(serializers.ModelSerializer):

    class Meta:

        model = Deal

        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):

    class Meta:

        model = Task

        fields = '__all__'

class FollowUpSerializer(serializers.ModelSerializer):

    class Meta:

        model = FollowUp

        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):

    class Meta:

        model = Company

        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        exclude = ('password',)