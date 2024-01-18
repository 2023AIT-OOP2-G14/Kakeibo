from flask import Flask, request, render_template, jsonify
from datetime import datetime
from modules import expenditure_data_manager

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('input.html')

@app.route('/input', methods=["POST"])
def expenses_add():

    # 追加するデータの取得
    amount = request.form.get('amount')
    category = request.form.get('category')
    date = request.form.get('date')

    print(amount, category, date)

    # データの追加
    expenditure_data_manager.add_data(amount, category, date)

    return render_template('input.html')

@app.route('/graph')
def graph():
    return render_template('graph.html')

@app.route('/graph/data', methods=['GET', 'POST'])
def get_data():
    received_data = request.data.decode('utf-8')

    if received_data == '[object Event]':
        date = datetime.now().strftime('%Y-%m-%d')
    else:
        date = received_data

    data =  expenditure_data_manager.get_graph_data(date)
    if not data:
        data = {}
    #print(data)
    return jsonify(data)

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

if __name__ == '__main__':
    app.run(debug=True)