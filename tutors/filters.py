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

    q = django_filters.CharFilter(
        method="filter_title",
        label="Search",
        )

    category = django_filters.ChoiceFilter(
        field_name="category",
        choices=LessonType.CATEGORY_CHOICES,
        label="Category",
    )

    subject = django_filters.ChoiceFilter(
        choices=LessonType.SUBJECT_CHOICES,
        label="Subject",
    )

    skill_level = django_filters.ChoiceFilter(
        choices=LessonType.SKILL_LEVEL_CHOICES,
        label="Skill level",
    )

    class Meta:
        """
        Configure the model and fields available for filtering.
        """

        model = LessonType
        fields = ["q", "category", "subject", "skill_level"]

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
