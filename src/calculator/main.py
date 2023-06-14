import flask

app = flask.Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return flask.render_template('form.html')
#testing

@app.route('/result', methods=['POST'])
def result():
    var_1 = flask.request.form.get("var_1", type=int)
    var_2 = flask.request.form.get("var_2", type=int)
    operation = flask.request.form.get("operation")
    if(operation == 'Addition'):
        result = var_1 + var_2
    elif(operation == 'Subtraction'):
        result = var_1 - var_2
    elif(operation == 'Multiplication'):
        result = var_1 * var_2
    elif(operation == 'Division'):
        result = var_1 / var_2
    else:
        result = 'INVALID CHOICE'
    entry = result
    return flask.render_template('result.html', entry=entry)

if __name__ == '__main__':
    app.run(debug=True)
