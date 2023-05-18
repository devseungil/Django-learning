from django import forms
from .models import Article
# class ArticleForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        #fields = ('~~','~~',) 갖고오고싶은것만 갖고오기 모델에서
        #exclude = ('~~',) ~~빼고 전부 가져오기
        #exclude랑 fields는 동시에 사용하면 안됨 (익스는 빼고가져와라 필드도 가져와라 = 겹침)