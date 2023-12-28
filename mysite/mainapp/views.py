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

def unknown(request):
    val1 = float(request.POST.get('n1'))
    val2 = float(request.POST.get('n2'))
    val3 = float(request.POST.get('n3'))
    val4 = float(request.POST.get('n4'))
    val5 = float(request.POST.get('n5'))
    val6 = float(request.POST.get('n6'))
    val7 = float(request.POST.get('n7'))
    val8 = float(request.POST.get('n8'))
    val9 = float(request.POST.get('n9'))
    val10 = float(request.POST.get('n10'))
    val11 = float(request.POST.get('n11'))
    val12 = float(request.POST.get('n12'))
    val13 = float(request.POST.get('n13'))
    val14 = float(request.POST.get('n14'))
    val15 = float(request.POST.get('n15'))
    val16 = float(request.POST.get('n16'))
    val17 = float(request.POST.get('n17'))
    val18 = float(request.POST.get('n18'))
    val19 = float(request.POST.get('n19'))
    val20 = float(request.POST.get('n20'))
    val21 = float(request.POST.get('n21'))
    val22 = float(request.POST.get('n22'))
    val23 = float(request.POST.get('n23'))
    val24 = float(request.POST.get('n24'))
    val25 = float(request.POST.get('n25'))
    val26 = float(request.POST.get('n26'))
    val27 = float(request.POST.get('n27'))
    val28 = float(request.POST.get('n28'))
    val29 = float(request.POST.get('n29'))
    val30 = float(request.POST.get('n30'))
    val31 = float(request.POST.get('n31'))
    val32 = float(request.POST.get('n32'))
    val33 = float(request.POST.get('n33'))
    val34 = float(request.POST.get('n34'))
    val35 = float(request.POST.get('n35'))
    val36 = float(request.POST.get('n36'))
    val37 = float(request.POST.get('n37'))
    val38 = float(request.POST.get('n38'))
    val39 = float(request.POST.get('n39'))
    val40 = float(request.POST.get('n40'))
    val41 = float(request.POST.get('n41'))
    val42 = float(request.POST.get('n42'))
    val43 = float(request.POST.get('n43'))
    val44 = float(request.POST.get('n44'))
    val45 = float(request.POST.get('n45'))
    val46 = float(request.POST.get('n46'))
    val47 = float(request.POST.get('n47'))
    val48 = float(request.POST.get('n48'))
    val49 = float(request.POST.get('n49'))
    val50 = float(request.POST.get('n50'))
    val51 = float(request.POST.get('n51'))
    val52 = float(request.POST.get('n52'))
    val53 = float(request.POST.get('n53'))