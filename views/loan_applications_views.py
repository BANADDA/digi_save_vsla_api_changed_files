from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import LoanApplications
from digi_save_vsla_api.serializers import LoanApplicationsSerializer

@api_view(['GET', 'POST'])
def loan_applications_list(request):
    if request.method == 'GET':
        loan_applications = LoanApplications.objects.all()
        serializer = LoanApplicationsSerializer(loan_applications, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LoanApplicationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def loan_applications_detail(request, pk):
    try:
        loan_application = LoanApplications.objects.get(pk=pk)
    except LoanApplications.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LoanApplicationsSerializer(loan_application)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LoanApplicationsSerializer(loan_application, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        loan_application.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)