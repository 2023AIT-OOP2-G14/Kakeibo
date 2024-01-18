import pathlib
import json
from collections import defaultdict
from datetime import datetime

file_path = './modules/balance_of_account.json'
file_path_obj = pathlib.Path(file_path)

def get_graph_data(date):
    """
    指定された日付の各カテゴリーに対する支出データを取得します。

    Parameters
    ----------
    date : str
        検索する日付。形式は 'YYYY-MM-DD' です。

    Returns
    -------
    dict
        各カテゴリーの支出総額を含む辞書。カテゴリーが存在しない場合は 'その他' として集計します。

    """
    if not file_path_obj.exists():
        return {}
    
    with open(file_path, 'r') as json_open:
        j = json.load(json_open)

    result_dict = defaultdict(int)
    category_list = ['食費', '外食費', '日用品', '交通費', '衣服', '交際費', '趣味']

    search_date = datetime.strptime(date, '%Y-%m-%d').date()

    for entry in j:
        entry_date = datetime.strptime(entry["date"], '%Y-%m-%d').date()
        if entry_date.year == search_date.year and entry_date.month == search_date.month:
            category = entry["category"] if entry["category"] in category_list else "その他"
            result_dict[category] += entry["amount"]

    return dict(result_dict)

def add_data(amount, category, date):
    """
    金額、カテゴリ、日付を受け取り、それらをJSONデータとして追加します。

    Parameters
    ----------
    amount : int
        追加する経費の金額。
    category : str
        経費のカテゴリ。
    date : str
        経費が発生した日付。形式は 'YYYY-MM-DD'。

    Returns
    -------
    None
    """
    print(amount, category, date)
    _add_json_data(amount, category, date)

def _add_json_data(amount, category, date):
    """
    金額、カテゴリ、日付を受け取り、それらをJSONデータとして追加します。

    Parameters
    ----------
    amount : int
        追加する経費の金額。
    category : str
        経費のカテゴリ。
    date : str
        経費が発生した日付。形式は 'YYYY-MM-DD'。

    Returns
    -------
    None

    Notes
    -----
    この関数は、指定されたファイルパスが存在しない場合、新しいJSONファイルを作成します。
    ファイルが既に存在する場合は、新しいデータを既存のJSONデータに追加します。
    """
    amount = int(amount)
    new_data = {
        'amount': amount,
        'category': category,
        'date': date
    }

    if not file_path_obj.exists():
        _create_json_file()
        save_data = [new_data]
    else:
        with open(file_path, 'r') as json_open:
            json_load = json.load(json_open)
        json_load.append(new_data)
        save_data = json_load

    with open(file_path, 'w') as f:
        json.dump(save_data, f, indent=4, ensure_ascii=False)

def _create_json_file():
    """
    JSONファイルを作成します。

    Returns
    -------
    None

    Notes
    -----
    この関数は、指定されたパスにJSONファイルを作成します。
    ファイルが既に存在する場合は、新しいファイルは作成されません。
    """
    file_path_obj.touch()

if __name__ == '__main__':
    add_data(500, '衣服', '2020-01-01')