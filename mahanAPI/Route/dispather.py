from flask import request
import sys,os
sys.path.insert(0,os.path.abspath('..'))
from data.DataAccess import DataAccess
from model.dispather import dispather
from config.Config import *
from flask import jsonify

@app.route('/dispather/read',methods=['POST','GET'])
def read():
    data=DataAccess.fetch_all('select * from dispatcher',[])
    return jsonify([dispather(*a)  for a in data])
@app.route('/dispather/create',methods=['POST','GET'])
def create():
    DataAccess.execute('insert into dispatcher(fname,lname,adr,nid,birthday,phone_number,lic_no,ex_date) values (?,?,?,?,?,?,?,?)',
    [request.form['fname'],request.form['lname'],request.form['adr'],request.form['nid'],request.form['birthday'],request.form['phone_number'],request.form['lic_no'],request.form['ex_date']])
    return jsonify({'status':'done'})
@app.route('/dispather/delete',methods=['POST','GET'])
def delete():
    DataAccess.execute('delete from dispatcher where id=?',[request.form['id']])
    return jsonify({'status':'done'})
