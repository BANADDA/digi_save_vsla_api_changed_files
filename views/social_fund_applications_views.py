from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import SocialFundApplications
from digi_save_vsla_api.serializers import SocialFundApplicationsSerializer

@api_view(['GET', 'POST'])
def social_fund_applications_list(request):
    if request.method == 'GET':
        social_fund_applications = SocialFundApplications.objects.all()
        serializer = SocialFundApplicationsSerializer(social_fund_applications, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SocialFundApplicationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def social_fund_applications_detail(request, pk):
    try:
        social_fund_application = SocialFundApplications.objects.get(pk=pk)
    except SocialFundApplications.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SocialFundApplicationsSerializer(social_fund_application)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SocialFundApplicationsSerializer(social_fund_application, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        social_fund_application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)