from flask import request
import sys,os
sys.path.insert(0,os.path.abspath('..'))
from data.DataAccess import DataAccess
from model.flight_attendent import flight_attendent
from config.Config import *
from flask import jsonify

@app.route('/flight_attendent/read',methods=['POST','GET'])
def read():
    data=DataAccess.fetch_all('select * from flight_attendent',[])
    return jsonify([flight_attendent(*a)  for a in data])
@app.route('/flight_attendent/create',methods=['POST','GET'])
def create():
    DataAccess.execute('insert into flight_attendent(fname,lname,adr,nid,birthday,phone_number,type,post,medical_id) values (?,?,?,?,?,?,?,?,?)',
    [request.form['fname'],request.form['lname'],request.form['adr'],request.form['nid'],request.form['birthday'],request.form['phone_number'],request.form['type'],request.form['post'],request.form['medical_id']])
    return jsonify({'status':'done'})
@app.route('/flight_attendent/delete',methods=['POST','GET'])
def delete():
    DataAccess.execute('delete from flight_attendent where id=?',[request.form['id']])
    return jsonify({'status':'done'})
@app.route('/flight_attendent/update',methods=['POST','GET'])
def update():
    DataAccess.execute('update flight_attendent set fname=?,lname=?,adr=?,nid=?,birthday=?,phone_number=?,type=?,post=?,medical_id=? where id=?',
    [request.form['fname'],request.form['lname'],request.form['adr'],request.form['nid'],request.form['birthday'],request.form['phone_number'],request.form['type'],request.form['post'],request.form['medical_id'],request.form['id']])
    return jsonify({'status':'done'})