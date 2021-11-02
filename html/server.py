from flask  import Flask, render_template, request
import pandas as pd
import Final_Base

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/days')
def days():
   return render_template('days.html')

@app.route('/months')
def months():
   return render_template('months.html')

@app.route('/province')
def province():
   return render_template('province.html')

@app.route('/months-table')
def months_table():
   df = pd.read_csv('static/tables/months.csv')
   return render_template('months_table.html', df=df)

@app.route('/days-table')
def days_table():
   df = pd.read_csv('static/tables/days.csv')
   return render_template('days_table.html', df=df)

@app.route('/province-table')
def province_table():
   df = pd.read_csv('static/tables/province.csv')
   return render_template('province_table.html', df=df)

@app.route('/coba')
def coba():
   return render_template('coba.html')

if __name__ == '__main__':
    app.run()