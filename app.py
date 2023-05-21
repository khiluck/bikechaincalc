from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def calculate_chain_length():
    FC = int(request.form.get('FC'))
    CS = int(request.form.get('CS'))
    CL = int(request.form.get('CL'))
    X = int(request.form.get('X'))

    chain_length = FC/2 + CS/2 + CL/6.35 + X

    return 'Длина цепи в звеньях: {:.2f}'.format(chain_length)

if __name__ == '__main__':
    app.run(debug=True)
