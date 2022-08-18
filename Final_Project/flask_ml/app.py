from flask import Flask, redirect, render_template, request, url_for
import pandas as pd
import numpy as np
import pickle
from os.path import join, dirname, realpath
from sklearn.metrics import mean_absolute_error



#initiate a flask
app = Flask(__name__,template_folder='templates', static_folder='static')

#Function that Load the model

def predict_price(Year,HP,Kilometers,Automatic_Manual,Segmet_ABCDEF,Maker,Fuel,Max_vel,Cylindernumber):
    #X_test = pd.read_pickle(r'../flask_ml/xtest.p')
    X_test = pd.read_pickle("c:\\Users\\Sergio Manzano\\Documents\\Ironhack bootcamp\\Final_Project\\flask_ml\\xtest.p")
    
    y_test = pd.read_pickle("c:\\Users\\Sergio Manzano\\Documents\\Ironhack bootcamp\\Final_Project\\flask_ml\\ytest.p")



    #X_test = pd.read_pickle("C:\\Users\\Sergio Manzano\\Documents\\Ironhack bootcamp\\Final_Project\\flask_ml\\xtest.p")

    #y_test = pd.read_pickle(r'../flask_ml/ytest.p')


    templist = [0,0, 0,0,
                    0,0,0, 
                    0,0,0,
                    0,0,0,0,
                    0,0,0,0,
                    0,0,0,0,
                    0,0,0,0,
                    0,0,0,0,
                    0,0,0,0,
                    0,0,0,0,
                    0,0,0,0,
                    0,0,0,
                    0,0,0]
        
    year = int(Year)
    templist[0] = year
    
    HP = int(HP) 
    templist[1] = HP
    
    Kilometers = int(Kilometers)
    templist[2] = Kilometers
    
    motor= 'Motor_'+str(Automatic_Manual).capitalize()
    motorindx =X_test.columns.tolist().index(motor)
    templist[motorindx] = 1
    
    segment = 'Segment_Segment'+str(Segmet_ABCDEF).capitalize()
    segmentindx =X_test.columns.tolist().index(segment)
    templist[segmentindx] = 1
    
    maker = 'Maker_'+str(Maker).upper()
    makertindx =X_test.columns.tolist().index(maker)
    templist[makertindx] = 1
    
    fuel = 'Fuel_'+str(Fuel).capitalize()
    fuelindx =X_test.columns.tolist().index(fuel)
    templist[fuelindx] = 1
    
    maxvel = int(Max_vel)
    templist[46] = maxvel
    
    Cylindernumber = int(Cylindernumber)
    templist[47] = Cylindernumber
    
    xgb_model = pickle.load(open("c:\\Users\\Sergio Manzano\\Documents\\Ironhack bootcamp\\Final_Project\\flask_ml\\model.p",'rb'))
    score = xgb_model.score(X_test,y_test)
    score = round(score*100,3)
    #New
    y_pred = xgb_model.predict(X_test)
    scoremae= mean_absolute_error(y_test, y_pred)
    #year,HP,Kilometers,motor,segment,maker,fuel,maxvel,Cylindernumber
    
    result = xgb_model.predict(np.array([templist]))
    
    #result_range1 = round(result[0]*.80)
    #result_range2 = round(result[0]*1.20)

    #New
    result_range1 = round(result[0]-scoremae)
    result_range2 = round(result[0]+scoremae)
    
    result1 = str(f'Year: {year} / Maker: {str(Maker)} / HP: {HP} / Kilometers: {Kilometers} / Motor: {Automatic_Manual} / Segment: {Segmet_ABCDEF} / Fue: {Fuel} / Max vel: {Max_vel} / Cylinder number: {Cylindernumber} ***********************************Price prediction: €{round(result[0],0)} Best price range: €{result_range1}, - €{result_range2}      (MAE : {round(scoremae,0)}  Score R2: {score}) *******************   ')
    
    return result1 



@app.route('/ml', methods = ('GET','POST'))
def predict():
    if request.method == "GET":

        maker_vals = pd.read_pickle("c:\\Users\\Sergio Manzano\\Documents\\Ironhack bootcamp\\Final_Project\\flask_ml\\maker_vals.p")
        maker_vals = list(maker_vals['Maker'])
        return render_template('main.html', makers=maker_vals)

    if request.method == "POST":
        input_parameter1 = (request.form['Year'])
        input_parameter2= request.form['HP']
        input_parameter3 = request.form['Kilometers']
        input_parameter4 = request.form['Automatic_Manual']
        input_parameter5 = request.form['Segmet_ABCDEF']
        input_parameter6 = request.form['makers']
        input_parameter7 = request.form['Fuel']
        input_parameter8 = request.form['Max_vel']
        input_parameter9 = request.form['Cylindernumber']


        
        prediction = predict_price(input_parameter1,input_parameter2,
        input_parameter3,input_parameter4,input_parameter5,input_parameter6,
        input_parameter7,input_parameter8,input_parameter9)
        result = str(prediction)
        
        return render_template('main.html', my_result = result)
    


if __name__ == '__main__':
    app.run(debug=True)

#Running app which contains all the logic/routes defined above##    
app.run(debug=True)


#predict_price(2018,73.944,153192,'manual','c','opel','diEsel',164.0,4)


