from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.translation import activate
from .models import Product
from .serializers import ProductSerializer

class ProductListView(APIView):
    def get(self, request):
        lang = request.query_params.get('lang', 'en')  # Default til: Ingliz
        activate(lang)  # Tilni faollashtirish
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
