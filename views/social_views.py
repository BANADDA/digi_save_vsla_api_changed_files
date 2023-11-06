from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import Social
from digi_save_vsla_api.serializers import SocialSerializer

@api_view(['GET', 'POST'])
def social_list(request):
    if request.method == 'GET':
        socials = Social.objects.all()
        serializer = SocialSerializer(socials, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SocialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def social_detail(request, pk):
    try:
        social = Social.objects.get(pk=pk)
    except Social.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocialSerializer(social)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SocialSerializer(social, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        social.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)