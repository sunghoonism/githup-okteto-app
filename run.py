from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

todos = {}

class TodoSimple(Resource):
    """
    You can try this example as follow:
        $ curl http://localhost:5000/todo1 -d "data=Remember the milk" -X PUT
        $ curl http://localhost:5000/todo1
        {"todo1": "Remember the milk"}
        $ curl http://localhost:5000/todo2 -d "data=Change my breakpads" -X PUT
        $ curl http://localhost:5000/todo2
        {"todo2": "Change my breakpads"}
    Or from python if you have requests :
     >>> from requests import put, get
     >>> put('http://localhost:5000/todo1', data={'data': 'Remember the milk'}).json
     {u'todo1': u'Remember the milk'}
     >>> get('http://localhost:5000/todo1').json
     {u'todo1': u'Remember the milk'}
     >>> put('http://localhost:5000/todo2', data={'data': 'Change my breakpads'}).json
     {u'todo2': u'Change my breakpads'}
     >>> get('http://localhost:5000/todo2').json
     {u'todo2': u'Change my breakpads'}
    """
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api.add_resource(TodoSimple, '/<string:todo_id>')


@app.route("/")
def hello():
    return 'Hello'
"""
@app.route('/webhook', methods=['POST'])
def webhook():
    if method=='POST':
        headers = {
        'Accept': 'application/vnd.tosslab.jandi-v2+json',
        'Content-Type': 'application/json'
        }
        #data = '{"body":"[[Naver]](http:naver.com) You have a new Pizza order.","connectColor":"#FAC11B","connectInfo":[{"title":"Topping","description":"Pepperoni"},\n{"title":"Location","description":"Empire State Building, 5th Ave, New York","imageUrl":"Url_to_text"}]}'
        print(request.form['text'])
        #print('POST!')
        data='{{"text":"{} {}"}}'.format(request.form['text'], request.form['text'])
        #data={'body':'I am from webhook'}
        requests.post('https://wh.jandi.com/connect-api/webhook/11495160/86d7ab45df200b89fdedb99158472833', headers=headers, data=data)
    else:
        return 'text'
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
