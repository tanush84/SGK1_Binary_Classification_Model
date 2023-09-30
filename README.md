END to END ML model for the binary prediction of SGK-1 inhibitors using python script. 

*****

After installing the requirements in an Virtual Environment
or creating a new environment using conda by using "environment_dependencies.yml" file
just open the command prompt or Terminal in the above created virtual environment
run the command given below
### Using KNN Algorithm based prediction
python predict_KNN_rdkit.py test.smi

### OR 
### Using SVM Algorithm based prediction
python predict_SVM_rdkit.py test.smi

similarly, for any unknown molecule when just use the command by specifying the path
of "*.smi" file.
The supplied "test.smi" file is an inactive molecule.

python predict_name_of_algorithm.py [specify_path]*.smi


The result will be displayed in the terminal as Molecule to be active or Inactive

The image in repository indicate the Various models along with the accuracy as predicted by lazy algorithm.




 
