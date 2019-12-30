from flask import request
import sys,os
sys.path.insert(0,os.path.abspath('..'))
from data.DataAccess import DataAccess
from model.pilot import pilot
from config.Config import *
from flask import jsonify

@app.route('/pilot/read',methods=['POST','GET'])
def read():
    data=DataAccess.fetch_all('select * from pilot',[])
    return jsonify([pilot(*a)  for a in data])
@app.route('/pilot/create',methods=['POST','GET'])
def create():
    DataAccess.execute('insert into pilot(fname,lname,adr,nid,birthday,phone_number,type,type_ex_date,flight_time,lice_no,ex_date,medical_id) values (?,?,?,?,?,?,?,?,?,?,?,?)',
    [request.form['fname'],request.form['lname'],request.form['adr'],request.form['nid'],request.form['birthday'],request.form['phone_number'],request.form['type'],request.form['type_ex_date'],request.form['flight_time'],request.form['lice_no'],request.form['ex_date'],request.form['medical_id']])
    return jsonify({'status':'done'})
@app.route('/pilot/delete',methods=['POST','GET'])
def delete():
    DataAccess.execute('delete from pilot where id=?',[request.form['id']])
    return jsonify({'status':'done'})
@app.route('/pilot/update',methods=['POST','GET'])
def update():
     DataAccess.execute('update pilot setfname=?,lname=?,adr=?,nid=?,birthday=?,phone_number=?,type=?,type_ex_date=?,flight_time=?,lice_no=?,ex_date=?,medical_id=?) where id=?',
    [request.form['fname'],request.form['lname'],request.form['adr'],request.form['nid'],request.form['birthday'],request.form['phone_number'],request.form['type'],request.form['type_ex_date'],request.form['flight_time'],request.form['lice_no'],request.form['ex_date'],request.form['medical_id'],request.form['id']])
    return jsonify({'status':'done'})