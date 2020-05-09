from flask import Flask,render_template,request,g
from panels import func
app = Flask(__name__)
@app.route("/",methods=['POST','GET'])
def hello():
    # path='testcases/30.jpg'
    # energy=func(path)
    return render_template('index.html')
@app.route('/result',methods=['POST','GET'])
def result():
    if request.method=='POST':
        path=request.form['imagepath']
        cost=request.form['avg']
        manual = request.form['area']
        energy=func(path)
        amount=int(energy)*float(cost)
        return render_template('result.html',result=energy,savings=amount)


    
app.run(debug=True)
