from django.contrib.admin import AdminSite
from django.templatetags.static import static
from django.utils.html import format_html


class LazzatAdminSite(AdminSite):
    site_header = "🍴 Lazzat Restaurant"
    site_title = "Lazzat Restaurant Admin"
    index_title = "Boshqaruv Paneli"

    def each_context(self, request):
        context = super().each_context(request)
        return context
