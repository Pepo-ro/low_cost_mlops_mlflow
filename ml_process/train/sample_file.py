import git
import tempfile
import pdb
import json
import os

with tempfile.TemporaryDirectory() as tmpdir:
  write_path = os.path.join(tmpdir, 'sample.json') # パスを作成
  #write_path = repo_dir + "\\sample.json"
  data = {}
  
  fp = open(write_path , 'w')
  json.dump(data,fp, indent=4)

  json_open = open(write_path, 'r')

  print(json_open)



