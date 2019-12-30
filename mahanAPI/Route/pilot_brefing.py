from flask import request
import sys,os
sys.path.insert(0,os.path.abspath('..'))
from data.DataAccess import DataAccess
from model.pilot_brefing import pilot_brefing
from config.Config import *
from flask import jsonify

@app.route('/pilot_brefing/read',methods=['POST','GET'])
def read():
    data=DataAccess.fetch_all('select * from filght_brefing',[])
    return jsonify([pilot_brefing(*a)  for a in data])
@app.route('/pilot_brefing/create',methods=['POST','GET'])
def create():
    DataAccess.execute('insert into pilot_brefing(wether,chart,pilot_id,dispather_id) values (?,?,?,?)',
    [request.form[''],request.form[''],request.form[''],request.form['']])
    return jsonify({'status':'done'})
@app.route('/pilot_brefing/delete',methods=['POST','GET'])
def delete():
    DataAccess.execute('delete from pilot_brefing where id=?',[request.form['id']])
    return jsonify({'status':'done'})
