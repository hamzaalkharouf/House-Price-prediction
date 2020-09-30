from flask import Flask,request
import scikit_learn
import Write_Csv
app = Flask(__name__)
#append data(from url) to list
def Data_append(x1,x2,x3,x4,x5,x6):
    list_data=[]
    list_data.append(x1)
    list_data.append(x2)
    list_data.append(x3)
    list_data.append(x4)
    list_data.append(x5)
    list_data.append(x6)
    return list_data

#route /
#take data from url then send them to scikit_learn of Calculate price from scikit
#return information
@app.route('/')
def hello_world():
        transaction_date=float(request.args.get('transaction_date'))
        house_age=float(request.args.get('house_age'))
        distance_to_the__nearest_MRT_station=float(request.args.get('distance_to_the__nearest_MRT_station'))
        number_of_convenience_stores=float(request.args.get('number_of_convenience_stores'))
        latitude=float(request.args.get('latitude'))
        longitude=float(request.args.get('longitude'))
        list_data=[]
        list_data=Data_append(transaction_date,house_age,distance_to_the__nearest_MRT_station,number_of_convenience_stores,latitude,longitude)
        price=scikit_learn.path(list_data)
        list_data.append(price)
        Write_Csv.Write_Csv(list_data)
        return '''<h3>
        transaction date : {}<br>
        house age= {}<br>
        distance to the nearest MRT station= {}<br>
        number of convenience stores= {}<br>
        latitude= {}<br>
        longitude= {}<br>
        price ={}
        </h3>'''.format(transaction_date,house_age,distance_to_the__nearest_MRT_station,number_of_convenience_stores,latitude,longitude,price)

#to run servier => py app.py -path ./model.pickle
if __name__ == '__main__':
    app.run(port=5060,debug=False,use_reloader=False)
# http://127.0.0.1:5060/?transaction_date=2017.917&house_age=10&distance_to_the__nearest_MRT_station=306.59470&number_of_convenience_stores=15&latitude=24.98034&longitude=121.53951
