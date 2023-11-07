from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import ShareOut
from digi_save_vsla_api.serializers import ShareOutSerializer
from digi_save_vsla_api.models import *
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def share_out_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            group_id = data.get('group_id')
            cycle_id = data.get('cycleId')
            users_id = data.get('users_id')
            share_value = data.get('share_value')

            # Get the related instances based on their IDs
            group = GroupProfile.objects.get(id=group_id)
            cycle = CycleMeeting.objects.get(id=cycle_id)
            users = Users.objects.get(id=users_id)

            share_out = ShareOut(
                group=group,
                cycleId=cycle,
                users=users,
                share_value=share_value,
            )
            share_out.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Share out created successfully',
            })

        if request.method == 'GET':
            share_out_list = ShareOut.objects.all()
            share_out_data = []
            for share_out in share_out_list:
                share_out_data.append({
                    'group_id': share_out.group.id,
                    'cycleId': share_out.cycleId.id,
                    'users_id': share_out.users.id,
                    'share_value': share_out.share_value,
                })
            return JsonResponse({
                'status': 'success',
                'share_out_list': share_out_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

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