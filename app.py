from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/pokemon/<username>')
def show_user_profile(username):

    url = 'http://pokeapi.co/api/v2/pokemon/' + username +'/'
    
    r = requests.get(url)

    u = r.json()['id']

    return '<h1> The pokemon with name {0} has id {1}</h1>'.format(username, u)

@app.route('/pokemon/<int:post_id>')
def show_post(post_id):

    url = 'http://pokeapi.co/api/v2/pokemon/' + str(post_id) +'/'

    r = requests.get(url)

    u = r.json()['name']

    return '<h1>The pokemon with id {0} is {1}</h1>'.format(post_id, u)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
