from .models import Time_opt
import django_filters
from django_filters import DateFilter, CharFilter,DateFromToRangeFilter

from .models import * 

 
class Time_optFilter(django_filters.FilterSet):
 
    class Meta:
        model = Time_opt
        fields = '__all__'



class OrderFilter(django_filters.FilterSet):
	start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	range_date = DateFromToRangeFilter(field_name="date_created")
	# note = CharFilter(field_name='note', lookup_expr='icontains')


	class Meta:
		model = peoplemove
		fields = '__all__'
		exclude = ['ps','date_created']

class agenderFilter(django_filters.FilterSet):
	range_date = DateFromToRangeFilter(field_name="date_created")
	# start_age = DateFilter(field_name="age", lookup_expr='gte')
	# end_age = DateFilter(field_name="age", lookup_expr='lte')
	start_date = DateFilter(field_name="date_created", lookup_expr='gte')
	end_date = DateFilter(field_name="date_created", lookup_expr='lte')
	# range_age = DateFromToRangeFilter(field_name="age")

	# note = CharFilter(field_name='note', lookup_expr='icontains')


	class Meta:
		model = agender
		fields = '__all__'
		exclude = ['ps', 'date_created']


