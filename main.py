import os
from flask import Flask, render_template, flash, request
from models import *
from search import *   

app = Flask(__name__)


# Flask can respond differently to various HTTP methods



# For render_template pass in name of template and any variables needed
@app.route('/' , methods = ['GET' ,'POST'])
def search():

    if(request.method == 'POST'):
        anime =request.form['anime']
        #return redirect(url_for('result', anime =anime))

    return render_template('index.html')


@app.route('/result' , methods=['GET', 'POST'])
def result():
    anime = request.args.get('anime' , None)
    print(anime)
    return render_template('result.html' , anime = anime)


if __name__ == "__main__":
    app.run(debug=True)
