from flask import Flask
from flask_restful import reqparse
import pymysql

app = Flask(__name__)

@app.route('/')#资源路径
def hello_world():
    re='hello world'
    return re

@app.route('/select',methods=[('GET')])
def select():
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True)#id入参,类型int 必填
    args = parser.parse_args()
    re=args.get('name')

    sql1 = "select*from phpyun_ad where ad_name='%s'"%(re)
    se=sql(sql1)
    print(se)
    return str(se)


def sql(sql):
    con = pymysql.connect("localhost","root","",charset="utf8")
    cur = con.cursor()
    cur.execute("use phpyun")



    cur.execute(sql)
    re1=cur.fetchall()


    cur.close()
    con.close()
    return re1




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
