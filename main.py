from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from flasgger import Swagger


#  用户登录api
from entpoints.sessions.resource import SessionsResource




app = Flask(__name__)

cors = CORS(app,resources={r"/api/v1/*": {"origins": "*"}}, supports_credentials=True)
api = Api(app)



app.config['SWAGGER'] = {
    'title': '小程序api',
    'uiversion': 2
}
swagger_template = {
    'securityDefinitions': {
        'basicAuth': {
            'type': 'basic'
        }
    }
}
swagger = Swagger(app, template=swagger_template)

api.prefix = '/api/v1'
# 登录/获取用户信息api
api.add_resource(SessionsResource,'/sessions',methods=['GET','POST'],endpoint='login')




@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    # print('hehhehe')
    app.run(host='0.0.0.0',port=5000)