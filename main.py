from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def atividade():
    return render_template('atividade.html', msg='')

@app.route('/verificar')
def verificar():
    num = 5
    mensagem= ''
    while num <= 100:
        if num % 7 == 0 and num % 5 != 0:
            mensagem+=  ' - ' + str(num)
        num += 1
    return render_template('atividade.html', msg=mensagem)

if (__name__)     ==('__main__'):

    app.run(debug=True)