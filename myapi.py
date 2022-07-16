from flask import*
import sqlite3 as sql

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    con = sql.connect("web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from long1")
    data = cur.fetchall()
    return render_template("index.html", datas=data)


@app.route("/add_user", methods=['POST', 'GET'])
def add_user():
    if request.method == 'POST':
        uname = request.form['uname']
        contact = request.form['contact']
        con = sql.connect("web.db")
        cur = con.cursor()
        cur.execute("insert into long1(UNAME,CONTACT) values (?,?)", (uname, contact))
        con.commit()
        flash('User Added', 'success')
        return redirect(url_for("index"))
    return render_template("add_user.html")


@app.route("/edit_user/<string:uid>", methods=['POST', 'GET'])
def edit_user(uid):
    if request.method == 'POST':
        uname = request.form['uname']
        contact = request.form['contact']
        con = sql.connect("web.db")
        cur = con.cursor()
        cur.execute("update long1 set UNAME=?,CONTACT=? where UID=?", (uname, contact, uid))
        con.commit()
        flash('User Updated', 'success')
        return redirect(url_for("index"))
    con = sql.connect("web.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from long1 where UID=?", (uid,))
    data = cur.fetchone()
    return render_template("edit_user.html", datas=data)


@app.route("/delete_user/<string:uid>", methods=['GET'])
def delete_user(uid):
    con = sql.connect("web.db")
    cur = con.cursor()
    cur.execute("delete from long1 where UID=?", (uid,))
    con.commit()
    flash('User Deleted', 'warning')
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.secret_key = 'admin123'
    app.run(debug=True)