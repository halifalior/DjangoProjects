from django import forms

class PassengerForm(forms.Form):

    user_input_pclass=forms.IntegerField(min_value=1,max_value=100,
                                         widget=forms.NumberInput(attrs={
                                             "class": "form-control",
                                             "placeholder": "pclass here"
                                         }))

    user_input_sex=forms.IntegerField(min_value=1,max_value=100,
                                      widget=forms.NumberInput(attrs={
                                          "class": "form-control",
                                          "placeholder": "sex here"
                                      }))
    user_input_age=forms.IntegerField(min_value=1,max_value=100,
                                      widget=forms.NumberInput(attrs={
                                          "class": "form-control",
                                          "placeholder": "age here"
                                      }))
    user_input_sibsp=forms.IntegerField(min_value=1,max_value=100,
                                        widget=forms.NumberInput(attrs={
                                            "class": "form-control",
                                            "placeholder": "pclass here"
                                        }))
    user_input_parch=forms.IntegerField(min_value=1,max_value=100,
                                        widget=forms.NumberInput(attrs={
                                            "class": "form-control",
                                            "placeholder": "parch here"
                                        }))
    user_input_fare=forms.IntegerField(min_value=1,max_value=100,
                                       widget=forms.NumberInput(attrs={
                                           "class": "form-control",
                                           "placeholder": "fare here"
                                       }))
    user_input_embarked=forms.IntegerField(min_value=1,max_value=100,
                                           widget=forms.NumberInput(attrs={
                                               "class": "form-control",
                                               "placeholder": "embarked here"
                                           }))
    user_input_title=forms.IntegerField(min_value=1,max_value=100,
                                        widget=forms.NumberInput(attrs={
                                            "class": "form-control",
                                            "placeholder": "title here"
                                        }))



class TestForm(forms.Form):

    u_user=forms.CharField(label="User Name",max_length=10,
        widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "user"}))

    u_age=forms.IntegerField(label="Age",min_value=0,max_value=120,required=False,
         widget=forms.NumberInput(attrs={
         "class":"form-control",
         "placeholder": "age" }))

    u_hight=forms.DecimalField(label="Hight in CM",min_value=1.2,required=False,decimal_places=2,
       widget=forms.NumberInput(attrs={
       "class": "form-control",
       "placeholder": "hight "}))


    u_email=forms.EmailField(label="Email Address",
        widget=forms.EmailInput(attrs={
         "class":"form-control",
         "placeholder": "email" }))

    u_student=forms.BooleanField(label="Is Student?",required=False,
         widget=forms.CheckboxInput(attrs={
         "class": "form-control",
         "placeholder": "email"}))

    u_time = forms.TimeField(label="time", required=False,
                                   widget=forms.TimeInput(attrs={
                                       "class": "form-control",
                                       "placeholder": "time"}))
    u_date = forms.DateField(label="date",
                                   widget=forms.DateInput(attrs={
                                       "class": "form-control",
                                       "placeholder": "date"}))




