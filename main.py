
from flask import Flask, render_template, flash, request
from models import find
app = Flask(__name__)


# Flask can respond differently to various HTTP methods




# For render_template pass in name of template and any variables needed
@app.route('/' , methods = ['GET' ,'POST'])
def search():
    user_ani =[]
    if(request.method == 'POST'):
        ani=request.form['getAnime']
        user_ani = find(ani)
    ani_gen = user_ani[0]
    ani_tags = user_ani[1][1]
    print(ani_tags)

    return render_template('index.html' ,ani_gen = ani_gen , ani_tags = ani_tags)


if __name__ == "__main__":
    app.run()
