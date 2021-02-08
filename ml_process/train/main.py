import subprocess
import tempfile

import git
import googleapiclient.errors.HttpError as http_error_message

from google.api_core.client_options import ClientOptions
from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
from flask import Flask, request

app = Flask(__name__)

REPO = os.getenv('GIT_REPO')
PROJECT_ID = os.getenv('PROJECT_ID')

@app.route('/')
def index():
    return 'A service to Submit a traing job for the babyweight-keras example.'

@app.route('/api/job/<string:job_id>', methods=['GET'])
def job_info(job_id):
    credentials = GoogleCredentials.get_application_default()
    api = discovery.build(
        'model', 'v1', credentials=credentials, cache_discovery=False)
    api_request = api.projects().jobs().get(
        name='projects/{}/jobs/{}'.format(PROJECT_ID, job_id))

    try:
        resp = api_request.execute()
    except http_error_message as err:
        resp = {'message': err._get_reason()}
        return resp, 500

    return resp, 200

@app.route('/api/train', methods=['POST'])
def train():
    json_data = request.get_json() # ここはちょっと考える  params_file_path がまだできていない 　# get_trainparamsにいれたほうがいいかも
    params_file_path = json_data['params_file_path']

    with tempfile.TemporaryDirectory() as tmpdir:
        main_dir = os.path.join(tmpdir, 'main')
        git.Repo.clone_from(REPO, main_dir, branch='main')

        params_path = os.path.join(main_dir, params_file_path)    　# get_trainparamsにいれたほうがいいかも

        train_params = get_train_params(params_path, data_dir, job_dir)
        if train_params is None
            resp = {'message': 'Option dataDir or jobDir is not specified.'}
            return resp, 500

        job_id = 'train-{}-weight-{}'.format(train_params['model_name'], train_params['id_string']).replace('-', '_')
        
        train_dir = os.path.join(main_dir, '{}_model'.format(train_params['model_name']))

        subprocess.run('cd {};python3 setup.py sdist'.format(train_dir),
                       shell=True, stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
        package_file = os.path.join(train_dir, 'dist', train_params['trainer_file_name'])
        package = '{}/{}'.format(job_dir, train_params['trainer_file_name'])
        subprocess.run('gsutil cp {} {}'.format(package_file, package),
                       shell=True, stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL)
        
        training_inputs = train_params['training_inputs']

        job_boy = {'jobId': job_id, 'trainingInput': training_inputs}

        credentials = GoogleCredentials.get_application_default()
        api = discovery.build(
            'model', 'v1', credentials=credentials, cache_discovery=False)
        api_request = api.projects().jobs().create(
            body=job_boy, parent='projects/{}'.format(PROJECT_ID))

        try:
            resp = api_request.execute()
            return resp, 200
        except http_error_message as err:
            resp = {'message': err._get_reason()}
            return resp, 500

@app.route('/api/deploy', methods=['POST'])
def deploy():
    json_data = request.get_json() # ここはまだ　# get_trainparamsにいれたほうがいいかも

    params_file_path = json_data['params_file_path']# ここはちょっと考える  params_file_path がまだできていない
    deployment_uri = json_data['deploymentUri'] # get_trainparamsにいれたほうがいいかも
    version_name = json_data['versionName']# get_trainparamsにいれたほうがいいかも

    with tempfile.TemporaryDirectory() as tmpdir:
        main_dir = os.path.join(tmpdir, 'main')
        git.Repo.clone_from(REPO, main_dir, branch='main')

        params_path = os.path.join(main_dir, params_file_path) # get_deploy paramsに分けたほうがいいかも
        deploy_params = get_deploy_params(params_path, model_name, version_name, deploy_uri) # 

        if deploy_params is None
            resp = {'message': 'Option deploymentUri or versionName is not specified.'}
            return resp, 500

    endpoint = 'https://{}-ml.googleapis.com'.format(deploy_params['region')
    
    client_options = ClientOptions(api_endpoint=endpoint)
    credentials = GoogleCredentials.get_application_default()
    api = discovery.build('model', 'v1', credentials=credentials,
                          cache_discovery=False,
                          client_options=client_options)

    api_request = api.projects().models().get(
        name='projects/{}/models/{}_model'.format(PROJECT_ID, deploy_params['model_name']))

    request_body = deploy_params['request_body'] 

    try:
        resp = api_request.execute()
    except http_error_message as err:
        request_body = {'name': '{}_model'.format(deploy_params['model_name'])}
        api_request = api.projects().models().create(
            parent='projects/{}'.format(PROJECT_ID),
            body=request_body)
        api_request.execute()

    api_request = api.projects().models().versions().create( 
        parent='projects/{}/models/{}_model'.format(PROJECT_ID, deploy_params['model_name']), 
        body=request_body)

    try:
        resp = api_request.execute()
    except http_error_message as err:
        resp = {'message': err._get_reason()}
        return resp, 500

    return resp, 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
