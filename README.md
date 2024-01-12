# Kakeibo
自由課題　仕様

# 入力ページの仕様
- フォームでデータを処理する
- フォーム名　金額：使った金額 ID:amount
- フォーム名　カテゴリー:食費・趣味・交際・日用品・その他 ID:category
- フォーム名　日付:日付（inputタグでtypeをdate指定） 　ID:date
- 送信先URL:/input Method:POST

# カレンダーページ
- GETリクエストで特定の日にちの支出合計を取得
- パラメータ 日付データ:yyyy-mm-ddの形式で送信！
- GET先:/get_daily
- 帰ってくるデータ形式:指定日の支出合計

# グラフページ 
