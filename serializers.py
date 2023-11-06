# serializers.py
from rest_framework import serializers
from .models import ActiveCycleMeeting, AssignedPositions, ConstitutionTable, CycleMeeting, CycleSchedules, CycleStartMeeting, Fines, GroupCycleStatus, GroupFees, GroupForm, GroupLink, GroupMembers, GroupProfile, LoanApplications, LoanDisbursement, LoanPayments, Loans, Meeting, MemberShares, PaymentInfo, Positions, ReversedTransactions, SavingsAccount, ShareOut, Shares, Social, SocialFundApplications, Users, WelfareAccount

class GroupFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupForm
        fields = '__all__'

class SavingsAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavingsAccount
        fields = '__all__'
        
class AssignedPositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignedPositions
        fields = '__all__'
        
class ConstitutionTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConstitutionTable
        fields = '__all__'
        
class CycleSchedulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CycleSchedules
        fields = '__all__'
        
class GroupMembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupMembers
        fields = '__all__'
        
class GroupProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupProfile
        fields = '__all__'
        
class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = '__all__'
        
class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = '__all__'

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'fname', 'lname')

        
class GroupFeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupFees
        fields = '__all__'
        
class CycleMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CycleMeeting
        fields = '__all__'
        
class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        fields = '__all__'
        
class MemberSharesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberShares
        fields = '__all__'
        
class WelfareAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = WelfareAccount
        fields = '__all__'
        
class ActiveCycleMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActiveCycleMeeting
        fields = '__all__'
        
class SharesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shares
        fields = '__all__'
        
class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = '__all__'
        
class GroupLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupLink
        fields = '__all__'
        
class LoanApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplications
        fields = '__all__'
        
class SocialFundApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialFundApplications
        fields = '__all__'
        
class CycleStartMeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CycleStartMeeting
        fields = '__all__'
        
class PaymentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentInfo
        fields = '__all__'
        
class FinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fines
        fields = '__all__'
        
class GroupCycleStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupCycleStatus
        fields = '__all__'
        
class LoansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = '__all__'
        
class LoanDisbursementSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanDisbursement
        fields = '__all__'
        
class LoanPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanPayments
        fields = '__all__'
        
class ShareOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShareOut
        fields = '__all__'
        
class ReversedTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReversedTransactions
        fields = '__all__'