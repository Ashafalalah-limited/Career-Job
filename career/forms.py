from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['full_name', 'email', 'phone', 'cover_letter', 'profile_picture', 'cv']

    def clean_cv(self):
        cv = self.cleaned_data.get('cv')
        if cv:
            if not cv.name.endswith('.pdf'):
                raise forms.ValidationError("Only PDF files are allowed.")
            if cv.size > 5 * 1024 * 1024:
                raise forms.ValidationError("File size should not exceed 5MB.")
        return cv

    def clean_profile_picture(self):
        image = self.cleaned_data.get('profile_picture')
        if image:
            if image.size > 2 * 1024 * 1024:
                raise forms.ValidationError("Profile picture must be under 2MB.")
        return image
