from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from entpoints.sessions.resource import SessionsResource
from flasgger import Swagger

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
# 用户登录api
api.add_resource(SessionsResource,'/sessions',methods=['GET','POST'])
api.add_resource(SessionsResource,'/sessions/<string:phone>',methods=['DELETE'],endpoint='loginout')

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    print('hehhehe')
    app.run()