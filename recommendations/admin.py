from django.contrib import admin
from .models import Recommendation


@admin.register(Recommendation)
class RecommendationAdmin(admin.ModelAdmin):
    list_filter = ('type_of_recommendation', 'date_posted', 'posted_by')
    search_fields = ['posted_by', 'title',]
