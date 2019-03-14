import pandas as pd
#import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.image as plt1
#2019-03-07,2005.0000,2021.0000,2000.2000,2012.5000,1104116
import urllib.request
from flask import Flask,render_template,url_for,request,jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/predict" , methods=['GET', 'POST'])
def test():
    select = request.form.get('stock-select')

    ticker = select
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NSE:' + ticker + '&apikey=S5R8PAYIH8YYCJAU&datatype=csv'
    #url2 = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=MSFT&outputsize=full&apikey=demo'
    urllib.request.urlretrieve(url, 'dataset1.csv')




    #x, y = np.loadtxt('dataset1.csv', delimiter=',', unpack=True)
    #plt.plot(x,y, label='Sample Graph')

    dataset=pd.read_csv('dataset1.csv')
    X=dataset.iloc[1:,4].values
    Y=dataset.iloc[:dataset.shape[0]-1,1].values

    X=X.reshape(1,-1)
    Y=Y.reshape(1,-1)
    from sklearn.linear_model import LinearRegression
    regressor=LinearRegression()
    regressor.fit(X,Y)

    y_pred=regressor.predict(X[0].reshape(1,-1))

    plt.scatter(X, Y,color='red')
    plt.plot(X, Y,color='blue',linewidth=2)




    plt.savefig('static/images/new_plot.png')




    #dataset1=pd.read_csv("dataset2.json")
    #dataset1=pd.read_csv("dataset.csv")

    return render_template('plot.html', name = 'new_plot', url ='/static/images/new_plot.png')

if __name__=='__main__':
    app.run(debug=True)
