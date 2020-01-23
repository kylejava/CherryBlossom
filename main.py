import os
from flask import Flask, render_template, flash, request
from models import *


app = Flask(__name__)


# Flask can respond differently to various HTTP methods



# For render_template pass in name of template and any variables needed
@app.route('/' , methods = ['GET' ,'POST'])
def search():
    error = " "
    if(request.method == 'POST'):
        anime =request.form['anime']
        #return redirect(url_for('result', anime =anime))

    return render_template('index.html',error = error)


@app.route('/result' , methods=['GET', 'POST'])
def result():
    user_anime = request.args.get('anime' , None)
    user_anime = verify(user_anime)
    if('None' in user_anime):
        error = "Please enter another search"
        return render_template('index.html',error = error)
    user_ani = ((user_anime['data']['Media']['title']['english']))
    print(user_ani)
    ani = {}
    ani = find(user_ani)
    anime_name = ani['name']

    return render_template('result.html' , anime_name = anime_name)


if __name__ == "__main__":
    app.run(debug=True)
