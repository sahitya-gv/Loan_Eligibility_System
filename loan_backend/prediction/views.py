from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .serializers import LoanInputSerializer
from ml.predictor import predict_loan


class PredictView(APIView):
    permission_classes = [AllowAny]   # switch to IsAuthenticated after Developer 1's login works

    def post(self, request):
        serializer = LoanInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)   # bad input returns a 400 error
        result = predict_loan(dict(serializer.validated_data))
        return Response(result)
