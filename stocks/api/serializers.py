from rest_framework.serializers import ModelSerializer
from stocks.models import Company

class CompanySerializer(ModelSerializer):

    class Meta:
        fields = ['name', 'symbol','graph']
        model = Company