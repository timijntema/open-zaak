from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView

from vng_api_common.authorizations.models import Applicatie, Autorisatie

from .forms import (
    COMPONENT_TO_PREFIXES_MAP,
    AutorisatieFormSet,
    RelatedTypeSelectionMethods,
    VertrouwelijkheidsAanduiding,
    get_scope_choices,
)


class AutorisatiesView(DetailView):
    model = Applicatie
    template_name = "admin/autorisaties/applicatie_autorisaties.html"
    pk_url_kwarg = "object_id"
    # set these on the .as_viev(...) call
    admin_site = None
    model_admin = None

    # perform permission checks
    def dispatch(self, request, *args, **kwargs):
        assert self.admin_site
        assert self.model_admin

        applicatie = self.get_object()
        if not self.model_admin.has_change_permission(request, applicatie):
            raise PermissionDenied()

        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        import bpdb

        bpdb.set_trace()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(self.admin_site.each_context(self.request))
        context.update(
            {
                "opts": Applicatie._meta,
                "original": self.get_object(),
                "title": _("beheer autorisaties"),
                "is_popup": False,
                "formset": AutorisatieFormSet(),
                "scope_choices": get_scope_choices(),
                "COMPONENTS_TO_PREFIXES_MAP": COMPONENT_TO_PREFIXES_MAP,
                "RELATED_TYPE_SELECTION_METHODS": RelatedTypeSelectionMethods.choices,
                "VA_CHOICES": VertrouwelijkheidsAanduiding.choices,
            }
        )
        return context
