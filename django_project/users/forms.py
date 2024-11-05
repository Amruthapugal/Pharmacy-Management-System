from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm) :
	email = forms.EmailField()
	username = forms.TextInput(attrs= {'size' :10, 'title':'Your username' })

	class meta :
		model = User
		fields = ['username', 'name', 'password1', 'password2']

 		


'''class PostForm(forms.ModelForm):
    class Meta:
        model = medicines
        fields = ('medicine_id','medicine_name','cost', 'medicine_type')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['medicine_type'].queryset = medicines.objects.none()		'''

	