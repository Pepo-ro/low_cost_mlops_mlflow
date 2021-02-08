import yaml
import uuid

def get_train_params(file_path, data_dir, job_dir)

    return None if data_dir is None or job_dir is None

    file_open = open(file_path, "r") # パスが間違えていた時のエラー処理
    data = yaml.safe_load(file_open)

    id_string = str(uuid.uuid4())
    job_dir = os.path.join(job_dir, id_string)

    data['training_inputs']['jobDir'] = job_dir
    data['training_inputs']['args']['--data-dir'] = data_dir
    data['training_inputs']['pythonModule'] = 'trainer.task'
    data['id_string'] = id_string

    return data

def get_deploy_params(file_path, model_name, version_name, deploy_uri)
]   return None if deployment_uri is None or version_name is None
    
    file_open = open(file_path, "r") # パスが間違えていた時のエラー処理
    data = yaml.safe_load(file_open)

    data['request_body']['name'] = version_name
    data['request_body']['deploymentUri'] = deploy_uri
    data['request_body']['runtimeVersion'] = data['training_inputs']['runtimeVersion'] # ここができるかまだわかららん
    data['request_body']['pythonVersion'] = data['training_inputs']['pythonVersion'] # ここができるかまだわかららん
    
    return data
