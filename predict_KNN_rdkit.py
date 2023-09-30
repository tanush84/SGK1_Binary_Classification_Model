import argparse
import pandas as pd
import joblib
import numpy as np
import pandas as pd
from rdkit import rdBase, Chem
from rdkit.Chem import AllChem, PandasTools, Descriptors
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import PandasTools
from sklearn.svm import SVC
import os, sys
import argparse
import configparser
import time
import re
from lightgbm import *
import argparse

df = []

def read_smi_file(file_path):
    try:
        with open(file_path, 'r') as smi_file:
            lines = smi_file.readlines()
        return [line.strip() for line in lines]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []

def smi_to_dataframe(file_path):
    smi_data = read_smi_file(file_path)
    if not smi_data:
        return None
    
    data = {'SMILES': smi_data}
    df = pd.DataFrame(data)
    return df

def main():
    parser = argparse.ArgumentParser(description="Convert a .smi file to a pandas DataFrame.")
    parser.add_argument('input_file', type=str, help='Path to the .smi file')

    args = parser.parse_args()
    input_file = args.input_file

    df = smi_to_dataframe(input_file)

    if df is not None:
        print("DataFrame created successfully:")
        print(df.head())
        PandasTools.AddMoleculeColumnToFrame(df, 'SMILES')
        df['FP'] = df.apply(lambda x: AllChem.GetMorganFingerprintAsBitVect(x.ROMol, 2, 1024), axis=1)
        FP= [AllChem.GetMorganFingerprintAsBitVect(mol, 2, 1024) for mol in df.ROMol]
        df_FP = pd.DataFrame(np.array(FP))
        df_FP.index = df.index
        df = pd.concat([df, df_FP], axis=1)
        X = df.drop(df.columns[[0, 1, 2]],axis = 1)
        
        filename = './assets/predict_KNN_rdkit.joblib'
        # load the model from disk
        loaded_model = joblib.load(filename)

        y_train=pd.read_csv('./assets/sgk1_Y_train.csv')
        
        x_train=pd.read_csv('./assets/sgk1_X_train.csv')
        result = loaded_model.fit(x_train.values, y_train.values.ravel())
        y_predicted = loaded_model.predict(X.values)
        
        if y_predicted==1:
            print("Molecule is predicted to be Active")
        elif y_predicted==0:
            print("Molecule is predicted to be Inctive")

    else:
        print("DataFrame creation failed.")
    
    


if __name__ == "__main__":
    main()



