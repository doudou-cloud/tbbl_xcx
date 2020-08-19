from flask import jsonify
from flask_restful import Resource,reqparse

session_parser = reqparse.RequestParser()

session_parser.add_argument('token',type=str,location = ['cookies'])
session_parser.add_argument('phone',type=str,location = ['json'])
session_parser.add_argument('pwd',type=str,location = ['json'])


user_dic = {}
class SessionsResource(Resource):
    #登录
    def post(self):
        """
            小程序用户登录
            ---
            tags:
              - 登录
            parameters:
              - name: 登录body
                in: body
                type: dict
                description: 学生登录用参数
                schema:
                  properties:
                    phone:
                      required: False
                      type: string
                    pwd:
                      required: False
                      type: string

                  example:
                     phone: 13111111111
                     pwd: 123abc
            responses:
              500:
                description: 状态描述：服务器内部错误
              200:
                description: 状态描述：成功
              100:
                description: 状态描述：传入参数错误
              104:
                description: 状态描述：用户名或者密码错误, 登录失败
              105:
                description: 状态描述：学生名或班级代码输入错误, 登录失败
        """
        args = session_parser.parse_args()
        print(args)
        phone = args.phone
        pwd = args.pwd
        print(phone,pwd)
        user_dic.update({'phone':phone,'pwd':pwd})
        # user_dic['pwd'] = pwd
        return user_dic

    # 获取
    def get(self):
        """
            小程序获取phone用户信息
            ---
            tags:
              - 登录
            parameters:
              - name: 获取body
                in: body
                type: dict
                description: 获取用户参数
                schema:
                  properties:
                    phone:
                      required: False
                      type: string

                  example:
                     phone: 13111111111
            responses:
              500:
                description: 状态描述：服务器内部错误
              200:
                description: 状态描述：成功
              100:
                description: 状态描述：传入参数错误
              104:
                description: 状态描述：用户名或者密码错误, 登录失败
              105:
                description: 状态描述：学生名或班级代码输入错误, 登录失败
        """
        from flask import request
        print(request.path)
        print('GET请求！')
        return jsonify(user_dic)

    # 删除
    def delete(self,phone):
        """
            退出
            ---
            tags:
              - 登录
            parameters:
              - name: 获取body
                in: body
                type: dict
                description: 获取用户参数
                schema:
                  properties:
                    phone:
                      required: False
                      type: string

                  example:
                     phone: 13111111111
            responses:
              500:
                description: 状态描述：服务器内部错误
              200:
                description: 状态描述：成功
        """
        args = session_parser.parse_args()
        phone = args.phone
        print('phone is {}！'.format(phone))
        print('DELETE请求！')
        del user_dic['phone']
        return jsonify(user_dic)
