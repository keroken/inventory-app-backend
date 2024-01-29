from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework import status

class ProductView(APIView):
  """
  商品操作に関する関数
  """
  def get(self, request, format=None):
    """
    商品の一覧を取得する
    """
    queryset = Product.objects.all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data, status.HTTP_200_OK)
  
  def post(self, request, format=None):
    """
    商品情報を登録する
    """
    serializer = ProductSerializer(data=request.data)
    # validationを通らなかった場合、例外を投げる
    serializer.is_valid(raise_exception=True)
    # 検証したデータを永続化する
    serializer.save()
    return Response(serializer.data, status.HTTP_201_CREATED)

