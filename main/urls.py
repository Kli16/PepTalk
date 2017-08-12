from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', views.index, name= 'index'),
    url(r'^About/$', views.index, name= 'index'),
    url(r'^mentee_signup/$', views.mentee_signup, name='mentee_signup'),
    url(r'^mentor_signup/$', views.mentor_signup, name='mentor_signup'),
    url(r'^mentee/$', views.mentee, name='mentee'),
    url(r'^mentor/$', views.mentor, name='mentor'),
    url(r'^Mentees/$', views.mentees_about, name='mentees_about'),
    url(r'^Mentors/$', views.mentors_about, name='mentors_about'),
    url(r'^Contact/$', views.contact, name='Contact'),
    url(r'login_success/$', views.login_success, name='login_success'),
    url(r'^mentor_profile/logout/$', RedirectView.as_view(url='/logout/')),
    url(r'^mentor_profile/$', views.mentor_profile, name='mentor_profile'),
    url(r'^mentor_profile/edit/$', views.edit_mentor_profile, name='edit_mentor_profile'),
    url(r'^mentor_profile/generalcontact/$', RedirectView.as_view(url='/generalcontact/')),
    url(r'^mentor_profile/drills/$', RedirectView.as_view(url='/drills/')),
    url(r'^mentor_profile/prepsharing/$', RedirectView.as_view(url='/prepsharing/')),
    url(r'^mentor_profile/tournament/$', RedirectView.as_view(url='/tournament/')),
    url(r'^mentor_profile/mentee_profile/$', RedirectView.as_view(url='/mentee_profile/')),
    url(r'^mentor/$', RedirectView.as_view(url='/prepsharing/')),
    url(r'^mentor_profile/(?P<username>[a-zA-Z0-9]+)/$', views.get_mentor_profile, name='mentor_profile'),
    url(r'^mentee_profile/logout/$', RedirectView.as_view(url='/logout/')),
    url(r'^logout/$', RedirectView.as_view(url='/About/')),
    url(r'^mentee_profile/$', views.mentee_profile, name='mentee_profile'),
    url(r'^generalcontact/$', views.generalcontact, name='generalcontact'),
    url(r'^prepsharing/$', views.prepsharing, name='prepsharing'),
    url(r'^drills/$', views.drills, name='drills'),
    url(r'^tournament/$', views.tournament, name='tournament'),
    url(r'^mentorsubmission/$', views.submitted, name='submitted'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
