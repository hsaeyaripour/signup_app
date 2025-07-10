from flask import Flask, request, render_template
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host='db',
        database='signupdb',
        user='signupuser',
        password='signuppass'
    )

@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO users (name, email) VALUES (%s, %s);', (name, email))
        conn.commit()
        cur.close()
        conn.close()
        return 'ثبت‌نام با موفقیت انجام شد!'
    return render_template('form.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
