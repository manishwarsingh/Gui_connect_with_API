from flask import Flask, render_template,flash, redirect, request,jsonify,abort,url_for
import sqlite3 as sql
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
app = Flask(__name__,template_folder='temp')
app.secret_key="foreteens.com"

@app.route('/')
def new_slots():
   flash( "hello world!!")
   return render_template('home.html')

@app.route('/foretees',methods = ['POST', 'GET'])
def foretees():
   error=None
   if request.method == 'POST':
      try:
         w_day = request.form['w_day']
         stime = request.form['stime']
         # person = request.form['person']
         
         with sql.connect("database.db") as con:
            cur = con.cursor()
            cur.execute("select * from Foretees WHERE day='Monday'")
            data = cur.fetchone()
            print(data)
            cur.execute("INSERT INTO Foretees (day,stime) VALUES (?,?)" ,(w_day,stime))
            con.commit()
            cur.close()
            flash ("Record successfully added")
            return redirect(url_for('list'))
      except:
         con.rollback()
         error = "This Day is Already Exists , Try Again"
         return render_template("home.html",error=error)
         
         

@app.route('/list')
def list():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from Foretees")
   
   rows = cur.fetchall()
   print(rows)
   return render_template("list.html",rows = rows)

@app.route('/api/slots')
def api():
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   cur.execute("select * from Foretees")
   rows = cur.fetchall()
   
   data = {}
   # print(data)
   for row in rows:
      new_date =  datetime.strptime(row[1], '%Y-%m-%d').strftime('%m/%d/%Y')
      data[new_date] = {"time":row[2].split(",")}
      # new_date= .strptime(row[1], '%Y-%m-%d') strftime(data[row[1]],"%m/%d/%Y")], {"time":row[2]}
   return jsonify(data)

def get_post(post_id):
   con = sql.connect('database.db')
   con.row_factory=sql.Row
   cur=con.cursor()
   post = cur.execute('SELECT * FROM Foretees WHERE id = ?', (post_id,)).fetchone()
   cur.close()
   if post is None:
      abort(404)
   return post


@app.route("/<int:id>/edit/",methods=["POST","GET"])
def edit(id):
   print("ID:", id)
   post = get_post(id)
   print(post, request.method)


   if request.method == 'POST':
      w_day = request.form['w_day']
      stime = request.form['stime']
      # person = request.form['person']

      if not w_day:
         flash("w_day is required!")

      elif not stime:
         flash("stime is required!")

      # elif not person:
      #    flash("person is required!")

      else:
         print("else_frame start")
         con = sql.connect('database1.db')
         con.row_factory=sql.Row
         cur=con.cursor()
         cur.execute('UPDATE Foretees SET day = ?, stime = ?'
                      ' WHERE id = ?',
                      (w_day, stime, id))
         rows = cur.fetchall()
         print("Rowas",rows)
         con.commit()
         cur.close()
         flash("Record update successfully")
         return redirect(url_for('list',rows=rows))

   return render_template('edit.html',post=post)

@app.route("/<int:id>/delete/",methods=['POST','GET'])
def delete(id):
   print('ID:-',id)
   
   con = sql.connect("database.db")
   con.row_factory = sql.Row
   cur = con.cursor()
   sqls = """ DELETE FROM Foretees WHERE id=? """
   cur.execute(sqls, (id,))
   con.commit()
   cur.close()
   flash("Recod Delete successfully..")
   # flash('"{}" was successfully deleted!')
   return redirect(url_for('list'))

if __name__ == "__main__":
   app.run(debug=True)    
