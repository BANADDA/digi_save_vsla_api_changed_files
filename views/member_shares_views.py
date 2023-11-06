from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import MemberShares
from digi_save_vsla_api.serializers import MemberSharesSerializer

@api_view(['GET', 'POST'])
def member_shares_list(request):
    if request.method == 'GET':
        member_shares = MemberShares.objects.all()
        serializer = MemberSharesSerializer(member_shares, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MemberSharesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def member_shares_detail(request, pk):
    try:
        member_shares = MemberShares.objects.get(pk=pk)
    except MemberShares.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MemberSharesSerializer(member_shares)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MemberSharesSerializer(member_shares, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        member_shares.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)