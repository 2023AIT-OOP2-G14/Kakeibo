from flask import Flask, request, render_template, jsonify
from modules import expenditure_data_manager
from modules.http_except import HttpException, BadRequest

app = Flask(__name__)

@app.errorhandler(HttpException)
def error_http_except(e):
    return jsonify({'message': e.message}), e.code

@app.route('/')
def index():
    return render_template('input.html')

@app.route('/input', methods=["POST"])
def expenses_add():

    # 追加するデータの取得
    amount = request.form.get('amount')
    category = request.form.get('category')
    date = request.form.get('date')
    # パラメータのNULLチェック HTMLで必ず入力されるようにするが直接URLを叩かれた場合のため
    if amount == '' or category == '' or date == '':
        raise BadRequest('400 Bad Request')
    # パラメータの型チェック
    match category:
        case "food" | "hobby" | "fare" | "necessities" | "other":
            # カテゴリーにマッチした値のため何もしない
            pass
        case _:
            raise BadRequest('400 Bad Request')
    
    print(amount, category, date)

    # データの追加
    expenditure_data_manager.add_data(amount, category, date)

    return jsonify({'message': 'OK'}), 200

if __name__ == '__main__':
    app.run(debug=True)