from flask import Flask, request, redirect, render_template, abort

app = Flask(__name__)
a = [{'name': 'Alex', 'id': 1, 'surname': 'Turner', 'age': 33},
    {'name': 'Thom', 'id': 2, 'surname': 'Yorke', 'age': 50},
    {'name': 'Jane', 'id': 3, 'surname': 'Porter', 'age': 17}]

@app.route('/users')
def print_them_all():
    b = ''
    for i in range(len(a)):
        print(a[i]['name'],a[i]['surname'])
        b = b + a[i]['name'] + ' ' + a[i]['surname'] + '<br>'
    ##return
    return render_template('all users.html', a=a)

@app.route('/user/<id>')
def find_his_id(id):
    id = int(id)
    for i in range(len(a)):
        if a[i]['id'] == id:
            return render_template('any user.html', user=a[i])
    abort(404)

@app.route('/')
def users():
    return redirect('/users')

@app.route('/home')
def home():
    return redirect('/')

if __name__ == '__main__':
    app.run()