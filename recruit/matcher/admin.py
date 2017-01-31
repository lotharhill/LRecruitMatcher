from django.contrib import admin
from django import forms
from .models import Company, Person, Position, Match, Interview
from django.forms import TextInput, Textarea
from django.db import models

#COMPANY NOT LINKING TO VIEW ON SITE
class CompanyAdminForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = '__all__'

class CompanyAdmin(admin.ModelAdmin):
    fields = ['company_name', 'main_number', 'address', 'zip_code', 'description', 'industry', 'size', 'website', 'linkedin_profile']

admin.site.register(Company, CompanyAdmin)

#PERSON NOT LINKING OT VIEW ON SITE
class PersonAdminForm(forms.ModelForm):

    class Meta:
        model = Person
        fields = '__all__'

class PersonAdmin(admin.ModelAdmin):
    form = PersonAdminForm
    list_display = ['first_name', 'last_name', 'middle_name', 'title', 'suffix', 'nickname', 'created', 'last_updated', 'salary', 'phone', 'email', 'linkedin_profile']
    search_fields = ['last_name', 'first_name', 'middle_name', 'nickname']

admin.site.register(Person, PersonAdmin)

#POSITION IS NOT LINKING
class PositionAdminForm(forms.ModelForm):

    class Meta:
        model = Position
        fields = '__all__'

class MatchInLine(admin.TabularInline):
	model = Match

class PositionAdmin(admin.ModelAdmin):
    form = PositionAdminForm
    list_display = ['job_title', 'created', 'last_updated', 'position_zip', 'ext_description', 'position_id', 'title_code', 'city', 'salary_lower', 'salary_upper', 'job_description', 'telephone_count', 'in_person_count', 'notes', 'presentation_count', 'benefits', 'social_linkedin', 'resume_count', 'offer_made_count', 'fee']
    fieldsets = [
    	('Main Info', {'fields': ['job_title', 'fee', 'position_id', 'title_code']}),
    	('Location Info', {'fields': ['city', 'position_zip']}),
    	('Position Details', {'fields': ['job_description', 'description']}),
    ]
    inlines = [MatchInLine]

admin.site.register(Position, PositionAdmin)


#interview is correctly linking to VIEW ON SITE
class InterviewInline(admin.TabularInline):
    model = Interview
    extra = 1
    fieldsets = [
    	(None, {'fields': ['scheduled_time', 'candidate_feedback', 'client_feedback']}),
    	('Blablah', {'fields': ['interview_with']})
    ]
    formfield_overrides = {
    	models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

#MATCH IS correctly linking to viewonsite
class MatchAdminForm(forms.ModelForm):

    class Meta:
        model = Match
        fields = '__all__'

class MatchAdmin(admin.ModelAdmin):
    form = MatchAdminForm
    fieldsets = [
    	(None, {'fields': ['candidate', 'position', 'notes', 'stage_in_process']}),
    ]
    inlines = [InterviewInline]
    formfield_overrides = {
    	models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

admin.site.register(Match, MatchAdmin)

class InterviewAdmin(admin.ModelAdmin):
	model = Interview
	formfield_overrides = {
		models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':60})},
	}

admin.site.register(Interview, InterviewAdmin)