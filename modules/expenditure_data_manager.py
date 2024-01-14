import pathlib
import json

file_path = './modules/balance_of_account.json'
file_path_obj = pathlib.Path(file_path)

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
    amount : float
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
