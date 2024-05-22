"""import os
path="notebooks/research.ipynb"

dir,file=os.path.split(path)

os.makedirs(dir,exist_ok=True)

with open (path,"w") as f:
    pass """



"""echo [$(date)]: "START"


echo [$(date)]: "creating env with python 3.8 version" 


conda create --prefix ./env python=3.8 -y


echo [$(date)]: "activating the environment" 

source activate ./env

echo [$(date)]: "installing the dev requirements" 

pip install -r requirements.txt

echo [$(date)]: "END"  """



















