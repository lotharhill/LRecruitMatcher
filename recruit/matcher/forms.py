from django import forms
from .models import Person, Company, Position, Match, Interview
from crispy_forms.bootstrap import InlineField
from crispy_forms.helper import FormHelper


class PersonForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = [
        'prefix',
        'first_name',
        'middle_name',
        'last_name',
        'suffix',
        'nickname',
        'title',
        'title_code',
        'current_employer',
        'phone',
        'email',
        'salary',
        'linkedin_profile']


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
        'company_name', 
        'main_number', 
        'address', 
        'zip_code', 
        'description', 
        'industry', 
        'size', 
        'website', 
        'linkedin_profile'
        ]


class PositionForm(forms.ModelForm):
    city = forms.CharField(
        initial = 'default value'
    )
    class Meta:
        model = Position
        fields = [
        'job_title', 
        'company', 
		'city', 
        'position_zip', 
        'contact_name',
        'title_code', 
        'salary_lower', 
        'salary_upper',
        'fee', 
        'position_id',
        'benefits',
        'notes', 
        'job_description', 
        'ext_description', 
        ]


class MatchForm(forms.ModelForm):

    class Meta:
        model = Match
        fields = ['stage_in_process', 'candidate', 'position', 'notes', 'is_active']


class InterviewForm(forms.ModelForm):
    class Meta:
        model = Interview
        fields = ['scheduled_time', 'candidate_feedback', 'client_feedback', 'match', 'interview_with']
