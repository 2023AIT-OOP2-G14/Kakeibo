from flask import Flask, request, render_template
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


if __name__ == '__main__':
    app.run(debug=True)