from flask import Flask, render_template
from database import create_logs_table, get_connection

app=Flask(__name__)

create_logs_table()

@app.route("/")

def home():
    conn=get_connection()
    conn.execute("""
                 INSERT INTO logs(ip_address,endpoint,status_code,timestamp)
                 VALUES('192.168.1.10','/login',401,'2026-02-27 10:00:00')
                 """)
    conn.commit()
    logs=conn.execute("SELECT * from logs").fetchall()
    conn.close()

    return render_template("index.html",logs=logs)

if __name__ == "__main__":
    app.run(debug=True)