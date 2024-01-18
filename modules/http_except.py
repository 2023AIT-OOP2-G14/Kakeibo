# FileName      : http_except.py
# Description   : HTTPの例外を定義するモジュールです。

class HttpException(Exception):
    code = 0
    message = ''
    def __init__(self, code, message):
        self.code = code
        self.message = message

# 500 Internal Server Error - サーバー内部でエラーが発生した場合に使用。
class ServerException(HttpException):
    def __init__(self, message):
        super().__init__(500, message)

# 418 I'm a teapot - サーバーがティーポットであることを示す場合に使用。処理したくないリクエストが来た時に使用しましょう！
class TeapotException(HttpException):
    def __init__(self, message):
        super().__init__(418, message)

# 401 Unauthorized - 認証が必要なリソースに対して認証を行わなかった場合に使用。
class UnauthorizedException(HttpException):
    def __init__(self, message):
        super().__init__(401, message)

# 400 Bad Request - クライアントから無効なリクエスト（パラメータ不足等）が送信された場合に使用。
class BadRequest(HttpException):
    def __init__(self, message):
        super().__init__(400, message)