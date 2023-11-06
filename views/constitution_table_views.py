from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from digi_save_vsla_api.models import ConstitutionTable, GroupProfile
from digi_save_vsla_api.serializers import ConstitutionTableSerializer

@api_view(['GET', 'POST'])
def constitution_table_list(request):
    print("Received data:", request.data)
    data = request.data
    try:
        if request.method == 'POST':
            group_id = data.get('group_id')
            hasConstitution = data.get('hasConstitution')
            constitutionFiles = data.get('constitutionFiles')
            usesGroupShares = data.get('usesGroupShares')
            shareValue = data.get('shareValue')
            maxSharesPerMember = data.get('maxSharesPerMember')
            minSharesRequired = data.get('minSharesRequired')
            frequencyOfContributions = data.get('frequencyOfContributions')
            offersLoans = data.get('offersLoans')
            maxLoanAmount = data.get('maxLoanAmount')
            interestRate = data.get('interestRate')
            interestMethod = data.get('interestMethod')
            loanTerms = data.get('loanTerms')
            registrationFee = data.get('registrationFee')
            selectedCollateralRequirements = data.get('selectedCollateralRequirements')

            # Get the GroupProfile instance based on the group_id
            group_profile = GroupProfile.objects.get(id=group_id)

            constitution = ConstitutionTable(
                group_id=group_profile,
                hasConstitution=hasConstitution,
                constitutionFiles=constitutionFiles,
                usesGroupShares=usesGroupShares,
                shareValue=shareValue,
                maxSharesPerMember=maxSharesPerMember,
                minSharesRequired=minSharesRequired,
                frequencyOfContributions=frequencyOfContributions,
                offersLoans=offersLoans,
                maxLoanAmount=maxLoanAmount,
                interestRate=interestRate,
                interestMethod=interestMethod,
                loanTerms=loanTerms,
                registrationFee=registrationFee,
                selectedCollateralRequirements=selectedCollateralRequirements,
            )
            constitution.save()

            return JsonResponse({
                'status': 'success',
                'message': 'Constitution created successfully',
            })

        if request.method == 'GET':
            constitutions = ConstitutionTable.objects.all()
            constitution_data = []
            for constitution in constitutions:
                constitution_data.append({
                    'group_id': constitution.group_id.id,
                    'hasConstitution': constitution.hasConstitution,
                    'constitutionFiles': constitution.constitutionFiles,
                    'usesGroupShares': constitution.usesGroupShares,
                    'shareValue': constitution.shareValue,
                    'maxSharesPerMember': constitution.maxSharesPerMember,
                    'minSharesRequired': constitution.minSharesRequired,
                    'frequencyOfContributions': constitution.frequencyOfContributions,
                    'offersLoans': constitution.offersLoans,
                    'maxLoanAmount': constitution.maxLoanAmount,
                    'interestRate': constitution.interestRate,
                    'interestMethod': constitution.interestMethod,
                    'loanTerms': constitution.loanTerms,
                    'registrationFee': constitution.registrationFee,
                    'selectedCollateralRequirements': constitution.selectedCollateralRequirements,
                })
            return JsonResponse({
                'status': 'success',
                'constitutions': constitution_data,
            })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e),
        }, status=500)


@api_view(['GET', 'PUT', 'DELETE'])
def constitution_table_detail(request, pk):
    try:
        constitution_table = ConstitutionTable.objects.get(pk=pk)
    except ConstitutionTable.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ConstitutionTableSerializer(constitution_table)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ConstitutionTableSerializer(constitution_table, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        constitution_table.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
