# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from django.conf.urls import url

from .util import page
from . import views
from bedrock.redirects.util import redirect


urlpatterns = (
    url('^$', views.home, name='mozorg.home'),
    page('about', 'mozorg/about.html'),
    page('about/manifesto', 'mozorg/about/manifesto.html'),
    page('about/manifesto/details', 'mozorg/about/manifesto-details.html'),
    page('about/leadership', 'mozorg/about/leadership.html'),
    page('about/policy/lean-data', 'mozorg/about/policy/lean-data.html'),
    page('about/policy/patents', 'mozorg/about/policy/patents/index.html'),
    page('about/policy/patents/license', 'mozorg/about/policy/patents/license.html'),
    page('about/policy/patents/license/1.0', 'mozorg/about/policy/patents/license-1.0.html'),
    page('about/policy/patents/guide', 'mozorg/about/policy/patents/guide.html'),
    page('book', 'mozorg/book.html'),
    url('^credits/$', views.credits_view, name='mozorg.credits'),
    page('credits/faq', 'mozorg/credits-faq.html'),
    page('developer/browsertest', 'mozorg/browser-test.html'),
    url('^about/partnerships/$', views.partnerships, name='mozorg.partnerships'),
    page('about/partnerships/distribution', 'mozorg/partnerships-distribution.html'),
    page('about/history', 'mozorg/about/history.html'),
    page('about/history/details', 'mozorg/about/history-details.html'),
    page('about/mozilla-based', 'mozorg/projects/mozilla-based.html'),
    page('projects/calendar', 'mozorg/projects/calendar.html'),
    url('^projects/calendar/holidays/$', views.holiday_calendars,
        name='mozorg.projects.holiday_calendars'),
    # Bug 981063, catch all for old calendar urls.
    # must be here to avoid overriding the above
    redirect(r'^projects/calendar/', 'mozorg.projects.calendar', locale_prefix=False),
    page('mission', 'mozorg/mission.html'),
    page('ITU', 'mozorg/itu.html'),
    page('about/powered-by', 'mozorg/powered-by.html'),
    url('^about/forums/$', views.forums_view, name='mozorg.about.forums.forums'),
    page('about/forums/etiquette', 'mozorg/about/forums/etiquette.html'),
    page('about/forums/cancellation', 'mozorg/about/forums/cancellation.html'),
    page('about/governance', 'mozorg/about/governance/governance.html'),
    page('about/governance/roles', 'mozorg/about/governance/roles.html'),
    page('about/governance/policies', 'mozorg/about/governance/policies/policies.html'),
    page('about/governance/policies/commit', 'mozorg/about/governance/policies/commit.html'),
    page('about/governance/policies/commit/access-policy', 'mozorg/about/governance/policies/commit/access-policy.html'),
    page('about/governance/policies/commit/requirements', 'mozorg/about/governance/policies/commit/requirements.html'),
    page('about/governance/policies/security-group/bugs', 'mozorg/about/governance/policies/security/bugs.html'),
    page('about/governance/policies/security-group/tld-idn', 'mozorg/about/governance/policies/security/tld-idn.html'),
    page('about/governance/policies/security-group/membership', 'mozorg/about/governance/policies/security/membership.html'),
    page('about/governance/policies/security-group/certs', 'mozorg/about/governance/policies/security/certs/index.html'),
    page('about/governance/policies/security-group/certs/policy', 'mozorg/about/governance/policies/security/certs/policy.html'),
    page('about/governance/policies/security/plugin-whitelist-policy', 'mozorg/about/governance/policies/security/plugin-whitelist-policy.html'),
    page('about/governance/organizations', 'mozorg/about/governance/organizations.html'),
    page('about/governance/policies/participation',
         'mozorg/about/governance/policies/participation.html'),
    page('about/governance/policies/module-ownership',
         'mozorg/about/governance/policies/module-ownership.html'),
    page('about/governance/policies/regressions',
         'mozorg/about/governance/policies/regressions.html'),
    page('about/governance/policies/reviewers', 'mozorg/about/governance/policies/reviewers.html'),

    page('about/policy/transparency', 'mozorg/about/policy/transparency/index.html'),
    page('about/policy/transparency/jan-dec-2015',
         'mozorg/about/policy/transparency/jan-dec-2015.html'),
    page('about/policy/transparency/jan-jun-2016',
         'mozorg/about/policy/transparency/jan-jun-2016.html'),

    page('contact', 'mozorg/contact/contact-landing.html'),
    page('contact/spaces', 'mozorg/contact/spaces/spaces-landing.html'),
    page('contact/spaces/mountain-view', 'mozorg/contact/spaces/mountain-view.html'),
    page('contact/spaces/auckland', 'mozorg/contact/spaces/auckland.html'),
    page('contact/spaces/beijing', 'mozorg/contact/spaces/beijing.html'),
    page('contact/spaces/berlin', 'mozorg/contact/spaces/berlin.html'),
    page('contact/spaces/london', 'mozorg/contact/spaces/london.html'),
    page('contact/spaces/paris', 'mozorg/contact/spaces/paris.html'),
    page('contact/spaces/portland', 'mozorg/contact/spaces/portland.html'),
    page('contact/spaces/san-francisco', 'mozorg/contact/spaces/san-francisco.html'),
    page('contact/spaces/taipei', 'mozorg/contact/spaces/taipei.html'),
    page('contact/spaces/tokyo', 'mozorg/contact/spaces/tokyo.html'),
    page('contact/spaces/toronto', 'mozorg/contact/spaces/toronto.html'),
    page('contact/spaces/vancouver', 'mozorg/contact/spaces/vancouver.html'),

    page('contact/communities', 'mozorg/contact/communities/communities-landing.html'),
    page('contact/communities/north-america', 'mozorg/contact/communities/north-america.html'),
    page('contact/communities/latin-america', 'mozorg/contact/communities/latin-america.html'),
    page('contact/communities/europe', 'mozorg/contact/communities/europe.html'),
    page('contact/communities/asia-south-pacific',
         'mozorg/contact/communities/asia-south-pacific.html'),
    page('contact/communities/antarctica', 'mozorg/contact/communities/antarctica.html'),
    page('contact/communities/africa-middle-east',
         'mozorg/contact/communities/africa-middle-east.html'),
    page('contact/communities/arabic', 'mozorg/contact/communities/arabic.html'),
    page('contact/communities/hispano', 'mozorg/contact/communities/hispano.html'),
    page('contact/communities/francophone', 'mozorg/contact/communities/francophone.html'),

    page('contact/communities/canada', 'mozorg/contact/communities/canada.html'),
    page('contact/communities/united-states', 'mozorg/contact/communities/united-states.html'),
    page('contact/communities/argentina', 'mozorg/contact/communities/argentina.html'),
    page('contact/communities/bolivia', 'mozorg/contact/communities/bolivia.html'),
    page('contact/communities/brazil', 'mozorg/contact/communities/brazil.html'),
    page('contact/communities/chile', 'mozorg/contact/communities/chile.html'),
    page('contact/communities/colombia', 'mozorg/contact/communities/colombia.html'),
    page('contact/communities/costa-rica', 'mozorg/contact/communities/costa-rica.html'),
    page('contact/communities/cuba', 'mozorg/contact/communities/cuba.html'),
    page('contact/communities/ecuador', 'mozorg/contact/communities/ecuador.html'),
    page('contact/communities/mexico', 'mozorg/contact/communities/mexico.html'),
    page('contact/communities/nicaragua', 'mozorg/contact/communities/nicaragua.html'),
    page('contact/communities/paraguay', 'mozorg/contact/communities/paraguay.html'),
    page('contact/communities/peru', 'mozorg/contact/communities/peru.html'),
    page('contact/communities/uruguay', 'mozorg/contact/communities/uruguay.html'),
    page('contact/communities/venezuela', 'mozorg/contact/communities/venezuela.html'),

    page('contact/communities/albania', 'mozorg/contact/communities/albania.html'),
    page('contact/communities/armenia', 'mozorg/contact/communities/armenia.html'),
    page('contact/communities/austria', 'mozorg/contact/communities/austria.html'),
    page('contact/communities/balkans', 'mozorg/contact/communities/balkans.html'),
    page('contact/communities/basque', 'mozorg/contact/communities/basque.html'),
    page('contact/communities/belgium', 'mozorg/contact/communities/belgium.html'),
    page('contact/communities/bosnia-and-herzegovina',
         'mozorg/contact/communities/bosnia-and-herzegovina.html'),
    page('contact/communities/bulgaria', 'mozorg/contact/communities/bulgaria.html'),
    page('contact/communities/catalan', 'mozorg/contact/communities/catalan.html'),
    page('contact/communities/croatia', 'mozorg/contact/communities/croatia.html'),
    page('contact/communities/czech-republic', 'mozorg/contact/communities/czech-republic.html'),
    page('contact/communities/denmark', 'mozorg/contact/communities/denmark.html'),
    page('contact/communities/estonia', 'mozorg/contact/communities/estonia.html'),
    page('contact/communities/finland', 'mozorg/contact/communities/finland.html'),
    page('contact/communities/france', 'mozorg/contact/communities/france.html'),
    page('contact/communities/germany', 'mozorg/contact/communities/germany.html'),
    page('contact/communities/greece', 'mozorg/contact/communities/greece.html'),
    page('contact/communities/hungary', 'mozorg/contact/communities/hungary.html'),
    page('contact/communities/ireland', 'mozorg/contact/communities/ireland.html'),
    page('contact/communities/italy', 'mozorg/contact/communities/italy.html'),
    page('contact/communities/kosovo', 'mozorg/contact/communities/kosovo.html'),
    page('contact/communities/lithuania', 'mozorg/contact/communities/lithuania.html'),
    page('contact/communities/norway', 'mozorg/contact/communities/norway.html'),
    page('contact/communities/poland', 'mozorg/contact/communities/poland.html'),
    page('contact/communities/portugal', 'mozorg/contact/communities/portugal.html'),
    page('contact/communities/macedonia', 'mozorg/contact/communities/macedonia.html'),
    page('contact/communities/montenegro', 'mozorg/contact/communities/montenegro.html'),
    page('contact/communities/romania', 'mozorg/contact/communities/romania.html'),
    page('contact/communities/russia', 'mozorg/contact/communities/russia.html'),
    page('contact/communities/serbia', 'mozorg/contact/communities/serbia.html'),
    page('contact/communities/slovakia', 'mozorg/contact/communities/slovakia.html'),
    page('contact/communities/slovenia', 'mozorg/contact/communities/slovenia.html'),
    page('contact/communities/spain', 'mozorg/contact/communities/spain.html'),
    page('contact/communities/sweden', 'mozorg/contact/communities/sweden.html'),
    page('contact/communities/switzerland', 'mozorg/contact/communities/switzerland.html'),
    page('contact/communities/the-netherlands', 'mozorg/contact/communities/the-netherlands.html'),
    page('contact/communities/turkey', 'mozorg/contact/communities/turkey.html'),
    page('contact/communities/ukraine', 'mozorg/contact/communities/ukraine.html'),
    page('contact/communities/united-kingdom', 'mozorg/contact/communities/united-kingdom.html'),

    page('contact/communities/australia', 'mozorg/contact/communities/australia.html'),
    page('contact/communities/bangladesh', 'mozorg/contact/communities/bangladesh.html'),
    page('contact/communities/cambodia', 'mozorg/contact/communities/cambodia.html'),
    page('contact/communities/china', 'mozorg/contact/communities/china.html'),
    page('contact/communities/hong-kong', 'mozorg/contact/communities/hong-kong.html'),
    page('contact/communities/india', 'mozorg/contact/communities/india.html'),
    page('contact/communities/indonesia', 'mozorg/contact/communities/indonesia.html'),
    page('contact/communities/japan', 'mozorg/contact/communities/japan.html'),
    page('contact/communities/kerala', 'mozorg/contact/communities/kerala.html'),
    page('contact/communities/malaysia', 'mozorg/contact/communities/malaysia.html'),
    page('contact/communities/myanmar', 'mozorg/contact/communities/myanmar.html'),
    page('contact/communities/nepal', 'mozorg/contact/communities/nepal.html'),
    page('contact/communities/pakistan', 'mozorg/contact/communities/pakistan.html'),
    page('contact/communities/philippines', 'mozorg/contact/communities/philippines.html'),
    page('contact/communities/singapore', 'mozorg/contact/communities/singapore.html'),
    page('contact/communities/south-korea', 'mozorg/contact/communities/south-korea.html'),
    page('contact/communities/sri-lanka', 'mozorg/contact/communities/sri-lanka.html'),
    page('contact/communities/taiwan', 'mozorg/contact/communities/taiwan.html'),
    page('contact/communities/thailand', 'mozorg/contact/communities/thailand.html'),
    page('contact/communities/vietnam', 'mozorg/contact/communities/vietnam.html'),

    page('contact/communities/algeria', 'mozorg/contact/communities/algeria.html'),
    page('contact/communities/cameroon', 'mozorg/contact/communities/cameroon.html'),
    page('contact/communities/ivory-coast', 'mozorg/contact/communities/ivory-coast.html'),
    page('contact/communities/egypt', 'mozorg/contact/communities/egypt.html'),
    page('contact/communities/ghana', 'mozorg/contact/communities/ghana.html'),
    page('contact/communities/israel', 'mozorg/contact/communities/israel.html'),
    page('contact/communities/jordan', 'mozorg/contact/communities/jordan.html'),
    page('contact/communities/kenya', 'mozorg/contact/communities/kenya.html'),
    page('contact/communities/mauritius', 'mozorg/contact/communities/mauritius.html'),
    page('contact/communities/palestine', 'mozorg/contact/communities/palestine.html'),
    page('contact/communities/senegal', 'mozorg/contact/communities/senegal.html'),
    page('contact/communities/tunisia', 'mozorg/contact/communities/tunisia.html'),
    page('contact/communities/uganda', 'mozorg/contact/communities/uganda.html'),
    page('contact/communities/zimbabwe', 'mozorg/contact/communities/zimbabwe.html'),

    page('MPL', 'mozorg/mpl/index.html'),
    page('MPL/historical', 'mozorg/mpl/historical.html'),
    page('MPL/license-policy', 'mozorg/mpl/license-policy.html'),
    page('MPL/headers', 'mozorg/mpl/headers/index.html'),
    page('MPL/1.1', 'mozorg/mpl/1.1/index.html'),
    page('MPL/1.1/FAQ', 'mozorg/mpl/1.1/faq.html'),
    page('MPL/1.1/annotated', 'mozorg/mpl/1.1/annotated/index.html'),
    page('MPL/2.0', 'mozorg/mpl/2.0/index.html'),
    page('MPL/2.0/FAQ', 'mozorg/mpl/2.0/faq.html'),
    page('MPL/2.0/Revision-FAQ', 'mozorg/mpl/2.0/revision-faq.html'),
    page('MPL/2.0/combining-mpl-and-gpl', 'mozorg/mpl/2.0/combining-mpl-and-gpl.html'),
    page('MPL/2.0/differences', 'mozorg/mpl/2.0/differences.html'),
    page('MPL/2.0/permissive-code-into-mpl', 'mozorg/mpl/2.0/permissive-code-into-mpl.html'),

    page('contribute', 'mozorg/contribute/index.html'),
    url('^contribute/embed/$', views.contribute_embed,
        name='mozorg.contribute_embed'),
    page('contribute/events', 'mozorg/contribute/events.html'),
    url('^contribute/friends/$', views.contribute_friends, name='mozorg.contribute.friends'),
    page('contribute/signup', 'mozorg/contribute/signup.html'),
    page('contribute/stories', 'mozorg/contribute/stories.html'),
    page('contribute/stories/faye', 'mozorg/contribute/story-faye.html'),
    page('contribute/stories/michael', 'mozorg/contribute/story-michael.html'),
    page('contribute/stories/ruben', 'mozorg/contribute/story-ruben.html'),
    page('contribute/stories/shreyas', 'mozorg/contribute/story-shreyas.html'),
    url('^contribute/studentambassadors/$',
        views.contribute_studentambassadors_landing,
        name='mozorg.contribute.studentambassadors.landing'),
    url('^contribute/task/',
        views.ContributeTaskView.as_view(),
        name='mozorg.contribute.taskview'),
    url(r'^contributor-data/(?P<source_name>[a-z]{2,20})\.json$', views.mozid_data_view,
        name='mozorg.contributor-data'),
    url('^internet-health/$', views.internet_health, name='mozorg.internet-health'),
    page('internet-health/privacy-security', 'mozorg/internet-health/privacy-security.html'),
    page('internet-health/digital-inclusion', 'mozorg/internet-health/digital-inclusion.html'),
    page('moss', 'mozorg/moss/index.html'),
    page('moss/foundational-technology', 'mozorg/moss/foundational-technology.html'),
    page('moss/mission-partners', 'mozorg/moss/mission-partners.html'),
    page('moss/secure-open-source', 'mozorg/moss/secure-open-source.html'),
    page('plugincheck', 'mozorg/plugincheck.html'),
    url(r'^robots.txt$', views.Robots.as_view(), name='robots.txt'),
    url('^technology/$', views.technology, name='mozorg.technology'),
    page('developer/css-grid', 'mozorg/developer/css-grid-demo.html'),

    # namespaces
    url(r'^2004/em-rdf$', views.namespaces, {'namespace': 'em-rdf'}),
    url(r'^2005/app-update$', views.namespaces, {'namespace': 'update'}),
    url(r'^2006/addons-blocklist$', views.namespaces, {'namespace': 'addons-bl'}),
    url(r'^2006/browser/search/$', views.namespaces, {'namespace': 'mozsearch'}),
    url(r'^keymaster/gatekeeper/there\.is\.only\.xul$', views.namespaces, {'namespace': 'xul'}),
    url(r'^microsummaries/0\.1$', views.namespaces, {'namespace': 'microsummaries'}),
    url(r'^projects/xforms/2005/type$', views.namespaces, {'namespace': 'xforms-type'}),
    url(r'^xbl$', views.namespaces, {'namespace': 'xbl'}),
)
