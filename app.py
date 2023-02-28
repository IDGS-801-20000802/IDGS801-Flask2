
from flask import Flask,render_template
from flask import request
from collections import Counter
from flask import make_response
from flask import flash
from flask_wtf import CSRFProtect


import forms
import cajasDinamicas

app= Flask(__name__)

app.config['SECRET_KEY']="esta es tu clave privada"
csrf=CSRFProtect()

@app.route("/calcular", methods=['GET'])
def calcular():
    return render_template("calcular.html")

@app.route("/Traductor",methods=["GET","POST"])
def traductor():
    alum_form=forms.UserForm2(request.form)
    idiom_form=forms.idiomas(request.form)
    btn = request.form.get("Guardar")
    btn2= request.form.get("Buscar")
    if request.method=="POST" and 'Guardar' in request.form :
        if alum_form.validate():
            
            if btn=='Guardar':
                ing = request.form['ingles']
                esp = request.form['espanol']
                g=open('diccionario.txt', 'a')
                g.write(ing.lower() + ' ' + esp.lower() + '\n')
            
                return render_template("traductor.html",form=alum_form,form1=idiom_form)
    if request.method=="POST" and 'Buscar' in request.form:
        if idiom_form.validate():
            
            ingles=None
            espanol=None
            if btn2=='Buscar':
                idi=idiom_form.idioma.data
                lenguage=idiom_form.lenguage.data.lower()
                f=open('diccionario.txt','r')
                lineas=f.readlines()
                mensaje=''
                for linea in lineas:
                    ingles, espanol = linea.strip().lower().split(' ') 
                
                    if idi=='es':
                        if lenguage==ingles:
                            mensaje = f'la traduccion de "{ingles.upper()}" es "{espanol.upper()}".'
                            break 
                    elif idi=='in':
                        if lenguage==espanol:
                            mensaje = f'la traduccion de "{espanol.upper()}" es "{ingles.upper()}".'
                            break
                if not mensaje:
                    mensaje="No existe la palabra en el Diccionario"
                    f.close()
                return render_template("traductor.html",form=alum_form, form1=idiom_form, mensaje=mensaje)
                
    return render_template("traductor.html",form=alum_form ,form1=idiom_form)

@app.route("/cookie", methods=['GET','POST'])
def cookie():
    reg_user=forms.LoginForm(request.form)

    response=make_response(render_template('cookie.html', form=reg_user))
    if request.method == 'POST' and reg_user.validate():
        user=reg_user.username.data
        pasw=reg_user.password.data
        datos=user+"@"+pasw
        success_message='Bienvenido {}'.format(user)
        response.set_cookie('datos_user', datos)
        flash(success_message)
    response=make_response(render_template('cookie.html', form=reg_user))
        #print(user + ' '+ pasw)
    return response

@app.route("/Alumnos",methods=['GET','POST'])
def alumnos():
    reg_alum=forms.UserForm(request.form)
    mat=' '
    nom=' '
    if request.method == 'POST' and reg_alum.validate():
        mat=reg_alum.matricula.data
        nom=reg_alum.nombre.data
    return render_template ('Alumnos.html', form=reg_alum,mat=mat,nom=nom)

@app.route("/CajasDi", methods=['GET','POST'])
def CajasDi():
    reg_caja=cajasDinamicas.CajaForm(request.form)
    if request.method=='POST':
        btn = request.form.get("btn")
        if btn == 'Cargar':
            return render_template('CajasDinamicas.html',form=reg_caja)
        if btn == 'Datos':
            numero = request.form.getlist("numeros")
            max_value = None
            for num in numero:
                if (max_value is None or num > max_value):
                    max_value = num

            min_value = None
            for num in numero:
                if (min_value is None or num < min_value):
                    min_value = num

            for i in range(len(numero)):
                numero[i] = int(numero[i])


            prom = 0
            prom = sum(numero) / len(numero)

            counter = Counter(numero)
            resultados = counter.most_common()
            textoResultado = ''
            for r in resultados:
                textoResultado += '<p>El número {0} se repite {1}</p>'.format(r[0], r[1])
            return render_template('CajasDinamicas.html',form=reg_caja, max_value=max_value, min_value=min_value, prom=prom, repetidos = textoResultado)
    return render_template('CajasDinamicas.html', form=reg_caja)

if __name__=="__main__":
    #srf.init_app(app)
    app.run(debug=True,port=3000)























