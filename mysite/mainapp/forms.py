from django.forms import ModelForm
from .models import Divorce

class DivorcePredictionForm(ModelForm):
    class Meta:
        model = Divorce
        # fields = []
        # for i in range(1, 53):
        #     fields.append('n'+str(i))
        fields = [f'n{i}' for i in range(1, 53)]














# class DivorcePredictionForm(forms.Form):
#     n1 = forms.FloatField(min_value= 0, max_value= 4, label= 'When one of you apologizes after a discussion goes in a bad direction, does it extend?')
#     n2 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you ignore each other\'s differences at the end of the day?')
#     n3 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you and your partner take discussions to correct your issues?')
#     n4 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you and your partner contact each other after an argument?')
#     n5 = forms.FloatField(min_value= 0, max_value= 4, label= 'Is time spent with your partner special?')
#     n6 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you have time for each other at home?')
#     n7 = forms.FloatField(min_value= 0, max_value= 4, label= 'Are you and your partner like strangers at home?')
#     n8 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you enjoy holidays with your partner?')
#     n9 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you enjoy travelling with your partner?')
#     n10 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you and your partner have similar goals?')
#     n11 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you think that you and your partner can live in harmony?')
#     n12 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you and your partner have similar values in terms of personal freedom?')
#     n13 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you both have similar goals for your children or friends?')
#     n14 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you both have similar dreams on how you want to live?')
#     n15 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do the both of you have similar ideas on what love should be?')
#     n16 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you share the same views about being happy in life?')
#     n17 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you have similar ideas on what marriage should be?')
#     n18 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you have similar ideas about how roles should be in marriage?')
#     n19 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do the both of you have similar values in trust?')
#     n20 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you know what your partner likes?')
#     n21 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you know how to take care of your partner when they are sick?')
#     n22 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you know your partner\'s favourite meal?')
#     n23 = forms.FloatField(min_value= 0, max_value= 4, label= 'Can you tell when your partner is stressed?')
#     n24 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you have knowledge of your partner\'s inner world?')
#     n25 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you know your partner\'s basic concerns?')
#     n26 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you know what stresses your partner?')
#     n27 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you know your partner\'s hopes and wishes?')
#     n28 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you know your partner very well?')
#     n29 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you know your partner\'s friend circle?')
#     n30 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you feel aggressive when you argue with your partner?')
#     n31 = forms.FloatField(min_value= 0, max_value= 4, label= 'When discussing with your partner do you use vulgar expressions?')
#     n32 = forms.FloatField(min_value= 0, max_value= 4, label= 'Can you use negative statements about your partner\'s personality during your discussions?')
#     n33 = forms.FloatField(min_value= 0, max_value= 4, label= 'Can you use offensive expressions during your discussions?')
#     n34 = forms.FloatField(min_value= 0, max_value= 4, label= 'Can you insult your partner during your discussions?')
#     n35 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you humiliate your partner when you argue?')
#     n36 = forms.FloatField(min_value= 0, max_value= 4, label= 'Is your argument with your partner calm?')
#     n37 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you hate your partner\'s way of bringing things up?')
#     n38 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you and your partner fight during arguments?')
#     n39 = forms.FloatField(min_value= 0, max_value= 4, label= 'Are you and your partner already fighting before you know what\'s going on?')
#     n40 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you lose your calm when talking to your partner about something?')
#     n41 = forms.FloatField(min_value= 0, max_value= 4, label= 'When you and your partner are arguing, do you say a word?')
#     n42 = forms.FloatField(min_value= 0, max_value= 4, label= 'Are you mostly thirsty to calm the environment?')
#     n43 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you think it\'s good for you to leave home for a while?')
#     n44 = forms.FloatField(min_value= 0, max_value= 4, label= 'Would you rather stay silent than argue with your partner?')
#     n45 = forms.FloatField(min_value= 0, max_value= 4, label= 'Even if you are right in the argument, are you thirsty to upset the other side?')
#     n46 = forms.FloatField(min_value= 0, max_value= 4, label= 'When you argue with your partner, do you remain silent because you are afraid of not being able to control your anger?')
#     n47 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you feel like you are right during your discussions with your partner?')
#     n48 = forms.FloatField(min_value= 0, max_value= 4, label= 'Do you have anything to do with what your partner accused you of?')
#     n49 = forms.FloatField(min_value= 0, max_value= 4, label= 'Are you the one who is wrong about the problems at home?')
#     n50 = forms.FloatField(min_value= 0, max_value= 4, label= 'Would you hesitate to tell anyone about your partner\'s inadequacies?')
#     n51 = forms.FloatField(min_value= 0, max_value= 4, label= 'When you discuss your partner, do you tell people about their inadequacies?')
#     n52 = forms.FloatField(min_value= 0, max_value= 4, label= 'Lastly, are you afraid of telling people about your partner\'s inadequacies?')
