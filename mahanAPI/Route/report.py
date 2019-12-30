from flask import request
import sys,os
sys.path.insert(0,os.path.abspath('..'))
from data.DataAccess import DataAccess
from model.report import Report
from config.Config import *
from flask import jsonify

@app.route('/report/read',methods=['POST','GET'])
def read():
    data=DataAccess.fetch_all('select * from report',[])
    return jsonify([Report(*a)  for a in data])
@app.route('/report/create',methods=['POST','GET'])
def create():
    DataAccess.execute('insert into report(Type,text,pilot_id) values (?,?,?)',
    [request.form['Type'],request.form['text'],request.form['pilot_id']])
    return jsonify({'status':'done'})
@app.route('/report/delete',methods=['POST','GET'])
def delete():
    DataAccess.execute('delete from report where id=?',[request.form['id']])
    return jsonify({'status':'done'})
