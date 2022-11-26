echo [$(date)]: "START"    
## echo is used for Print
echo [$(date)]: "Creating conda env with version 3.8"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activate env"
source activate ./env
echo [$(date)]: "install dev requirements"
pip install -r requirements_dev.txt 
echo [$(date)]: "END"
