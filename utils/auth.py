import jwt
import time


openid,phone,type = None,None,None
login_result = {
    'openid':None,
    'phone':phone,
    'type':type
}

token_salt_key = 'aaa'

def generate_encode_token(ts,login_result,phone):
    '''
    生成登录token,用于之后的一系列验证
    :param ts:
    :param login_result:
    :param phone:
    :return:
    '''
    try:
        payload = {
            'iat':ts,
            'login_result':login_result,
            'iss':None,
            'info':{
                'phone':phone
            }
        }
        token_encode = jwt.encode(payload,token_salt_key,algorithm='HS256')


    except Exception as e:
        print('generate_encode_token：{}'.format(str(e)))
        print(f'generate_encode_token：{str(e)}')
        return False

    return token_encode


def check_decode_token():
    try:

        pass

    except Exception as e:

        return False



def check_auth():
    pass


