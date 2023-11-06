from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import PaymentInfo
from digi_save_vsla_api.serializers import PaymentInfoSerializer

@api_view(['GET', 'POST'])
def payment_info_list(request):
    if request.method == 'GET':
        payment_info = PaymentInfo.objects.all()
        serializer = PaymentInfoSerializer(payment_info, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PaymentInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def payment_info_detail(request, pk):
    try:
        payment_info = PaymentInfo.objects.get(pk=pk)
    except PaymentInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PaymentInfoSerializer(payment_info)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PaymentInfoSerializer(payment_info, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        payment_info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)