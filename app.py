from flask import Flask, request, render_template
from instapy import InstaPy

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World!"


@app.route('/home')
def main_form():
    return render_template('main_form.html')


@app.route('/home', methods=['POST'])
def add_post():
    default = request.form['default']
    if default == 'default' and not request.form['username'] and not request.form['password']:
        username = 'admin_support_99'
        password = 'admin123'
    else:
        username = request.form['username']
        password = request.form['password']
    target_username = request.form['target_username']
    print(f'username: {username}\npassword: {password}\ntarget username: {target_username}')
    run_script(username, password, target_username)
    return 'success'


def run_script(username, password, target_username):
    session = InstaPy(username=username, password=password, headless_browser=True)
    session.login()
    session.like_by_users([target_username], randomize=False, amount=10)


if __name__ == '__main__':
    app.run()
