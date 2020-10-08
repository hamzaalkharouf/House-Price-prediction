FROM python:3

# set a directory for the app
WORKDIR /House-Price-prediction

# copy all the files to the container
COPY . .

# install dependencies
RUN pip3 install pandas pickle-mixin argparse numpy Flask

COPY . /House-Price-prediction
# define the port number the container should expose
EXPOSE 5060
CMD python -c "print('http://127.0.0.1:5060/?transaction_date=2017.917&house_age=10&distance_to_the__nearest_MRT_station=306.59470&number_of_convenience_stores=15&latitude=24.98034&longitude=121.53951')"

# run the command
CMD ["python", "py app.py -path ./model.pickle"]

