import sqlite3
from .models import erp15map
from .models import erpecus
from .models import erp15amap
from . import db
from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
import pandas as pd
import pymysql
from numpy import nan
import math
from sqlalchemy import create_engine

def exceltodb(filename):
    
    #opening excel file
    df = pd.DataFrame(pd.read_excel(f'D:\Flask-sql\excelFiles\{filename}.xlsx'))
 
    engine = create_engine('mysql://root:kapil@localhost/crud')

    df.to_sql(filename.lower(), con=engine, if_exists='replace', index=False) 
        
     
    print("updated succ")
    flash(f" {filename} file uploaded to database successfully")
    
views = Blueprint('views', __name__)


def deleteExcel(filename):
    conn = pymysql.connect(
    host='localhost',
    user='root',
    password = 'kapil',
    db='crud',)
    cur = conn.cursor()
     
    cur.execute(f"drop table {filename.lower()}")
        
    cur.close()
    # Commit the transaction
    conn.commit()
    # Close the database connection
    conn.close()
    print("updated succ")
    flash(f" {filename} table droped successfully")


@views.route("/")
def index():
    return render_template("excel.html")

@views.route("/excel1")
def excel1():    
    return render_template("excel.html")

@views.route('/addExcel',methods=['POST'])
def addExcel():
   if request.method == 'POST':
        filee=request.form['fileName']
        print(filee)
        exceltodb(filee)
        return render_template("excel.html")

@views.route('/ExcelDel',methods=['POST'])
def ExcelDel():
     if request.method == 'POST':
        filee=request.form['fileName']
        print(filee)
        deleteExcel(filee)
        return render_template("excel.html")

#-------------erp15map :: start--------------------------------------
@views.route("/showerp15map")
def showerp15map():
    all_data=erp15map.query.all()
    return render_template("index.html",data=all_data)

@views.route('/inserterp15map', methods=['POST'])
def inserterp15map():
     if request.method == 'POST':
        inOut=request.form['inOut']
        Type=request.form['Type']
        Flag=request.form['Flag']
        StockInQty=request.form['StockInQty']
        ReExported=request.form['ReExported']
        ChangeUsage=request.form['ChangeUsage']
        StockedOutFor=request.form['StockedOutFor']
        otherPurpose=request.form['otherPurpose']
        my_data=erp15map(inOut,Type,Flag,StockInQty,ReExported,ChangeUsage,StockedOutFor,otherPurpose)
        db.session.add(my_data)
        db.session.commit()
        flash("Data inserted in sucessfully!!")
        return redirect(url_for('views.showerp15map'))


@views.route('/updateerp15map',methods=['GET','POST'])
def updateerp15map():
    if request.method=='POST':
        try:
            my_data=erp15map.query.get(request.form.get('id'))
            my_data.inOut=request.form['inOut']
            my_data.Type=request.form['Type']
            my_data.Flag=request.form['Flag']
            my_data.StockInQty=request.form['StockInQty']
            my_data.ReExported=request.form['ReExported']
            my_data.ChangeUsage=request.form['ChangeUsage']
            my_data.StockedOutFor=request.form['StockedOutFor']
            my_data.otherPurpose=request.form['otherPurpose']
            db.session.commit()

            flash("Data updated in sucessfully!!")
            return redirect(url_for('views.showerp15map'))
        except:
            return "invalid data. Data is not updated"

@views.route('/deleteerp15map/<id>/',methods=['GET','POST'])
def deleteerp15map(id):
    my_data=erp15map.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Data deleted sucessfully!!")
    return redirect(url_for('views.showerp15map'))
#-------------erp15map :: end--------------------------------------



#------------------EPR ECUS :: start------------------------------
@views.route("/showerpecus")
def showerpecus():
    all_data=erpecus.query.all()
    return render_template("indextwo.html",data=all_data)


@views.route('/inserterpecus', methods=['POST'])
def inserterpecus():
     if request.method == 'POST':
        inOut=request.form['inOut']
        Type=request.form['Type']
        Flag=request.form['Flag']
        RequiredField=request.form['RequiredField']
        EpeCode=request.form['EpeCode']
        IfeCode=request.form['IfeCode']
        FpCode=request.form['FpCode']
        my_data=erpecus(inOut,Type,Flag,RequiredField,EpeCode,IfeCode,FpCode)
        db.session.add(my_data)
        db.session.commit()
        flash("Data inserted in sucessfully!!")
        return redirect(url_for('views.showerpecus'))


@views.route('/updateerpecus',methods=['GET','POST'])
def updateerpecus():
    if request.method=='POST':
        try:
            my_data=erpecus.query.get(request.form.get('id'))
            my_data.inOut=request.form['inOut']
            my_data.Type=request.form['Type']
            my_data.Flag=request.form['Flag']
            my_data.RequiredField=request.form['RequiredField']
            my_data.EpeCode=request.form['EpeCode']
            my_data.IfeCode=request.form['IfeCode']
            my_data.FpCode=request.form['FpCode']
            db.session.commit()

            flash("Data updated in sucessfully!!")
            return redirect(url_for('views.showerpecus'))
        except:
            return "invalid data. Data is not updated"

@views.route('/deleteerpecus/<id>/',methods=['GET','POST'])
def deleteerpecus(id):
    my_data=erpecus.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Data deleted sucessfully!!")
    return redirect(url_for('views.showerpecus'))

#------------------EPR ECUS :: end------------------------------



#-------------------erp15Amap :: start-------------------
@views.route("/showerp15amap")
def showerp15amap():
    all_data=erp15amap.query.all()
    return render_template("indexthree.html",data=all_data)

@views.route('/inserterp15amap', methods=['POST'])
def inserterp15amap():
     if request.method == 'POST':
        inOut=request.form['inOut']
        Type=request.form['Type']
        Flag=request.form['Flag']
        StockInQty=request.form['StockInQty']
        QtyOfProducts=request.form['QtyOfProducts']
        QtyOfExported=request.form['QtyOfExported']
        otherPurpose=request.form['otherPurpose']
        my_data=erp15amap(inOut,Type,Flag,StockInQty,QtyOfProducts,QtyOfExported,otherPurpose)
      
        db.session.add(my_data)
        db.session.commit()
        flash("Data inserted in sucessfully!!")
        return redirect(url_for('views.showerp15amap'))


@views.route('/updateerp15amap',methods=['GET','POST'])
def updateerp15amap():
    if request.method=='POST':
        try:
            my_data=erp15amap.query.get(request.form.get('id'))
            my_data.inOut=request.form['inOut']
            my_data.Type=request.form['Type']
            my_data.Flag=request.form['Flag']
            my_data.StockInQty=request.form['StockInQty']
            my_data.QtyOfProducts=request.form['QtyOfProducts']
            my_data.QtyOfExported=request.form['QtyOfExported']
            my_data.otherPurpose=request.form['otherPurpose']
            db.session.commit()

            flash("Data updated in sucessfully!!")
            return redirect(url_for('views.showerp15amap'))
        except:
            return "invalid data. Data is not updated"

@views.route('/deleteerp15amap/<id>/',methods=['GET','POST'])
def deleteerp15amap(id):
    my_data=erp15amap.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Data deleted sucessfully!!")
    return redirect(url_for('views.showerp15amap'))


#-------------------erp15Amap :: end-------------------


#-------------------query :: start------------------
@views.route('/query')
def query():
    return render_template("query.html")

def returnQueryResult(Query):
    conn = pymysql.connect(
    host='localhost',
    user='root',
    password = 'kapil',
    db='crud',)
    cur = conn.cursor()
    for i in Query:
        for j in i:
            cur.execute(j)
    field_names = [i[0] for i in cur.description]
    return_value = cur.fetchall()
    cur.close()
    # Commit the transaction
    conn.commit()
    # Close the database connection
    conn.close()
    return render_template("query.html",attribute=field_names,data=return_value)
    


@views.route('/executeQuery/<id>/')
def executeQuery(id):
    q1 =  ["""insert into testing2 values (33,33,33);""","""insert into testing2 values (77,77,77);""","""select * from testing2"""],
    q2 =  [""" """,""" """,""" """]
    q3 = [""" """,""" """,""" """]
    queries = []
    queries.append(q1)
    queries.append(q2)
    queries.append(q3)
    return (returnQueryResult(q1))

#-------------------query :: end------------------3
