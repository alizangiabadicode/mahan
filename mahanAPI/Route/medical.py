from flask import request
import sys,os
sys.path.insert(0,os.path.abspath('..'))
from data.DataAccess import DataAccess
from model.medical import medical
from config.Config import *
from flask import jsonify

@app.route('/medical/read',methods=['POST','GET'])
def read():
    data=DataAccess.fetch_all('select * from medical',[])
    return jsonify([medical(*a)  for a in data])
@app.route('/medical/creat',methods=['POST','GET'])
def creat():
    DataAccess.execute('insert into medical(class,serial,dr,limit) values (?,?,?,?)',
    [request.form['class'],request.form['serial'],request.form['dr'],request.form['limit']])
    return jsonify({'status':'done'})
@app.route('/medical/delete',methods=['POST','GET'])
def delete():
    DataAccess.execute('delete from medical where id=?',[request.form['id']])
    return jsonify({'status':'done'})
@app.route('/medical/update',methods=['POST','GET'])
def update():
    DataAccess.execute('update medical set class=?,serial=?,dr=?,limit=? where id=?',
    [request.form['class'],request.form['serial'],request.form['dr'],request.form['limit'],request.form['id']])
    return jsonify({'status':'done'})