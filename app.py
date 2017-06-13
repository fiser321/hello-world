import requests,time
from flask import Flask
from flask import render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        r = requests.get("http://sso.jyall.com/common/randomImage?_t=0.6282324279843985&sid=0.7534077076139802")
        temp = ''
        if r.status_code == 200:
            temp = str(time.time())
            image_name = 'static/temp/' + temp + '.jpg'
            with open(image_name, "wb") as f:
                f.write(r.content)
        return render_template("index.html", file_name=image_name, name= temp)
    else:
        code1 = request.form['code1']
        code2 = request.form['code2']
        old_name = 'static/temp/' + str(code2) + '.jpg'
        new_name = 'static/real/' + code2 + "-" + str(code1) + '.jpg'
        with open(new_name, 'wb') as fw:
            with open(old_name, "rb") as fr:
                fw.write(fr.read())
        return redirect(url_for("index"))

if __name__ == "__main__":
    app.run()