from flask import Flask , render_template, request
import requests

app=Flask(__name__)

@app.route('/')  # give a route. to display the index.html
def homepage():
    return render_template("index.html") # will give the html content 

@ app.route("/weatherapp",methods=['POST',"GET"])  # Bind the below function with this route.
def get_weatherdata(): # get weatherdata
    url="https://api.openweathermap.org/data/2.5/weather"
    # user enter 3 parameter details .
    param={
        'q':request.form.get("city"), # how to get the city name? use request to get details from form with id city
        'appid':request.form.get("appid"), # get("id from html")
        'units':request.form.get("units")
        }

    response = requests.get(url,params=param)
    data = response.json()
  # Now, i have to return a data to the user. (when user fill the parameters and enter search , the data must be shown)
    return f"data: {data}"



if __name__=='__main__':  # this is the main function 
    app.run(host='0.0.0.0',port=5002)