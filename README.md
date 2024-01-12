# Kakeibo
自由課題　仕様

# 入力ページの仕様
- フォームでデータを処理する
- 金額　使った金額を入力 inputタグ　type="number" name="number"
- カテゴリー 食費・趣味・交際・日用品・その他 selectタグ optionのvalue値 food/hobby/fare/necessities/other
- 日付　日付を指定 inputタグ type="date" 　name="date"
- 送信先URL:/input Method:POST

# カレンダーページ
- GETリクエストで特定の日にちの支出合計を取得
- パラメータ 日付データ:yyyy-mm-ddの形式で送信
- GET先:/get_daily
- 帰ってくるデータ形式:指定日の支出合計

# グラフページ 
