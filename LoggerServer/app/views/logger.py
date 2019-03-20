from flask_cors import CORS
from flask import jsonify, Blueprint, make_response, request

blue=Blueprint('blueprint',__name__)

@blue.route('/')
def query_all():
    return jsonify({'code':10001,
                    'msg':'未授权'})

@blue.route('/upload_log/',methods=['POST','PUT'])
def upload_log():

    print(request.form)  #post上传表单数据
    print(request.args)  #get请求参数查询

    #获取
    json_data=request.get_json()
    print(json_data,type(json_data))

    #获取上传的文件数据
    print(request.files)

    resp=make_response(jsonify({'code':7000,'msg':'ok'}))
    resp.headers['refrer']='no referer'  #跨域请求中的引用来源

    return resp
