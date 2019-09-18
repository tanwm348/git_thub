from flask import Flask
from flask_restful import reqparse
import hashlib

app =Flask(__name__)

def md5(str):
    md5 = hashlib.md5()
    md5.update(str.encode(encoding="utf8"))
    str_md5 = md5.hexdigest()
    return str_md5


@app.route('/login')#资源路径
def login():
    pwd ="123456"
    parser = reqparse.RequestParser()
    parser.add_argument("username",type=str,required=True)#入参,类型str 必填
    parser.add_argument("password",type=str,required=True)#入参,类型str 必填
    args = parser.parse_args()
    username = args.get("username")

    password = args.get("password")

    newpassword = md5(pwd)
    if username == "admin" and password == newpassword:
        return "login-pass"
    elif username != "admin" or password != newpassword:
        return "login-fail"
    else:
        return "登陆异常"


if __name__ == '__main__':
    print(md5("123456"))
    app.run(host='0.0.0.0',debug=True)
