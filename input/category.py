import curses

def display_categories(stdscr, selected_row):
    """カテゴリー一覧をドラムロールで表示する関数"""
    categories = ["食費", "趣味", "交際", "日用品", "その他"]
    stdscr.clear()

    # カテゴリー一覧を画面に表示
    for i, category in enumerate(categories):
        x = 2
        y = i + 1
        stdscr.addstr(y, x, f"{category}", curses.A_NORMAL)

    # 選択中のカテゴリーをハイライト表示
    stdscr.addstr(selected_row, 2, f"{selected_row}. {categories[selected_row - 1]}", curses.A_REVERSE)
    
    stdscr.refresh()

def select_category(stdscr):
    """カテゴリーをドラムロールで選択する関数"""
    current_row = 1

    while True:
        key = stdscr.getch()

        # キー入力による選択変更
        if key == curses.KEY_UP and current_row > 1:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < 5:
            current_row += 1
        elif key == 10:  # Enter キーで選択確定
            return current_row

        # カテゴリー一覧を表示
        display_categories(stdscr, current_row)

def main(stdscr):
    # curses 初期化
    curses.curs_set(0)  # カーソル非表示
    curses.cbreak()
    stdscr.keypad(1)

    # カテゴリーを選択
    selected_category_id = select_category(stdscr)

    # 終了処理
    stdscr.getch()
    curses.endwin()

if __name__ == "__main__":
    curses.wrapper(main)
