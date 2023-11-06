from django.db import models

# Create your models here.
class GroupProfile(models.Model):
    groupName = models.CharField(max_length=255, default=None, blank=True, null=True)
    countryOfOrigin = models.CharField(max_length=255, default=None, blank=True, null=True)
    meetingLocation = models.CharField(max_length=255, default=None, blank=True, null=True)
    groupStatus = models.CharField(max_length=255, default=None, blank=True, null=True)
    groupLogoPath = models.CharField(max_length=255, default=None, blank=True, null=True)
    partnerID = models.CharField(max_length=255, default=None, blank=True, null=True)
    workingWithPartner = models.CharField(max_length=255, default=None, blank=True, null=True)
    isWorkingWithPartner = models.IntegerField(default=None, blank=True, null=True)
    numberOfCycles = models.CharField(max_length=255, default=None, blank=True, null=True)
    numberOfMeetings = models.CharField(max_length=255, default=None, blank=True, null=True)
    loanFund = models.CharField(max_length=255, default=None, blank=True, null=True)
    socialFund = models.CharField(max_length=255, default=None, blank=True, null=True)
    sync_flag = models.IntegerField(default=0)

    def __str__(self):
        return self.groupName
    
class ConstitutionTable(models.Model):
    group_id = models.ForeignKey(GroupProfile, on_delete=models.CASCADE)
    hasConstitution = models.IntegerField(default=None, blank=True, null=True)
    constitutionFiles = models.BinaryField(default=None, blank=True, null=True)
    usesGroupShares = models.BooleanField(default=None, blank=True, null=True)
    shareValue = models.FloatField(default=None, blank=True, null=True)
    maxSharesPerMember = models.IntegerField(default=None, blank=True, null=True)
    minSharesRequired = models.IntegerField(default=None, blank=True, null=True)
    frequencyOfContributions = models.CharField(max_length=255, default=None, blank=True, null=True)
    offersLoans = models.BooleanField(default=None, blank=True, null=True)
    maxLoanAmount = models.FloatField(default=None, blank=True, null=True)
    interestRate = models.FloatField(default=None, blank=True, null=True)
    interestMethod = models.CharField(max_length=255, default=None, blank=True, null=True)
    loanTerms = models.CharField(max_length=255, default=None, blank=True, null=True)
    registrationFee = models.CharField(max_length=255, default=None, blank=True, null=True)
    selectedCollateralRequirements = models.CharField(max_length=255, default=None, blank=True, null=True)
    sync_flag = models.IntegerField(default=0)

    def __str__(self):
        return f"ConstitutionTable for Group ID: {self.group_id}  - Has Constitution: {self.hasConstitution}"

class Users(models.Model):
    unique_code = models.TextField()
    fname = models.TextField()
    lname = models.TextField()
    email = models.TextField(default=None, blank=True, null=True)
    phone = models.TextField()
    sex = models.TextField()
    country = models.TextField()
    date_of_birth = models.TextField()
    image = models.TextField(default=None, blank=True, null=True)
    district = models.TextField()
    subCounty = models.TextField()
    village = models.TextField()
    number_of_dependents = models.TextField()
    family_information = models.TextField()
    next_of_kin_name = models.TextField()
    next_of_kin_has_phone_number = models.IntegerField(default=None, blank=True, null=True)
    next_of_kin_phone_number = models.TextField(default=None, blank=True, null=True)
    pwd_type = models.TextField(default=None, blank=True, null=True)
    sync_flag = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.fname} {self.lname}"

class GroupMembers(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    group_id = models.ForeignKey(GroupProfile, on_delete=models.CASCADE)
    sync_flag = models.IntegerField(default=0)

    def __str__(self):
        return f"GroupMember {self.user_id} for Group ID: {self.group_id}"

class CycleSchedules(models.Model):
    group_id = models.ForeignKey(GroupProfile, on_delete=models.CASCADE)
    meeting_duration = models.TextField()
    number_of_meetings = models.IntegerField()
    meeting_frequency = models.TextField()
    day_of_week = models.TextField()
    start_date = models.TextField()
    share_out_date = models.TextField()
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return f"CycleSchedules for Group ID: {self.group_id}"
    

class Positions(models.Model):
    name = models.TextField()
    sync_flag = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
class AssignedPositions(models.Model):
    position_id = models.ForeignKey(Positions, on_delete=models.CASCADE)
    member_id = models.ForeignKey(GroupMembers, on_delete=models.CASCADE)
    group_id = models.ForeignKey(GroupProfile, on_delete=models.CASCADE)
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return self.position

class GroupForm(models.Model):
    group_profile = models.ForeignKey(GroupProfile, on_delete=models.CASCADE)
    group_id = models.IntegerField()
    logged_in_users_id = models.IntegerField()
    constitution = models.ForeignKey(ConstitutionTable, on_delete=models.CASCADE)
    cycle_schedule = models.ForeignKey(CycleSchedules, on_delete=models.CASCADE)
    group_member = models.ForeignKey(GroupMembers, on_delete=models.CASCADE)
    assigned_position = models.ForeignKey(AssignedPositions, on_delete=models.CASCADE)
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return self.group_id
    
class SavingsAccount(models.Model):
    logged_in_users_id = models.IntegerField()
    date = models.TextField()
    purpose = models.TextField()
    amount = models.FloatField()
    sync_flag = models.IntegerField(default=1)
    
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.group

class GroupFees(models.Model):
    member = models.ForeignKey(GroupMembers, on_delete=models.CASCADE)
    group_id = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    registration_fee = models.FloatField()
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return self.member

class CycleMeeting(models.Model):
    date = models.TextField()
    time = models.TextField()
    endTime = models.TextField()
    location = models.TextField()
    facilitator = models.TextField()
    meetingPurpose = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()
    objectives = models.TextField()
    attendanceData = models.TextField()
    representativeData = models.TextField()
    proposals = models.TextField()
    totalLoanFund = models.IntegerField()
    totalSocialFund = models.IntegerField()
    socialFundContributions = models.TextField()
    sharePurchases = models.TextField()
    sync_flag = models.IntegerField(default=1)
    
    group_id = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.group_id
    
class Meeting(models.Model):
    date = models.TextField()
    time = models.TextField()
    endTime = models.TextField()
    location = models.TextField()
    facilitator = models.TextField()
    meetingPurpose = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()
    objectives = models.TextField()
    attendanceData = models.TextField()
    representativeData = models.TextField()
    proposals = models.TextField()
    socialFundContributions = models.TextField()
    sharePurchases = models.TextField()
    totalLoanFund = models.IntegerField()
    totalSocialFund = models.IntegerField()
    sync_flag = models.IntegerField(default=1)
    
    group_id = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    cycle_id = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.group_id
    
    
class MemberShares(models.Model):
    logged_in_users_id = models.IntegerField()
    date = models.TextField()
    sharePurchases = models.TextField()
    
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    cycle_id = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    cyclemeeting = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return self.group_id
    
class WelfareAccount(models.Model):
    logged_in_users_id = models.IntegerField()
    amount = models.FloatField()
    
    group_id = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    meeting_id = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    cycle_id = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return self.group_id

class ActiveCycleMeeting(models.Model):
    
    group_id = models.ForeignKey(GroupProfile, on_delete=models.CASCADE)
    cycleMeetingID = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return self.group_id

class Shares(models.Model):
    sharePurchases = models.TextField()
    
    meetingId = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    cycle_id = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    group_id = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return self.group_id


class Social(models.Model):
    socialFund = models.TextField()
    sync_flag = models.IntegerField(default=1)
    
    meetingId = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.meetingId

class GroupLink(models.Model):
    group_id = models.ForeignKey(GroupProfile, on_delete=models.CASCADE)
    group_name = models.TextField()
    group_image_path = models.TextField()
    sync_flag = models.IntegerField(default=1)
    constitution = models.ForeignKey(ConstitutionTable, on_delete=models.CASCADE)
    cycle_schedule = models.ForeignKey(CycleSchedules, on_delete=models.CASCADE)
    group_members = models.ForeignKey(GroupMembers, on_delete=models.CASCADE)
    assigned_positions = models.ForeignKey(AssignedPositions, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.group_name

class LoanApplications(models.Model):
    group_id = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    cycle_id = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    meeting_id = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    submission_date = models.TextField()
    loan_applicant = models.TextField()
    group_member = models.ForeignKey(GroupMembers, on_delete=models.CASCADE)
    amount_needed = models.FloatField()
    loan_purpose = models.TextField()
    repayment_date = models.TextField()
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return self.group_id


class SocialFundApplications(models.Model):
    group_id = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    cycle_id = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    meeting_id = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    submission_date = models.TextField()
    applicant = models.TextField()
    group_member = models.ForeignKey(GroupMembers, on_delete=models.CASCADE)
    amount_needed = models.FloatField()
    social_purpose = models.TextField()
    repayment_date = models.TextField()
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return self.group_id


class CycleStartMeeting(models.Model):
    date = models.TextField()
    time = models.TextField()
    location = models.TextField()
    facilitator = models.TextField()
    meeting_purpose = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()
    objectives = models.TextField()
    attendance_data = models.TextField()
    representative_data = models.TextField()
    proposals = models.TextField()
    end_time = models.TextField()
    assigned_funds = models.TextField()
    social_fund_bag = models.TextField()
    social_fund_contributions = models.TextField()
    share_purchases = models.TextField()
    sync_flag = models.IntegerField(default=1)


class PaymentInfo(models.Model):
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    cycle_id = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    meeting_id = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    meeting_id = models.ForeignKey(GroupMembers, on_delete=models.CASCADE)
    payment_amount = models.FloatField()
    payment_date = models.TextField()
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return self.group
    

class Fines(models.Model):
    memberId = models.ForeignKey(GroupMembers, on_delete=models.CASCADE)
    amount = models.IntegerField()
    reason = models.TextField()
    groupId = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    cycleId = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    meetingId = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    savingsAccountId = models.ForeignKey(SavingsAccount, on_delete=models.CASCADE)
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return self.groupId


class GroupCycleStatus(models.Model):
    group = models.ForeignKey(GroupProfile, on_delete=models.CASCADE)
    cycleId = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    is_cycle_started = models.BooleanField(default=False)
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return self.group

class Loans(models.Model):
    member = models.ForeignKey(GroupMembers, on_delete=models.CASCADE)
    loan_applicant = models.TextField()
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    loan_purpose = models.TextField()
    loan_amount = models.FloatField()
    interest_rate = models.FloatField()
    start_date = models.TextField()
    end_date = models.TextField()
    status = models.TextField()
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return self.group


class LoanDisbursement(models.Model):
    member = models.ForeignKey(GroupMembers, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    cycleId = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    loan = models.ForeignKey(Loans, on_delete=models.CASCADE)
    disbursement_amount = models.FloatField()
    disbursement_date = models.DateField()
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return self.group


class LoanPayments(models.Model):
    member = models.ForeignKey(GroupMembers, on_delete=models.CASCADE)
    group = models.ForeignKey(GroupForm, on_delete=models.CASCADE)
    loan = models.ForeignKey(Loans, on_delete=models.CASCADE)
    payment_amount = models.FloatField()
    payment_date = models.TextField()
    sync_flag = models.IntegerField(default=1)
    def __str__(self):
        return self.group


class ShareOut(models.Model):
    group = models.ForeignKey(GroupProfile, on_delete=models.CASCADE)
    cycleId = models.ForeignKey(CycleMeeting, on_delete=models.CASCADE)
    users = models.ForeignKey(Users, on_delete=models.CASCADE)
    share_value = models.FloatField()
    sync_flag = models.IntegerField(default=1)
    def __str__(self):
        return self.group


class ReversedTransactions(models.Model):
    group = models.ForeignKey(GroupProfile, on_delete=models.CASCADE)
    savings_account = models.ForeignKey(SavingsAccount, on_delete=models.CASCADE)
    logged_in_users = models.ForeignKey(Users, on_delete=models.CASCADE)
    reversed_amount = models.FloatField()
    date = models.TextField()
    purpose = models.TextField()
    reversed_data = models.TextField()
    sync_flag = models.IntegerField(default=1)
    
    def __str__(self):
        return self.group
