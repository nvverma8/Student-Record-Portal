from django import forms
from .models import Student

class SATResultForm(forms.ModelForm):
  def __init__(self, *args, **kwargs):
        # Get the 'instance' parameter if it exists
        instance = kwargs.get('instance')
        # Call the superclass constructor
        super(SATResultForm, self).__init__(*args, **kwargs)

        # Disable fields for update (if instance is provided)
        if instance:
            self.fields['name'].disabled = True
            self.fields['address'].disabled = True
            self.fields['city'].disabled = True
            self.fields['country'].disabled = True
            self.fields['pincode'].disabled = True
            # You can selectively disable fields based on your requirement
  class Meta:
      model = Student
      fields = ['name', 'address', 'city', 'country', 'pincode', 'sat_score']

      labels = {
          'name': 'Name',
          'address': 'Address',
          'city': 'City',
          'country': 'Country',
          'pincode': 'Pincode',            
          'sat_score': 'SAT Score',
        }

      widgets = {
          'name': forms.TextInput(attrs={'class': 'form-control'}),
          'address': forms.TextInput(attrs={'class': 'form-control'}),
          'city': forms.TextInput(attrs={'class': 'form-control'}),            'country': forms.TextInput(attrs={'class': 'form-control'}),
          'pincode': forms.TextInput(attrs={'class': 'form-control'}),
          'sat_score': forms.NumberInput(attrs={'class': 'form-control'}),
        }

  def clean_sat_score(self):
    
      sat_score = self.cleaned_data['sat_score']
      if sat_score < 0 or sat_score > 100:  # Assuming SAT scores are between 0 and 100
          raise forms.ValidationError("SAT score should be between 0 and 100")
      return sat_score
