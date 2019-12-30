from flask import request
import sys,os
sys.path.insert(0,os.path.abspath('..'))
from data.DataAccess import DataAccess
from model.flight import flight
from config.Config import *
from flask import jsonify

@app.route('/flight/read',methods=['POST','GET'])
def read():
    data=DataAccess.fetch_all('select * from flight',[])
    return jsonify([flight(*a)  for a in data])
@app.route('/flight/create',methods=['POST','GET'])
def create():
    DataAccess.execute('insert into flight(flight_no,date,block_in,block_out,pax_no,take_off,landing,captian,fo,so) values (?,?,?,?,?,?,?,?,?,?)',
    [request.form['flight_no'],[request.form['date'],[request.form['block_in'],[request.form['block_out'],[request.form['pax_no'],[request.form['take_off'],[request.form['landing'],[request.form['captian'],[request.form['fo'],[request.form['so']])
    return jsonify({'status':'done'})
@app.route('/flight/delete',methods=['POST','GET'])
def delete():
    DataAccess.execute('delete from flight where id=?',[request.form['id']])
    return jsonify({'status':'done'})
@app.route('/flight/update',methods=['POST','GET'])
def update():
    DataAccess.execute('update flightset flight_no=?,date,block_in=?,block_out=?,pax_no=?,take_off=?,landing=?,captian=?,fo=?,so=?) where id=?',
    [request.form['flight_no'],[request.form['date'],[request.form['block_in'],[request.form['block_out'],[request.form['pax_no'],[request.form['take_off'],[request.form['landing'],[request.form['captian'],[request.form['fo'],[request.form['so'],[request.form['id']])
    return jsonify({'status':'done'})