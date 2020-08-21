import hashlib
import time

from flask import jsonify
from flask_restful import Resource, reqparse
import requests
from utils.get_session_key import get_session_key

from utils.redis_utils import rds



session_parser = reqparse.RequestParser()

session_parser.add_argument('token', type=str, location=['json'], help='token权限')
session_parser.add_argument('code', type=str, location=['json'], help='前端传的code')
session_parser.add_argument('encryptedData', type=str, location=['json'])
session_parser.add_argument('iv', type=str, location=['json'])



user_dic = {}


class SessionsResource(Resource):
    # 登录

    def post(self):
        """
            小程序用户登录
            ---
            tags:
              - 登录及获取用户信息
            parameters:
              - name: 登录body
                in: body
                type: dict
                description: 登录/获取用户信息用参数
                schema:
                  properties:
                    code:
                      required: False
                      type: string
                    iv:
                      required: False
                      type: string
                    encryptedData:
                      required: False
                      type: string
                  example:
                     code: 13111111111
                     encryptedData: CiyLU1Aw2KjvrjMdj8YKliAjtP4gsMZMQmRzooG2xrDcvSnxIMXFufNstNGTyaGS9uT5geRa0W4oTOb1WT7fJlAC
                     iv: r7BXXKkLb8qrSNn05n0qiA
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
        code = args.code
        # print(code)
        if code:
            res = get_session_key(code)
            if res is False:
                return  #  获取session_key失败

            print(res)

            # errcode为0时代表请求成功，成功获取到session_key
            val = res['openid'] + "&" + res['session_key']
            key = res['openid'] + str(int(time.time()))
            md5 = hashlib.md5()
            md5.update(key.encode('utf-8'))
            key = md5.hexdigest()
        # 将token保存在redis中, --->便于今后验证   token ---->   key(openid+timestamp):val(openid+session_key)
            rds.set(key,val,ex=3600*24*2)
        # 判断数据库有没有该用户   有--->不做操作   无--->存入数据库
            response = {
                'token':key
            }

            return jsonify(response)

        # else:
        #     return {'missing parameter':'0'}

        # else:
        #     # 否则获取secret_key失败，返回获取失败,前端重新发起请求
        #     return {'missing code'}
        encryptedData = args.encryptedData
        iv = args.iv
        print(encryptedData, iv)
        #
        # if encryptedData and iv:
        #     appid = None
        #     from lalala.WXBizDataCrypt import WXBizDataCrypt
        #     pc = WXBizDataCrypt(appid, sessionKey=None)
        #     user_info_dict = pc.decrypt(encryptedData=encryptedData, iv=iv)  # 解密后的用户数据
        #     ''' 格式
        #         {
        #             'openId': 'oGZUI0egBJY1zhBYw2KhdUfwVJJE',
        #             'nickName': 'Band',
        #             'gender': 1,
        #             'language': 'zh_CN',
        #             'city': 'Guangzhou',
        #             'province': 'Guangdong',
        #             'country': 'CN',
        #             'avatarUrl': 'http://wx.qlogo.cn/mmopen/vi_32/aSKcBBPpibyKNicHNTMM0qJVh8Kjgiak2AHWr8MHM4WgMEm7GFhsf8OYrySdbvAMvTsw3mo8ibKicsnfN5pRjl1p8HQ/0',
        #             'unionId': 'ocMvos6NjeKLIBqg5Mr9QjxrP1FA',
        #             'watermark': {
        #                             'timestamp': 1477314187,
        #                             'appid': 'wx4f4bc4dec97d474b'
        #                             }
        #         }
        #     '''


        # else:
            # 缺少参数，获取数据失败，前端重新发起请求
        return {'missing parameter':'102'}

    # 获取
    def get(self):

        from flask import request
        print(request.path)
        print('GET请求！')
        return jsonify(user_dic)

    # 删除
    def delete(self,code):

        # print(code)
        args = session_parser.parse_args()
        code = args.code
        print('phone is {}！'.format(code))
        print('DELETE请求！')
        # del user_dic['phone']
        return jsonify(user_dic)
