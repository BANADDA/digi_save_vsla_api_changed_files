from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import Shares
from digi_save_vsla_api.serializers import SharesSerializer
from digi_save_vsla_api.models import *
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def shares_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            sharePurchases = data.get('sharePurchases')
            meeting_id = data.get('meetingId')
            cycle_id = data.get('cycle_id')
            group_id = data.get('group_id')

            # Get the related instances based on their IDs
            meeting = Meeting.objects.get(id=meeting_id)
            cycle = CycleMeeting.objects.get(id=cycle_id)
            group = GroupForm.objects.get(id=group_id)

            shares = Shares(
                sharePurchases=sharePurchases,
                meetingId=meeting,
                cycle_id=cycle,
                group_id=group,
            )
            shares.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Shares created successfully',
            })

        if request.method == 'GET':
            shares_list = Shares.objects.all()
            shares_data = []
            for share in shares_list:
                shares_data.append({
                    'sharePurchases': share.sharePurchases,
                    'meetingId': share.meetingId.id,
                    'cycle_id': share.cycle_id.id,
                    'group_id': share.group_id.id,
                })
            return JsonResponse({
                'status': 'success',
                'shares_list': shares_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)
@api_view(['GET', 'PUT', 'DELETE'])
def shares_detail(request, pk):
    try:
        shares = Shares.objects.get(pk=pk)
    except Shares.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SharesSerializer(shares)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SharesSerializer(shares, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        shares.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)