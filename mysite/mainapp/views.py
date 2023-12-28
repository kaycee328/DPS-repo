from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from .forms import DivorcePredictionForm
from django.contrib.auth.decorators import login_required
from sklearn.model_selection import train_test_split
from .models import Dps
# from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

@login_required
def home(request):
    return render(request, 'mainapp/index.html')

@login_required
def predict(request):
        if request.method == "POST":
            result = None  # Initialize result
            pd.set_option('display.max_columns', None)
            my_data = pd.read_csv('dps.csv')
            user = request.user
            print(str(user).upper())
            print(request.POST.get('submit'))

            x = my_data.drop(columns='Divorce')
            y = my_data.drop(my_data.iloc[:, 0:-1], axis=1)
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)

            descision_tree_model = DecisionTreeClassifier()
            descision_tree_model.fit(x_train, y_train)

            # if request.POST.get('submit'):
            values = [request.POST[f'n{i}'] for i in range(1, 53)]
            # print(values)

            predictions = descision_tree_model.predict([values])
            # Retrieve or create the user's Dps object
            user_dps = Dps.objects.filter(current_user=user).first()

            if user_dps is None:
                # If the user_dps does not exist, create a new one
                user_dps = Dps(current_user=user)
                user_dps.save()
            # Now user_dps holds the existing or newly created Dps object


            # Update the 'divorced' field based on the prediction
            user_dps.divorced = predictions == [1]
            user_dps.save()
            if predictions == [1]:
                result = "DIVORCED!"
            else:
                result = "NOT DIVORCED!"
            context = {'status': result}
            
            return render(request, 'mainapp/result.html', context)
        return render(request, 'mainapp/predict.html')


@login_required
def result(request):
    return render(request, 'mainapp/result.html')

