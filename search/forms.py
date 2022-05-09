from sre_parse import CATEGORIES
from django import forms

categoryChoices= [
    ('0', 'All Categories'),
    ('20081', 'Antiques'),
    ('550', 'Art'),
    ('2984', 'Baby'),
    ('267', 'Books'),
    ('12576', 'Business, Industrial'),
    ('625', 'Cameras, Photo'),
    ('15032', 'Cell Phones, Accessories'),
    ('11450', 'Clothing, Shoes, Accessories'),
    ('11116', 'Coins, Paper Money'),
    ('1', 'Collectibles'),
    ('58058', 'Computers/Tablets, Networking'),
    ('293', 'Consumer Electronics'),
    ('14339', 'Crafts'),
    ('237', 'Dolls, Bears'),
    ('11232', 'DVDs, Movies'),
    ('45100', 'Entertainment Memorabilia'),
    ('172008', 'Gift Cards, Coupons'),
    ('26395', 'Health, Beauty'),
    ('11700', 'Home, Garden'),
    ('281', 'Jewelry, Watches'),
    ('11233', 'Music'),
    ('619', 'Musical Instruments, Gear'),
    ('1281', 'Pet Supplies'),
    ('870', 'Pottery, Glass'),
    ('10542', 'Real Estate'),
    ('316', 'Specialty Services'),
    ('888', 'Sporting Goods'),
    ('64482', 'Sports Mem, Cards, Fan Shop'),
    ('260', 'Stamps'),
    ('1305', 'Tickets, Experiences'),
    ('220', 'Toys, Hobbies'),
    ('3252', 'Travel'),
    ('1249', 'Video Games, Consoles'),
    ('99', 'Everything Else'),
    ]


class MostWatchedForm(forms.Form):
    categoryId= forms.CharField(label='Please select a category', widget=forms.Select(choices=categoryChoices))
    #maxResults = forms.IntegerField(required=False)


class BidsSearchForm(forms.Form):
    keywords = forms.CharField(max_length=350, min_length = 2, required=False)
    categoryId= forms.CharField(label='Please select a category', widget=forms.Select(choices=categoryChoices))

    def clean(self):
        if self.cleaned_data['keywords'] != '' or self.cleaned_data['categoryId'] != '0' :
                return super().clean() #For python 3
        raise forms.ValidationError('Please select a category or type in the field.')

class TypoSearchForm(forms.Form):
    keywords = forms.CharField(max_length=350, min_length = 2, required=True)
    categoryId= forms.CharField(label='Please select a category', widget=forms.Select(choices=categoryChoices))

    def clean(self):
        if self.cleaned_data['keywords'] != '' or self.cleaned_data['categoryId'] != '0' :
                return super().clean() #For python 3
        raise forms.ValidationError('Please select a category or type in the field.')