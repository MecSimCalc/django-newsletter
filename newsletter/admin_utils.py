from functools import update_wrapper

from django.contrib.admin.utils import unquote
from django.http import Http404
from django.utils.encoding import force_str
from django.utils.translation import gettext as _
from .models import Subscription
from django.contrib.auth import get_user_model


class ExtendibleModelAdminMixin:
    def _getobj(self, request, object_id):
        opts = self.model._meta

        try:
            obj = self.get_queryset(request).get(pk=unquote(object_id))
        except self.model.DoesNotExist:
            # Don't raise Http404 just yet, because we haven't checked
            # permissions yet. We don't want an unauthenticated user to
            # be able to determine whether a given object exists.
            obj = None

        if obj is None:
            raise Http404(
                _("%(name)s object with primary key " "'%(key)s' does not exist.")
                % {"name": force_str(opts.verbose_name), "key": force_str(object_id)}
            )

        return obj

    def _wrap(self, view):
        def wrapper(*args, **kwargs):
            return self.admin_site.admin_view(view)(*args, **kwargs)

        return update_wrapper(wrapper, view)

    def _view_name(self, name):
        info = self.model._meta.app_label, self.model._meta.model_name, name

        return "%s_%s_%s" % info


def make_subscription(newsletter, email, name=None):
    addr = Subscription(subscribed=True)
    addr.newsletter = newsletter

    user = get_user_model().objects.filter(email=email).first()
    if user:
        addr.user = user
    else:
        addr.email_field = email
        if name:
            addr.name_field = name

    return addr
