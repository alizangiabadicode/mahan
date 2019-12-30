from flask import request
import sys,os
sys.path.insert(0,os.path.abspath('..'))
from data.DataAccess import DataAccess
from model.fa_flight import fa_flight
from config.Config import *
from flask import jsonify

@app.route('/fa_flight/read',methods=['POST','GET'])
def read():
    data=DataAccess.fetch_all('select * from fa_flight',[])
    return jsonify([fa_flight(*a).serialize()  for a in data])

@app.route('/fa_flight/create',methods=['POST','GET'])
def create():
    DataAccess.execute('insert into fa_flight(flight_id,fa_id) values (?,?)',
    [request.form['flight_id'],request.form['fa_id']])
    return jsonify({'status':'done'})