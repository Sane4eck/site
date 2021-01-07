from django import forms
from articles.models import Article, Comment
# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Ваше имя, сер!?', max_length=100)


class PostForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('article_title', 'article_text',)