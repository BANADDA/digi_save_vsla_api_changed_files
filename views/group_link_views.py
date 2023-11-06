# views/group_link_views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import GroupLink
from digi_save_vsla_api.serializers import GroupLinkSerializer

@api_view(['GET', 'POST'])
def group_link_list(request):
    if request.method == 'GET':
        group_links = GroupLink.objects.all()
        serializer = GroupLinkSerializer(group_links, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GroupLinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def group_link_detail(request, pk):
    try:
        group_link = GroupLink.objects.get(pk=pk)
    except GroupLink.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GroupLinkSerializer(group_link)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GroupLinkSerializer(group_link, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        group_link.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
