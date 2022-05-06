
from Blog.models import Post, Comment
from django import forms


class PostForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)

    #     for field in self.Meta.required:
            # self.fields[field].required = True
    
    class Meta:
        model=Post
        fields=('title','text')
        widgets={ #set up classes to edit widget css
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}) 
        }
        # required = ('title', 'text')

    def clean(self):
        cd = self.cleaned_data

        author = cd.get("author")
        title = cd.get("title")
        text = cd.get("text")
        # print('3',author,title,text)
        # print(cd)

        return cd


class CommentForm(forms.ModelForm):
    
    class Meta:
        model=Comment
        fields=('author','text')

        widgets={ #set up classes to edit widget css
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}) 
        }