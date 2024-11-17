from django import forms
from .models import  Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('__all__')

        widgets = {

 'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'xxxx'}),
 'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
 'author': forms.Select(attrs={'class': 'form-control'}),
 'body': forms.Textarea(attrs={'class': 'form-control'}),
 'first_name': forms.TextInput(attrs={'class': 'form-control'}),
 'surname': forms.TextInput(attrs={'class': 'form-control'}),
 'address_1': forms.TextInput(attrs={'class': 'form-control'}),
 'address_2': forms.TextInput(attrs={'class': 'form-control'}),
 'address_3': forms.TextInput(attrs={'class': 'form-control'}),
 'address_4': forms.TextInput(attrs={'class': 'form-control'}),
 'code': forms.TextInput(attrs={'class': 'form-control'}),
'mailing_list': forms.TextInput(attrs={'class': 'form-control'}),

        }





class HomeView(ListView):
    model = Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model = Post
    template_name ='article_details.html'

class AddPostView(CreateView):
    model =  Post
    template_name = 'add_post.html'
    fields = '__all__'
    #fields =('photo', 'name')
class AddPhotoView(PhotoView):
    model =  Post
    template_name = 'add_photo.html'
    fields =('photo', 'name')