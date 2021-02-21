import yaml
import uuid

def get_train_params(json_data, main_dir)
    

    return None if json_data['data_dir'] is None or json_data['job_dir'] is None
    

    params_path = os.path.join(main_dir, json_data['params_file_path'])

    file_open = open(params_path, "r") # パスが間違えていた時のエラー処理
    data = yaml.safe_load(file_open)

    id_string = str(uuid.uuid4())
    job_dir = os.path.join(job_dir, id_string)

    data['training_inputs']['jobDir'] = job_dir
    data['training_inputs']['args']['--data-dir'] = data_dir
    data['training_inputs']['pythonModule'] = 'trainer.task'
    data['id_string'] = id_string

    return data

def get_deploy_params(json_data, main_dir)
    return None if json_data['deploymentUri'] is None or json_data['versionName'] is None
    

    params_path = os.path.join(main_dir, json_data['params_file_path'])


    file_open = open(params_path, "r") # パスが間違えていた時のエラー処理
    data = yaml.safe_load(file_open)

    data['request_body']['name'] = json_data['versionName']
    data['request_body']['deploymentUri'] = json_data['deploymentUri']
    data['request_body']['runtimeVersion'] = data['training_inputs']['runtimeVersion'] # ここができるかまだわかららん
    data['request_body']['pythonVersion'] = data['training_inputs']['pythonVersion'] # ここができるかまだわかららん
    
    return data
