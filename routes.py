from ntpath import join
from os import path
from flask import flash, render_template, redirect, url_for, request, session
from ext import app, db
from forms import AddProduct, EditProductForm
from werkzeug.utils import secure_filename
from models import Product

SECRET_PASSWORD = "g4113ry"



@app.route('/', methods=['POST', 'GET'])
def home():
    form = AddProduct()

    products = Product.query.limit(12).all()
    return render_template("index.html", form=form, products=products)


@app.route('/editproduct/<int:index>', methods=['POST', 'GET'])
def edit_product(index):
    product = Product.query.get(index)

    if product:
        form = EditProductForm()
        if form.validate_on_submit():
            product.name = form.name.data

            if form.img.data:
                filename = secure_filename(form.img.data.filename)
                product.img = filename

                file_dir = join(app.root_path, "static", filename)
                form.img.data.save(file_dir)

            db.session.commit()
            return redirect("/admindashboard")

        form.name.data = product.name

        return render_template('adminpanel.html', form=form)
    else:
        return redirect('/admindashboard')
        

@app.route('/removeproduct/<int:index>', methods=['POST', 'DELETE'])
def remove_product(index):
    product = Product.query.get(index)

    if product:
        product.delete()
    else:
        flash('You do not have permission to access the admin dashboard.', 'danger')

    return redirect("/admindashboard")


@app.route('/admindashboard', methods=['POST', 'GET'])
def admindashboard():
    if request.method == 'POST' and request.form.get('password') == SECRET_PASSWORD:
        session['admin_access'] = True

    if session.get('admin_access'):
        form = AddProduct()
        products = Product.query.all()
        
        if form.validate_on_submit():
            new_product = Product(name=form.name.data, img=form.img.data.filename)
            new_product.create()

            filename = secure_filename(form.img.data.filename)
            file_dir = path.join(app.root_path, "static", filename)
            form.img.data.save(file_dir)
            
            return redirect("/admindashboard")
            
        return render_template('adminpanel.html', form=form, products=products)
    else:
        return render_template('password_form.html')




@app.route('/logout')
def logout():
    session.pop('admin_access', None)
    return redirect(url_for('admindashboard'))