from django import forms

from blogapp.models import Blog


class CreateNewPostForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Blog
        fields = ('category', 'acces_level', 'name', 'cover', 'short_desc', 'description', 'doc_file', 'author', 'published_by')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
        self.fields['category'].widget.attrs['class'] = 'form-control form-custom mb-4'
        self.fields['acces_level'].widget.attrs['class'] = 'form-control form-custom'
        self.fields['doc_file'].widget.attrs['class'] = 'form-control-file'
        self.fields['cover'].widget.attrs['class'] = 'form-control-file'
