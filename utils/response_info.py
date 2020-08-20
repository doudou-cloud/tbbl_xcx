from flask import jsonify,make_response

### 定义相应状态码  ###

CODE_SUCCESS = 200   # 成功

CODE_INTERNAL_ERROR = 500  # 服务器内部错误


CODE_INVALID_PARAMTER = 100  # 传入参数错误
CODE_INVALID_CHECK = 101    # 校验不通过
CODE_INVALID_TOKEN = 102    # 无效的token
CODE_ORIGINAL_PASSWORD_ERROE = 103  # 原始密码错误
CODE_USER_OR_PASSWORD_ERROR = 104  # 用户名或密码错误  登陆失败
CODE_PERMISSION_DENIED = 106  # 权限不足
CODE_PASSWORD_MODIFTY_ERROR = 107  # 密码修改失败
CODE_TOKEN_GENERATE_FAILURE = 109  # token生成失败，登陆失败
CODE_ADD_DATA_ERROR = 110  # 添加数据失败
CODE_NOT_LOGGED_IN = 112  # 未登录
CODE_GET_DATA_ERROR = 113  # 获取数据失败
CODE_INPUT_ERROR = 119  # 输入无效
CODE_PEPEATED_OPERATION = 120  # 重复的操作
CODE_FILES_UPLOAD_ERROR = 121  # 文件上传失败





def meke_suceesee_res(data,msg):
    res ={
        "code":CODE_SUCCESS,
        "data":data,
        "msg":msg
    }
    return make_response(jsonify(res))


def make_fail_res():
    return

