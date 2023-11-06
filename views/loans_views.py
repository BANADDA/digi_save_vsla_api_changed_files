from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import Loans
from digi_save_vsla_api.serializers import LoansSerializer

@api_view(['GET', 'POST'])
def loans_list(request):
    if request.method == 'GET':
        loans = Loans.objects.all()
        serializer = LoansSerializer(loans, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LoansSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def loans_detail(request, pk):
    try:
        loans = Loans.objects.get(pk=pk)
    except Loans.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LoansSerializer(loans)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LoansSerializer(loans, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        loans.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
