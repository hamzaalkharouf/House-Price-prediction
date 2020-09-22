from flask import Blueprint ,request
import pandas as pd
import os

parameter = Blueprint('parameter',__name__)

#take the path this file
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
#stores path csv
my_file_parameters = os.path.join(THIS_FOLDER,'csv\\lm_parameters.csv')
my_file_estate = os.path.join(THIS_FOLDER,'csv\\Real estate.csv')

#Read data in Csv
def Read_Csv():
    data = pd.read_csv(my_file_parameters)
    Thetas=data.columns
    Thetas = [item.replace("\'", "") for item in Thetas]
    Thetas = [float(Theta) for Theta in Thetas]
    Theta0=data.iloc[0,0]
    return Thetas ,Theta0

#writeing , Storing new information
def Write_Csv(list_data):
    df = pd.read_csv(my_file_estate)
    file = open(my_file_estate,"a")
    number=df['No'].values[-1]
    number+=1
    file.write(str(number)+",")
    for i in list_data:
        if i != list_data[6]:
            file.write(str(i)+",")
        else :file.write(str(i)+"\n")
    file.close()
    df.reset_index(drop = True,inplace=True)


#Calculate the new Real estate price
def Computation(list_data):
    Thetas ,Theta0=Read_Csv()
    price = 0
    for index ,feature in enumerate(list_data):
        price += feature * Thetas[index]
    price +=Theta0
    return price

#append data (new Real estate)to list
def Data_append(x1,x2,x3,x4,x5,x6):
    list_data=[]
    list_data.append(x1)
    list_data.append(x2)
    list_data.append(x3)
    list_data.append(x4)
    list_data.append(x5)
    list_data.append(x6)
    return list_data

#home page parameter
@parameter.route('/')
def index():
    return 'parameter .views!'
# http://127.0.0.1:5000/parameter/

#child page parameter
#show  information new Real estate and price
#take from url information of new Real estate , send them to function Data_append then return them as a list
#send them to function Computation to Calculate the new Real estate price
#appen price to list
#send the list through function Write_Csv to Store in csv(Real estate)
@parameter.route('/Realestate')
def ml():
    transaction_date=float(request.args.get('transaction_date'))
    house_age=float(request.args.get('house_age'))
    distance_to_the__nearest_MRT_station=float(request.args.get('distance_to_the__nearest_MRT_station'))
    number_of_convenience_stores=float(request.args.get('number_of_convenience_stores'))
    latitude=float(request.args.get('latitude'))
    longitude=float(request.args.get('longitude'))
    list_data=[]
    list_data=Data_append(transaction_date,house_age,distance_to_the__nearest_MRT_station,number_of_convenience_stores,latitude,longitude)
    price =Computation(list_data)
    list_data.append(price)
    Write_Csv(list_data)

    return '''<h3>
    transaction date : {}<br>
    house age= {}<br>
    distance to the nearest MRT station= {}<br>
    number of convenience stores= {}<br>
    latitude= {}<br>
    longitude= {}<br>
    price ={}
    </h3>'''.format(transaction_date,house_age,distance_to_the__nearest_MRT_station,number_of_convenience_stores,latitude,longitude,price)
# http://127.0.0.1:5000/parameter/Realestate?transaction_date=2017.917&house_age=10&distance_to_the__nearest_MRT_station=306.59470&number_of_convenience_stores=15&latitude=24.98034&longitude=121.53951
