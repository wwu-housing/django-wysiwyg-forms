from django.conf import settings
from django.conf.urls.defaults import *

from django.views.generic.simple import direct_to_template

from .views import ApplyTransactions, Edit

urlpatterns = patterns(
    '',
    url(r"^save/$", ApplyTransactions, name="wysiwyg_forms_apply_transactions"),
    url(r"^$", Edit, name="wysiwyg_forms_new_form"),
    url(r"^(\d+)/$", Edit, name="wysiwyg_forms_edit_form")
)

if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r"^test/$",
            direct_to_template,
            { "template": "wysiwyg_forms/test.html" },
            name="wysiwyg_forms_test")
    )
