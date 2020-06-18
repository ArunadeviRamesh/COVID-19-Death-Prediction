from flask import *
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
app = Flask(__name__)  
@app.route('/')  
def home1 ():  
    return render_template("home1.html")  
@app.route('/login')  
def login():  
    return render_template("login.html");  
@app.route('/validate', methods = ["POST"])  
def validate():  
	if request.method=='POST':
		a=request.form['coun'];
		b=request.form['confir']
		b=list(b)
		z=[]
		for i in range(len(b)):
			if(b[i]!=','):
				z.append(b[i])
		for i in range(len(z)):
			z[i]=int(z[i])
			strings = [str(integer) for integer in z]
			a_string = "".join(strings)
			p = int(a_string)
		df=pd.read_csv("world.csv")
		c=list(df["location"])
		d=list(df["total_cases"])
		e=list(df["tomorrow_deaths"])
		x=[]
		y=[]
		for i in range(len(c)):	
			if(a==c[i]):
				x.append(d[i]);
				y.append(e[i]);
		x=pd.DataFrame(x)
		y=pd.DataFrame(y)
		print(x)
		x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.4,random_state=0)
		lr=LinearRegression()
		lr.fit(x_train,y_train)
		y_pred=lr.predict(x_test)
		print(p);
		print(lr.predict([[p]]))
		h= lr.predict([[p]])
		return render_template("demo.html",h=h);
@app.route('/success')  
def success():  
    return "logged in successfully",a  
  
if __name__ == '__main__':  
    app.run(debug = True)  