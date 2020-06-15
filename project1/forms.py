from django import forms
from .models import uploads_sl,uploads_cat,category, uploads_qb
shop_choice=[
    ('fitter','Fitter'),
    ('carpenter','Carpenter'),
    ('welder','Welder'),
    ('blacksmith','Blacksmith'),
    ('painter','Painter'),
    ('personnel','Personnel'),
    ('combined','Combined KH List'),
    ('milwright','Milwright'),
    ('trimmer','Trimmer'),
    ('machinist','Machinist'),
]
desg_choice=[
    ('sse','SSE'),
    ('je','JE'),
    ('sr.tech','Sr. Tech'),
    ('tech-i','Tech I'),
    ('tech-ii','Tech II'),
    ('tech-iii','Tech III'),
    ('khalasi','Khalashi'),
    ('ch.os','Ch. OS'),
    ('os','OS'),
    ('sr.clerk','Sr. Clerk'),
    ('jr.clerk','Jr. Clerk'),
    ('peon','Peon'),
]
class sl_form(forms.Form):
    shop=forms.CharField(widget=forms.Select(choices=shop_choice))
    desg=forms.CharField(widget=forms.Select(choices=desg_choice))


class seniority_add_form(forms.ModelForm):
    # shop=forms.CharField(widget=forms.Select(choices=shop_choice))
    # desg=forms.CharField(widget=forms.Select(choices=desg_choice))
    class Meta():
        model=uploads_sl
        fields=['files','cwm_letter_no','subject','shop','desg']

# c=[
#     ('one','One'),
#     ('two','two'),
# ]
class qb_add_form(forms.ModelForm):
    class Meta():
        model=uploads_qb
        fields='__all__'

class nofi_add_form(forms.ModelForm):
    class Meta():
        model=uploads_cat
        fields="__all__"
        
