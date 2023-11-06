from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import ShareOut
from digi_save_vsla_api.serializers import ShareOutSerializer

@api_view(['GET', 'POST'])
def share_out_list(request):
    if request.method == 'GET':
        share_outs = ShareOut.objects.all()
        serializer = ShareOutSerializer(share_outs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ShareOutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def share_out_detail(request, pk):
    try:
        share_out = ShareOut.objects.get(pk=pk)
    except ShareOut.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ShareOutSerializer(share_out)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ShareOutSerializer(share_out, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        share_out.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)