from django.views.generic import ListView, UpdateView, CreateView
import forms
from directory import models
from models import BizPost
from extra_views import InlineFormSetView
# Create your views here.

class BulletinPost(CreateView):
    form_class = forms.BulletinPostForm
    template_name = 'management_general.html'
    model = BizPost

    def form_valid(self, form):
        user = self.request.user
        manager = user.manager
        post = form.instance
        post.save()
        manager.biz_posts.add(post)
        manager.save()
        return super(BulletinPost, self).form_valid(form)

    def get_success_url(self):
        return self.request.POST['next']

class ManagementPageMixin(object):
    model = models.Location
    success_url = "?message=Information successfully altered."
    form_title = None
    form_description = None

    def get_object(self, queryset=None):
        user = self.request.user
        manager = user.manager
        return models.Location.objects.get(manager=manager)

    def get_context_data(self, **kwargs):
        cd = super(ManagementPageMixin, self).get_context_data(**kwargs)
        cd['message'] = self.request.GET['message'] if self.request.GET.has_key("message") else None
        cd['manager'] = manager = self.request.user.manager
        cd['form_title'] = self.form_title
        cd['form_description'] = self.form_description
        cd['bulletin_form'] = forms.BulletinPostForm()
        return cd

class SpecialsManagementPage(ManagementPageMixin, InlineFormSetView):
    template_name = 'management_specials.html'
    inline_model = models.LocationSpecial
    form_class = forms.LocationSpecialForm
    form_title = "Daily Specials"
    form_description = "Here you can define the food and" \
                       " drink specials"
    max_num = 16
    extra = 5

class HoursManagementPage(ManagementPageMixin, InlineFormSetView):
    template_name = 'management_hours.html'
    form_class = forms.LocationHourForm
    form_title = "Hours of Operation"
    form_description = "To mark a day as closed, set" \
                       " both the opening and" \
                       " closing times to midnight (i.e. 00:00:00)"
    inline_model = models.LocationHour
    max_num = 7

class HighlightsManagementPage(ManagementPageMixin, InlineFormSetView):
    form_title = "Location Highlights"
    form_description = "These are the miscellanious notes about your" \
                       " business that appear on the right hand side" \
                       " of your business' page on the directory."
    template_name = "management_highlights.html"
    inline_model = models.LocationHighlight
    max_num = 10
    extra = 3

class GeneralManagementPage(ManagementPageMixin, UpdateView):
    template_name = "management_general.html"
    form_class = forms.LocationGeneralForm
    form_title = "Basic Info"
    form_description = ""

class BulletinListView(ListView):
    queryset = BizPost.objects.all().order_by("-post_time")
    paginate_by = 20
    template_name = "bulletins.html"
