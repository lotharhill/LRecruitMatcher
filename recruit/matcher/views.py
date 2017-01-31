
from django.http import Http404
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect 
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from .models import Position, Person, Company, Match, Interview
from .forms import PersonForm, CompanyForm, PositionForm, MatchForm, InterviewForm
# Create your views here.

class PersonView(generic.DetailView):
	model = Person
	template_name = 'matcher/persondetail.html'

class PersonCreate(CreateView):
	model = Person
	form_class = PersonForm

	def form_valid(self, form):
		self.object = form.save()
		return HttpResponseRedirect(self.get_success_url())

class PersonUpdate(UpdateView):
	model = Person
	form_class = PersonForm

class PersonDelete(DeleteView):
	model = Person
	success_url = reverse_lazy('matcher:index')

class PeopleList(generic.ListView):
	template_name = 'matcher/people_list.html'

	def get_queryset(self):
		return Person.objects.all()

def index(request):
    latest_person_list = Person.objects.order_by('-last_updated')[:5]
    latest_company_list = Company.objects.order_by('-last_updated')[:5]
    latest_position_list = Position.objects.order_by('-last_updated')[:5]
    latest_match_list = Match.objects.order_by('-last_updated')[:5]
    latest_interview_list = Interview.objects.order_by('-scheduled_time')[:5]
    #end up with this filtering for recent before and future
    #template = loader.get_template('matcher/index.html')
    context = {
    	'latest_person_list': latest_person_list,
    	'latest_company_list': latest_company_list,
    	'latest_position_list': latest_position_list,
    	'latest_match_list': latest_match_list,
    	'latest_interview_list': latest_interview_list,
    }
    return render(request, 'matcher/index.html', context)


class CompanyDetail(generic.DetailView):
	model = Company
	template_name = 'matcher/companydetail.html'


class CompanyList(generic.ListView):
	model = Company

	def get_queryset(self):
		"""Return the last five published questions."""
		return Company.objects.order_by('-last_updated')

class CompanyCreate(CreateView):
	model = Company
	form_class = CompanyForm

class CompanyUpdate(UpdateView):
	model = Company
	form_class = CompanyForm

def positiondetail(request, position_id):
	#all of this is html button stuff
	if(request.POST.get('tel')):
		position = get_object_or_404(Position, pk=position_id)
		position.telephone_count += 1
		position.save()
		return HttpResponseRedirect(reverse('matcher:positiondetail', args=(position.id,)))
	elif(request.POST.get('res')):
		position = get_object_or_404(Position, pk=position_id)
		position.resume_count += 1
		position.save()
		return HttpResponseRedirect(reverse('matcher:positiondetail', args=(position.id,)))
	else:
		position = get_object_or_404(Position, pk=position_id)
		return render(request, 'matcher/positiondetail.html', {'position': position})

class PositionCreate(CreateView):
	model = Position
	form_class = PositionForm

class PositionList(generic.ListView):
	model = Position

class PositionUpdate(UpdateView):
	model = Position
	form_class = PositionForm

def matchdetail(request, match_id):
    match = get_object_or_404(Match, pk=match_id)
    return render(request, 'matcher/matchdetail.html', {'match': match})

class MatchCreate(CreateView):
	model = Match
	form_class = MatchForm

class MatchList(generic.ListView):
	model = Match
	form_class = MatchForm

class MatchUpdate(UpdateView):
	model = Match
	form_class = MatchForm

def interviewdetail(request, interview_id):
	interview = get_object_or_404(Interview, pk=interview_id)
	return render(request, 'matcher/interviewdetail.html', {'interview': interview})

class InterviewCreate(CreateView):
	model = Interview
	form_class = InterviewForm

