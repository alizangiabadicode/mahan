from flask import request
import sys,os
sys.path.insert(0,os.path.abspath('..'))
from data.DataAccess import DataAccess
from model.airplane import airplane
from config.Config import *
from flask import jsonify

@app.route('/airplane/read',methods=['POST','GET'])
def read():
    data=DataAccess.fetch_all('select * from airplane',[])
    return jsonify([airplane(*a).serialize()  for a in data])

@app.route('/airplane/create',methods=['POST','GET'])
def create():
    DataAccess.execute('insert into airplane(total_flight_time,eng,name,reg_code,total_block_time,first_chair_no,sec_chair_no,eco_chair_no,eq) values (?,?,?,?,?,?,?,?,?)',
    [request.form['total_flight_time'],request.form['eng'],request.form['name'],request.form['reg_code'],request.form['total_block_time'],request.form['first_chair_no'],request.form['sec_chair_no'],request.form['eco_chair_no'],request.form['eq']])
    return jsonify({'status':'done'})
@app.route('/airplane/delete',methods=['POST','GET'])
def delete():
    DataAccess.execute('delete from airplane where id=?',[request.form['id']])
    return jsonify({'status':'done'})