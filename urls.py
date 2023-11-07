from django.urls import path, include
from digi_save_vsla_api.views.active_cycle_meeting_views import active_cycle_meeting_detail, active_cycle_meeting_list
from digi_save_vsla_api.views.assigned_positions_views import assigned_positions_detail, assigned_positions_list
from digi_save_vsla_api.views.constitution_table_views import constitution_table_detail, constitution_table_list
from digi_save_vsla_api.views.cycle_meeting_views import cycle_meeting_detail, cycle_meeting_list
from digi_save_vsla_api.views.cycle_schedules_views import cycle_schedules_detail, cycle_schedules_list
from digi_save_vsla_api.views.cycle_start_meeting_views import cycle_start_meeting_detail, cycle_start_meeting_list
from digi_save_vsla_api.views.fines_views import fines_detail, fines_list
from digi_save_vsla_api.views.group_cycle_status_views import group_cycle_status_detail, group_cycle_status_list
from digi_save_vsla_api.views.group_fees_views import group_fees_detail, group_fees_list
from digi_save_vsla_api.views.group_form_views import group_form_detail, group_form_list
from digi_save_vsla_api.views.group_link_views import group_link_detail, group_link_list
from digi_save_vsla_api.views.group_members_views import group_members_detail, group_members_list

from digi_save_vsla_api.views.group_profile_views import group_profile_detail, group_profile_list
from digi_save_vsla_api.views.loan_applications_views import loan_applications_detail, loan_applications_list
from digi_save_vsla_api.views.loan_disbursement_views import loan_disbursement_detail, loan_disbursement_list
from digi_save_vsla_api.views.loan_payments_views import loan_payments_detail, loan_payments_list
from digi_save_vsla_api.views.loans_views import loans_detail, loans_list
from digi_save_vsla_api.views.meeting_views import meeting_detail, meeting_list
from digi_save_vsla_api.views.member_shares_views import member_shares_detail, member_shares_list
from digi_save_vsla_api.views.payment_info_views import payment_info_detail, payment_info_list
from digi_save_vsla_api.views.positions_views import positions_detail, positions_list
from digi_save_vsla_api.views.reversed_transactions_views import reversed_transactions_detail, reversed_transactions_list
from digi_save_vsla_api.views.savings_account_views import savings_account_detail, savings_account_list
from digi_save_vsla_api.views.share_out_views import share_out_detail, share_out_list
from digi_save_vsla_api.views.shares_views import shares_detail, shares_list
from digi_save_vsla_api.views.social_fund_applications_views import social_fund_applications_detail, social_fund_applications_list
from digi_save_vsla_api.views.social_views import social_detail, social_list
from digi_save_vsla_api.views.users_views import users_detail, users_list
from digi_save_vsla_api.views.welfare_account_views import welfare_account_detail, welfare_account_list
from digi_save_vsla_api.views.auth_view import login_with_phone_code

urlpatterns = [
    # GroupProfile views
    path('group_profiles/', group_profile_list, name='group_profile_list'),
    path('group_profiles/<int:pk>/', group_profile_detail, name='group_profile_detail'),

    # ConstitutionTable views
    path('constitution_tables/', constitution_table_list, name='constitution_table_list'),
    path('constitution_tables/<int:pk>/', constitution_table_detail, name='constitution_table_detail'),

    # Users views
    path('users/', users_list, name='users_list'),
    path('users/<int:pk>/', users_detail, name='users_detail'),
    path('login-with-phone-code/', login_with_phone_code, name='login_with_phone_code'),

    # GroupMembers views
    path('group_members/', group_members_list, name='group_members_list'),
    path('group_members/<int:pk>/', group_members_detail, name='group_members_detail'),

    # CycleSchedules views
    path('cycle_schedules/', cycle_schedules_list, name='cycle_schedules_list'),
    path('cycle_schedules/<int:pk>/', cycle_schedules_detail, name='cycle_schedules_detail'),

    # Positions views
    path('positions/', positions_list, name='positions_list'),
    path('positions/<int:pk>/', positions_detail, name='positions_detail'),

    # AssignedPositions views
    path('assigned_positions/', assigned_positions_list, name='assigned_positions_list'),
    path('assigned_positions/<int:pk>/', assigned_positions_detail, name='assigned_positions_detail'),

    # GroupForm views
    path('group_forms/', group_form_list, name='group_form_list'),
    path('group_forms/<int:pk>/', group_form_detail, name='group_form_detail'),

    # SavingsAccount views
    path('savings_accounts/', savings_account_list, name='savings_account_list'),
    path('savings_accounts/<int:pk>/', savings_account_detail, name='savings_account_detail'),

    # GroupFees views
    path('group_fees/', group_fees_list, name='group_fees_list'),
    path('group_fees/<int:pk>/', group_fees_detail, name='group_fees_detail'),

    # CycleMeeting views
    path('cycle_meetings/', cycle_meeting_list, name='cycle_meeting_list'),
    path('cycle_meetings/<int:pk>/', cycle_meeting_detail, name='cycle_meeting_detail'),

    # Meeting views
    path('meetings/', meeting_list, name='meeting_list'),
    path('meetings/<int:pk>/', meeting_detail, name='meeting_detail'),

    # MemberShares views
    path('member_shares/', member_shares_list, name='member_shares_list'),
    path('member_shares/<int:pk>/', member_shares_detail, name='member_shares_detail'),

    # WelfareAccount views
    path('welfare_accounts/', welfare_account_list, name='welfare_account_list'),
    path('welfare_accounts/<int:pk>/', welfare_account_detail, name='welfare_account_detail'),

    # ActiveCycleMeeting views
    path('active_cycle_meetings/', active_cycle_meeting_list, name='active_cycle_meeting_list'),
    path('active_cycle_meetings/<int:pk>/', active_cycle_meeting_detail, name='active_cycle_meeting_detail'),

    # Shares views
    path('shares/', shares_list, name='shares_list'),
    path('shares/<int:pk>/', shares_detail, name='shares_detail'),

    # Social views
    path('social/', social_list, name='social_list'),
    path('social/<int:pk>/', social_detail, name='social_detail'),

    # GroupLink views
    path('group_links/', group_link_list, name='group_link_list'),
    path('group_links/<int:pk>/', group_link_detail, name='group_link_detail'),

    # LoanApplications views
    path('loan_applications/', loan_applications_list, name='loan_applications_list'),
    path('loan_applications/<int:pk>/', loan_applications_detail, name='loan_applications_detail'),

    # SocialFundApplications views
    path('social_fund_applications/', social_fund_applications_list, name='social_fund_applications_list'),
    path('social_fund_applications/<int:pk>/', social_fund_applications_detail, name='social_fund_applications_detail'),

    # # CycleStartMeeting views
    # path('cycle_start_meetings/', cycle_start_meeting_list, name='cycle_start_meeting_list'),
    # path('cycle_start_meetings/<int:pk>/', cycle_start_meeting_detail, name='cycle_start_meeting_detail'),

    # PaymentInfo views
    path('payment_info/', payment_info_list, name='payment_info_list'),
    path('payment_info/<int:pk>/', payment_info_detail, name='payment_info_detail'),

    # Fines views
    path('fines/', fines_list, name='fines_list'),
    path('fines/<int:pk>/', fines_detail, name='fines_detail'),

    # GroupCycleStatus views
    path('group_cycle_status/', group_cycle_status_list, name='group_cycle_status_list'),
    path('group_cycle_status/<int:pk>/', group_cycle_status_detail, name='group_cycle_status_detail'),

    # Loans views
    path('loans/', loans_list, name='loans_list'),
    path('loans/<int:pk>/', loans_detail, name='loans_detail'),

    # LoanDisbursement views
    path('loan_disbursements/', loan_disbursement_list, name='loan_disbursement_list'),
    path('loan_disbursements/<int:pk>/', loan_disbursement_detail, name='loan_disbursement_detail'),

    # LoanPayments views
    path('loan_payments/', loan_payments_list, name='loan_payments_list'),
    path('loan_payments/<int:pk>/', loan_payments_detail, name='loan_payments_detail'),

    # ShareOut views
    path('share_out/', share_out_list, name='share_out_list'),
    path('share_out/<int:pk>/', share_out_detail, name='share_out_detail'),

    # ReversedTransactions views
    path('reversed_transactions/', reversed_transactions_list, name='reversed_transactions_list'),
    path('reversed_transactions/<int:pk>/', reversed_transactions_detail, name='reversed_transactions_detail'),
]
