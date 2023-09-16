from flask import render_template, request, redirect
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja


@app.route("/ninjas")
def create_ninja():
    dojos = Dojo.get_all_dojos()
    return render_template("ninja.html", all_dojos = dojos)



@app.route("/new_ninja", methods=['POST'])
def create_ninja_func():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_list"]
    }

    Ninja.create_ninja(data)

    return redirect(f'/dojos/{request.form["dojo_list"]}')


@app.route('/ninja/update/<int:ninja_id>')
def show_page_update_ninja(ninja_id):
    data = {'ninja_id': ninja_id}

    ninja_obj_update = Ninja.get_specific_ninja(data)
    return render_template("update_ninja.html", Ninja = ninja_obj_update)


@app.route('/edit/<int:ninja_id>',methods=['POST'])
def update_ninja_func(ninja_id):
    data = {
        "fname" : request.form["NewFirstName"],
        "lname" : request.form["NewLastName"],
        "age" : request.form["NewAge"],
        'ninja_id': ninja_id
    }
    dojoId = request.form["dojoId"]
    Ninja.update_ninja(data)
    return redirect(f'/dojos/{dojoId}')


@app.route('/ninja/delete/<int:ninja_id>/dojo/<int:dojo_id>')
def delete(ninja_id, dojo_id):
    data = {"ninja_id": ninja_id}
    dojoId = dojo_id
    Ninja.delete_ninja(data)
    return redirect(f'/dojos/{dojoId}')