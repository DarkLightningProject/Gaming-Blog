from django import forms
from .models import PostModel,Comment
from ckeditor.widgets import CKEditorWidget

class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}))
    class Meta:
        model = PostModel
        fields = ('title','content')


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title','content','gaming_image')

class PostForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'content', 'gaming_image']




class PostForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = PostModel
        fields = ['title', 'content']  # Include other fields as needed


class CommentForm(forms.ModelForm):
        content = forms.CharField(label= '',widget=forms.TextInput(attrs={'placeholder': "Add Comment here...."}))
        class Meta:
         model = Comment
         fields = ('content',)
        