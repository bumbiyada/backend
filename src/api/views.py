from rest_framework import generics
from .serializers import ApiListSerializer
from .models import ListAll
# Create your views here.


class ApiListView(generics.ListAPIView):
    serializer_class = ApiListSerializer
    queryset = ListAll.objects.all()
