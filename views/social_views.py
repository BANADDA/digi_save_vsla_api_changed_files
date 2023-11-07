from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import Social
from digi_save_vsla_api.serializers import SocialSerializer
from digi_save_vsla_api.models import *
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def social_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            socialFund = data.get('socialFund')
            meeting_id = data.get('meetingId')

            # Get the related meeting instance based on its ID
            meeting = Meeting.objects.get(id=meeting_id)

            social = Social(
                socialFund=socialFund,
                meetingId=meeting,
            )
            social.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Social fund created successfully',
            })

        if request.method == 'GET':
            social_list = Social.objects.all()
            social_data = []
            for social in social_list:
                social_data.append({
                    'socialFund': social.socialFund,
                    'meetingId': social.meetingId.id,
                })
            return JsonResponse({
                'status': 'success',
                'social_list': social_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

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