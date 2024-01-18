from flask import Flask, request, render_template
import random # ランダムデータ作成のためのライブラリ
import json # json扱うためのライブラリ
import sqlite3 # データベース操作用のライブラリ
from traceback import format_exception_only # 例外処理用のライブラリ

# データベース名定義
dbname = 'data.db'

app = Flask(__name__)

# 1. 家計簿アプリのトップページ（入力画面をトップとする）
@app.route('/')
def index():
    return render_template('input.html')

# 入力画面のフォーム処理用
# パラメーター
# - amount: 金額
# - category: カテゴリー
# - date: 日付 yyyy-mm-dd形式を想定
@app.route('/input', methods=["POST"])
def input_data():
    # パラメーターを取得
    amount = request.form['amount']
    category = request.form['category']
    date = request.form['date']
    # パラメータのNULLチェック HTMLで必ず入力されるようにするが一応チェック
    if amount == '' or category == '' or date == '':
        return json.dumps({'status': 'NG'})
    # パラメータの型チェック
    match category:
        case "food" | "hobby" | "fare" | "necessities" | "other":
            # カテゴリーにマッチした値のため何もしない
            pass
        case _:
            return json.dumps({'status': 'NG'})
    # データベース保存処理
    if not write_db(amount, category, date):
        return json.dumps({'status': 'NG'})
    # レスポンスを返す
    return json.dumps({'status': 'OK'})

# データ取得用
# - type: 取得データのタイプ（daily, monthly, year）
# - date: 日付（yyyy-mm-dd形式）
@app.route('/get_daily', methods=["GET"])
def get_daily_data():
    # パラメーターを取得 yyyy-mm-dd形式で来る
    date = request.args.get('date', None)
    
    # 合計を数値で返す

    pass

# グラフ画面用（月別の支出・収入を取得）
# パラメーター 
@app.route('/get_monthly', methods=["GET"])
def get_monthly_data():
    
    pass

def write_db(amount:int, category:str, date:str):
    # データベース接続
    conn = sqlite3.connect(dbname)
    # データベース保存処理
    c = conn.cursor()
    try:
        # データを追加
        c.execute('INSERT OR IGNORE INTO data VALUES (?,?,?)', (amount, category, date))
        conn.commit()
    except KeyboardInterrupt as e:
        conn.rollback()
        print("KeyboardInterrupt")
        return False
    except Exception as e:
        print(format_exception_only(type(e), e))
        conn.rollback()
        return False
    finally:
        c.close()
        conn.close()
    return True

if __name__ == '__main__':
    # データベース初期化
    conn = sqlite3.connect(dbname)
    c = conn.cursor()
    try:
        print("データベース初期化")
        # テーブル作成　なければ新規作成
        # ---------------------------------------
        # テーブル名：data
        #  金額(name->amount type->INTEGER)
        #  カテゴリー(name->category type->INTEGER)
        #  日付(name->date type->TEXT)
        # ---------------------------------------
        c.execute('''
            CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            amount INTEGER,
            category INTEGER,
            date TEXT)
            ''')
        conn.commit()
    except KeyboardInterrupt as e:
        conn.rollback()
    except Exception as e:
        print(format_exception_only(type(e), e))
        conn.rollback()
    finally:
        c.close()
        conn.close()
    # 起動
    app.run()