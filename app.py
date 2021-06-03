#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def nitin():
    return render_template('iphone.html')
@app.route('/info',methods=['GET','POST'])
def gkgkg():
    if(request.method=='POST'):
        n1=int(request.form['n'])
        n2=int(request.form['e'])
        total=n1+n2
        return render_template('iphone.html',answer=total)
if __name__=='__main__':
    app.run()

