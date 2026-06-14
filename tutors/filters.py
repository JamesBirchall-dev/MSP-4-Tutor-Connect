import django_filters
from .models import LessonType


class LessonFilter(django_filters.FilterSet):
    """A filter class for filtering LessonType
    instances based on their attributes."""

    q = django_filters.CharFilter(method="filter_title")

    subject = django_filters.CharFilter(
        field_name="subject",
        lookup_expr="iexact",
    )

    skill_level = django_filters.CharFilter(
        field_name="skill_level",
        lookup_expr="iexact",
    )

    class Meta:
        model = LessonType
        fields = ["q", "subject", "skill_level"]

    def filter_title(self, queryset, name, value):
        """Filter the queryset based on the title of the lesson type."""
        return queryset.filter(title__icontains=value)
