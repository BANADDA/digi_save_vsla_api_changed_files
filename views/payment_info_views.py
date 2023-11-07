from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import PaymentInfo
from digi_save_vsla_api.serializers import PaymentInfoSerializer
from digi_save_vsla_api.models import *
from django.http import JsonResponse

@api_view(['GET', 'POST'])
def payment_info_list(request):
    print("Received data:", request.data)
    data = request.data

    try:
        if request.method == 'POST':
            group_id = data.get('group_id')
            cycle_id = data.get('cycle_id')
            meeting_id = data.get('meeting_id')
            member_id = data.get('member_id')
            payment_amount = data.get('payment_amount')
            payment_date = data.get('payment_date')

            # Get the related instances based on their IDs
            group = GroupForm.objects.get(id=group_id)
            cycle = CycleMeeting.objects.get(id=cycle_id)
            meeting = Meeting.objects.get(id=meeting_id)
            member = GroupMembers.objects.get(id=member_id)

            payment_info = PaymentInfo(
                group=group,
                cycle_id=cycle,
                meeting_id=meeting,
                member=member,
                payment_amount=payment_amount,
                payment_date=payment_date,
            )
            payment_info.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Payment information created successfully',
            })

        if request.method == 'GET':
            payment_info_list = PaymentInfo.objects.all()
            payment_info_data = []
            for payment_info in payment_info_list:
                payment_info_data.append({
                    'group_id': payment_info.group.id,
                    'cycle_id': payment_info.cycle_id.id,
                    'meeting_id': payment_info.meeting_id.id,
                    'member_id': payment_info.member.id,
                    'payment_amount': payment_info.payment_amount,
                    'payment_date': payment_info.payment_date,
                })
            return JsonResponse({
                'status': 'success',
                'payment_info_list': payment_info_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)

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