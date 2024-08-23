
from flask import Flask, render_template, request

import sqlite3
import pickle

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Contact Us',methods=["GET","POST"])
def contactus():
    if request.method == "POST" :
        fname = request.form.get("fullname")
        pno = request.form.get("phone")
        email = request.form.get("email")
        message = request.form.get("message")
        conn= sqlite3.connect("ytdatabase.db")
        cur = conn.cursor(f'''INSERT INTO CONTACT VALUE("{fname}","{pno}","{email}","{message}")
                          ''')
        conn.commit()
        return render_template('message.html')
    else :
        return render_template('contactus.html')

@app.route('/YouTube Analytics')
def analytics():
    return render_template('analytics.html')

@app.route('/predictor',methods=['GET','POST'])
def likepredict():
    if request.method == 'POST':
        views = request.form.get('views')
        dislike = request.form.get('dislikes')
        comment = request.form.get('commentCount')
        genre = request.form.get('genre')
        print(views,dislike,comment,genre)
        with open("model.pickle",'rb') as mod :
            model = pickle.load(mod)
        pred = model.predict([[float(views),float(dislike),float(comment),float(genre)]])
        return render_template('result.html',pred=str(round(pred[0])))

    else:
        return render_template("likepredict.html")




if __name__ == '__main__':
    app.run(host = '0.0.0.0',port=5000)




