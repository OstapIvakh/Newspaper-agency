from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from agency.models import Newspaper, Redactor


class NewspaperForm(forms.ModelForm):
    publishers = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Newspaper
        fields = ["title", "content", "publish_date", "topic", "publishers"]


class NewspaperSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by title"}
        )
    )


class RedactorCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Redactor
        fields = UserCreationForm.Meta.fields + (
            "years_of_experience",
            "first_name",
            "last_name",
            "email"
        )

    def save(self, commit=True):
        user = super(RedactorCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class RedactorUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter your first name',
            'class': 'form-control mb-3',
        }
    ))

    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter your last name',
            'class': 'form-control mb-3',
        }
    ))

    years_of_experience = forms.IntegerField(label='Years of experience', widget=forms.NumberInput(
        attrs={
            'placeholder': 'Enter your years of experience',
            'class': 'form-control mb-3',
        }
    ))

    class Meta:
        model = Redactor
        fields = ("first_name", "last_name", "years_of_experience")


class RedactorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by username"}
        )
    )


class TopicSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={"placeholder": "Search by topic"}
        )
    )
