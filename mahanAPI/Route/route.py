from flask import request
import sys,os
sys.path.insert(0,os.path.abspath('..'))
from data.DataAccess import DataAccess
from model.route import Route
from config.Config import *
from flask import jsonify

@app.route('/route/read',methods=['POST','GET'])
def read():
    data=DataAccess.fetch_all('select * from route',[])
    return jsonify([Route(*a)  for a in data])
@app.route('/route/create',methods=['POST','GET'])
def create():
    DataAccess.execute('insert into route(Permission_no,Dep,Dest) values (?,?,?)',
    [request.form['Permission_no'],request.form['Dep'],request.form['Dest']])
    return jsonify({'status':'done'})
@app.route('/route/delete',methods=['POST','GET'])
def delete():
    DataAccess.execute('delete from route where id=?',[request.form['id']])
    return jsonify({'status':'done'})
