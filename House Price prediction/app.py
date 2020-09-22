from flask import Flask
#import the parameter.views
from parameter.views import parameter
app = Flask(__name__)

#register of parameter
app.register_blueprint(parameter,url_prefix="/parameter")

#home page
@app.route('/')
def index():
    return 'hello world!'
# http://127.0.0.1:5000/

#Run
if __name__ =="__main__":
    app.run(port =5000 ,debug=False)
