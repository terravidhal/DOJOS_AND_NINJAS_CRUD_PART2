from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja



@app.route("/")
def home():
    return redirect('/dojos')


@app.route("/dojos")
def dojos_home():
    all_dojos = Dojo.get_all_dojos()
    print(all_dojos)
    return render_template("dojos.html", dojos = all_dojos)



@app.route("/create_dojo", methods=['POST'])
def create_dojo_func(): 
    data = {
        "name": request.form["Name"],
    }
    Dojo.create_dojo(data) 
    return redirect('/dojos')


@app.route("/dojos/<int:dojo_id>")
def dojo_show_func(dojo_id):

    data = {
        "dojo_id" : dojo_id
    }

    ninjas = Ninja.get_ninjas_specific_dojo(data)
    # print('ninjas++++', ninjas)
   
    one_dojo = Dojo.get_specific_dojo(data)

    return render_template("dojo_show.html", all_ninjas = ninjas, one_dojo = one_dojo, dojo_id= dojo_id)