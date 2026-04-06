from django.contrib.admin import AdminSite
from django.templatetags.static import static
from django.utils.html import format_html


class DasturxonAdminSite(AdminSite):
    site_header = "🍴 Dasturxon"
    site_title = "Dasturxon Admin"
    index_title = "Boshqaruv Paneli"

    def each_context(self, request):
        context = super().each_context(request)
        return context
