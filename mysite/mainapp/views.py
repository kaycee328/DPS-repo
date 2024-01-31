# from typing import Any
import pandas as pd
import numpy as np
from typing import Any
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from .forms import DivorcePredictionForm
from django.contrib.auth.decorators import login_required
from sklearn.model_selection import train_test_split
from .models import Customer, Divorce
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin 
from django.views.generic import DetailView, ListView, UpdateView, FormView, CreateView, TemplateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
# from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# UPDATED VERSION OF DPS CODE
class HomePage(LoginRequiredMixin, TemplateView):  # HOMEPAGE VIEW
    template_name = 'mainapp/cbv/homepage.html'

@login_required
def predictionform(request):
    pd.set_option('display.max_columns', None)
    my_data = pd.read_csv('dps.csv')
    # print(str(request.user).upper())

    x = my_data.drop(columns='Divorce')
    y = my_data['Divorce']
    # y = my_data.drop(my_data.iloc[:, 0:-1], axis=1)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

    decision_tree_model = DecisionTreeClassifier()
    decision_tree_model.fit(x_train, y_train)

    if request.method == 'POST': 
        delete_user_model = Divorce.objects.filter(user=request.user).delete()

        user_model = Divorce(user=request.user)

        if not delete_user_model:
            user_model = Divorce(user=request.user)
        
        form = DivorcePredictionForm(request.POST)

        if form.is_valid():
            print('FORM VALID')
            print(form.is_valid())

            vals = [form.cleaned_data[f'n{i}'] for i in range(1, 53)]

            for i, val in enumerate(vals, start=1):
                attribute_name = f'n{i}'
                setattr(user_model, attribute_name, val)
                print(getattr(user_model, attribute_name))

            
            # Make predictions and update the Divorce object
            predictions = decision_tree_model.predict([vals])
            user_model.divorce_status = predictions == 1

            user_model.save()
        return redirect('output')
        
    else:
        form = DivorcePredictionForm()

    return render(request, 'mainapp/cbv/testing.html', {'form': form})

class ResultView(TemplateView):     # RESULT PAGE VIEW
    template_name = 'mainapp/cbv/result-output.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
         context =  super().get_context_data(**kwargs)
         context['result'] = Divorce.objects.filter(user = self.request.user).first()
         return context
    