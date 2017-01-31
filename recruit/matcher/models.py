from django.core.urlresolvers import reverse

from django_extensions.db.fields import AutoSlugField
from django.db.models import *
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from smart_selects.db_fields import ChainedForeignKey,ChainedManyToManyField

TITLE_CODE_CHOICES = (
    ('CFVP', 'CFO/VP Finance'),
    ('CAAM', 'Controller/Accounting Manager'),
    ('ACCT', 'Accountant/Sr. Accountant'),
    ('FINM', 'Finance Manager/Director'),
    ('FINS', 'Financial Analyst'),
    ('COST', 'Cost Accountant'),
    ('TRSY', 'Treasury Positions'),
    ('ACPY', 'Accounts Payable'),
    ('AUDT', 'Audit/Audit Manager/Director'),
    ('TAXA', 'Tax Analyst/Senior'),
    ('TAXM', 'Tax Manager/Director/VP'),
    ('RCTR', 'Recruiter'),
    ('HRPR', 'Human Resources/Payroll'),
)

STAGE_CHOICES = (
    ('MTCH', 'Matched to Job'),
    ('SBMT', 'Submitted to Client'),
    ('RINT', 'Interview Requested'),
    ('INTP', 'In Interview Process'),
    ('OFFR', 'Offer Made'),
    ('PLCD', 'Placement Made'),
    ('DCLN', 'Candidate Declined'),
    ('NSFO', 'No Start/Falloff'),
)

INTERVIEW_TYPE_CHOICES = (
    ('INP', 'In Person'),
    ('TEL', 'Telephone'),
    ('FTS', 'FaceTime/Skype'),
)

PREFIX_CHOICES = (
    ('MR.', 'Mr.'),
    ('MS.', 'Ms.'),
    ('DR.', 'Dr.'),
    )

class Company(models.Model):

    # Fields
    company_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    main_number = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    zip_code = models.IntegerField(default=0)
    description = models.TextField(max_length=1000)
    industry = models.CharField(max_length=100)
    size = models.CharField(max_length=30)
    website = models.URLField()
    linkedin_profile = models.URLField()

    def __str__(self):
        coname = str(self.company_name)
        return coname

    def get_absolute_url(self):
    	return reverse('matcher:companydetail', args=(self.pk,))

    class Meta:
    	verbose_name_plural = "companies"

class Person(models.Model):
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    salary = models.PositiveIntegerField(default=0)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    prefix = models.CharField(max_length=12, blank=True, choices=PREFIX_CHOICES)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30,blank=True)
    suffix = models.CharField(max_length=30,blank=True)
    nickname = models.CharField(max_length=30,blank=True)
    title = models.CharField(max_length=100)#JOB TITLE SO WE SHOULD ADD A PREFIX LIKE MR MS DR ETC
    title_code = models.CharField(max_length=4, choices=TITLE_CODE_CHOICES)
    linkedin_profile = models.URLField(blank=True)

    # Relationship Fields
    current_employer = models.ForeignKey('Company', on_delete=models.CASCADE)

    class Meta:
    	verbose_name_plural = "people"

    def get_absolute_url(self):
    	return reverse('matcher:persondetail', args=(self.pk,))
    	  
    def __str__(self):
    	personname = str(self.first_name+" "+self.last_name)#change this to a conditional that takes care of all name fields
    	return personname



class Position(models.Model):
    # Fields
    job_title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    
    position_id = models.CharField(max_length=255)#this should autoincrement looking at the max in the field and +=1
    title_code = models.CharField(max_length=30, choices=TITLE_CODE_CHOICES)
    
#    position_adress = models.CharField(max_length=50)
    city = models.CharField(max_length=50)#refactor this to position_city 
    position_zip = models.IntegerField(default=0)

    salary_lower = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    salary_upper = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)

    job_description = models.TextField(max_length=10000)
    ext_description = models.TextField(max_length=10000, blank=True)  
#these need to be taken care of by DEFs
    telephone_count = models.IntegerField(default=0)#telephone should be a type of interview, shouldnt it?
    in_person_count = models.IntegerField(default=0)#changing this to total interviews
    presentation_count = models.IntegerField(default=0)#isnt this just the total Matches?
    resume_count = models.IntegerField(default=0)#establlish which measures client submittal and which is just a match
    offer_made_count = models.IntegerField(default=0)

    notes = models.TextField(max_length=1000)
    benefits = models.TextField(max_length=100)
    social_linkedin = models.URLField(blank=True)
    fee = models.IntegerField(default=0)

 

    # Relationship Fields
    company = models.ForeignKey('Company', on_delete=models.CASCADE)
    contact_name = ChainedForeignKey(
        "Person",
        chained_field="company",#The chained_field indicates the field on the same model that should be chained to.
        chained_model_field="current_employer",#The chained_model_field indicates the field of the chained model that corresponds to the model linked to by the chained_field
        #show_all=False,#show_all indicates if only the filtered results should be shown or if you also want to display the other results further down.
        #auto_choose=False,#auto_choose indicates if auto select the choice when there is only one available choice.
        #sort=True
        )
    #make this a picker for the company names AND MAKE IT MANY TO ONE so there can be multiple contact names


    def __str__(self):
    	full_name = str(self.job_title)
    	return full_name

    def get_absolute_url(self):
    	return reverse('matcher:positiondetail', args=(self.pk,))

    def get_interview_count(self):
        intcount = 0
        for match in self.match_set.all():
            for interview in match.interview_set.all():
                intcount += 1
        self.in_person_count = intcount
        self.save()
        return intcount

    def get_match_count(self):
        mtchcount = 0
        for match in self.match_set.all():
            mtchcount += 1
        self.presentation_count = mtchcount
        self.save()
        return mtchcount

class Match(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    
    stage_in_process = models.CharField(max_length=4, choices=STAGE_CHOICES)
    notes = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    # Relationship Fields
    candidate = models.ForeignKey('Person')
    position = models.ForeignKey('Position')

    def company(self):
    	it = str(self.position.company.company_name)
    	return it

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('matcher:matchdetail', args=(self.pk,))

    def __str__(self):
    	printname = str(self.candidate)+" for "+str(self.position)+" at "+str(self.position.company)
    	return printname

    def get_update_url(self):
        return reverse('match_update', args=(self.slug,))

    class Meta:
    	verbose_name_plural = "matches"

    #make a def for setting match.active to False if the Position it is associated with is closed


class Interview(models.Model):

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    scheduled_time = models.DateTimeField(blank=True)
    candidate_feedback = models.TextField(max_length=255, blank=True)
    client_feedback = models.TextField(max_length=255, blank=True)
    interview_type = models.CharField(max_length=3, choices=INTERVIEW_TYPE_CHOICES)

    # Relationship Fields
    match = models.ForeignKey('Match')
    interview_with = ChainedManyToManyField(
        'Person',
        chained_field="match",
        chained_model_field="company",
        )

    class Meta:
        ordering = ('-scheduled_time',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('matcher:interviewdetail', args=(self.pk,))

    def get_update_url(self):
        return reverse('Matcher_interview_update', args=(self.slug,))

    def __str__(self):
    	longone=str(self.match.candidate.first_name)+" "+str(self.match.candidate.last_name)+" for "+str(self.match.position.job_title)
    	return longone


