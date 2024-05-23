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

from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData

CustDataobj=CustomData(1.52,62.2,58.0,7.27,7.33,4.55,"Premium","F","VS2")

data=CustDataobj.get_data_as_dataframe()

print(data)
















