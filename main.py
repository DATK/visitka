from flask import Flask,render_template,request,redirect,abort
from src.SQL import Otsovik

app=Flask(__name__)

@app.route("/")
def redir2():
    return redirect("/main")

@app.route("/<path:n>")
def redir(n):
    return redirect("/main")




@app.route("/main",methods=["POST","GET"])
def main():
    otsovik=Otsovik()
    data=otsovik.get()
    if request.method=="POST":
        ots=request.form
        name=ots["name"]
        otsiv=ots["text"]
        if len(otsiv)>80:
            return redirect("/error_LongOtsiv")
        if len(name)>15:
            return redirect("/error_LongName")
        if name=="admin" and otsiv=="clsDB":
            otsovik.delete()
            return redirect("/visitka.html")
        otsovik.add(name,otsiv)
        return redirect("/main")
    
    elif request.method=="GET":
        return render_template("visitka.html",data=data)
    

@app.route("/error_<ERROR>")
def err(ERROR):
    if request.method=="GET":
        return render_template("errors.html",data=ERROR)


app.run(debug=True)