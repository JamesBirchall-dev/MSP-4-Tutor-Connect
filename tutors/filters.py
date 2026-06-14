import django_filters
from .models import LessonType

"""
FILTERS FOR TUTORS APP

This module contains custom filter classes used to refine
lesson search results based on user-selected criteria.
"""


class LessonFilter(django_filters.FilterSet):
    """
    Provides filtering functionality for LessonType querysets.

    Available filters:
    - q: Search lesson titles
    - subject: Filter by subject category
    - skill_level: Filter by skill level
    """

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
        """
        Configure the model and fields available for filtering.
        """

        model = LessonType
        fields = ["q", "subject", "skill_level"]

    def filter_title(self, queryset, name, value):
        """
        Perform a case-insensitive partial match against lesson titles.

        Args:
            queryset: The queryset being filtered.
            name: The filter field name.
            value: The search term entered by the user.

        Returns:
            QuerySet: Filtered lessons matching the supplied title text.
        """
        return queryset.filter(title__icontains=value)
