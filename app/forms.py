from django import forms
g=[('MALE','male'),('FEMALE','female')]
c=[('PYTHON','python'),('DJANGO','django'),('SQL','sql')]

class Studentform(forms.Form):
    name=forms.CharField(max_length=30)
    age=forms.IntegerField()
    email=forms.EmailField()
    address=forms.CharField(max_length=30,widget=forms.Textarea(attrs={'cols':10,'rows':5}))
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    #courses=forms.MultipleChoiceField(choices=c)
    courses=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)

