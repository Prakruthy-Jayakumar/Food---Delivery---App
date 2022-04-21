from django.forms import forms, ModelForm
from food_app.models import Place, Order, Food


class OrderNowForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['place'].queryset = Place.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['place'].queryset = Place.objects.filter(district_id=district_id).order_by('dist_name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['place'].queryset = self.instance.district.place_set.order_by('place_name')