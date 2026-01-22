import pandas as pd
import numpy as np
import random as rm
from rdkit import Chem
from enum import Enum
import random as rd

class HeteroAtoms(Enum) :
  Nitrogen = "N"
  Oxygen = "O"

# For heteroatoms, take in a dictionary of atom:atomCount, give out a tuple of (row of heteroatoms as columns of matrix,column of heteroatoms)
# [O:4,N:3]
def gen_structure(n_of_carbon,heteroatom_dict) :
  matrix_column = []
  for u in range(0,n_of_carbon) :
    matrix_column.append("C")

  for element,count in heteroatom_dict.items() :
    if element in HeteroAtoms :
      for i in range(1,count+1) :
        matrix_column.append(element)
    else :
      print("Element doesnt exist")
      return
      
  mol_matrix = np.zeros((len(matrix_column),len(matrix_column)),dtype=int)

  rd.shuffle(matrix_column)

  if(len(matrix_column) != mol_matrix.shape[0]) :
    print()
  for row in range(0,len(matrix_column)) :
    for col in range(0,row+1) :
      mol_matrix[row][col] = rm.randint(0,1)
  

  for row in range(0,len(matrix_column)) :
    for col in range(row,len(matrix_column)) :
      mol_matrix[row][col] = mol_matrix[col][row]
      if row == col :
        mol_matrix[row][col] = 0

  molecule = (mol_matrix,matrix_column)
  return molecule

def gen_no_of_structure(n_of_structures,n_of_carbons,heteroAtom_dict) :
  mol_dict = {}
  for i in range(1,n_of_structures + 1) :
    mol = gen_structure(n_of_carbons,heteroAtom_dict)
    mol_dict[f"mol_{i}"] = mol
  return mol_dict


def matrix_to_structure(molec_tuple) :
  adj_matrix = molec_tuple[0]
  hetero_info = molec_tuple[1]

  molec_df = pd.DataFrame(adj_matrix,index=)
  for i in range(0,adj_matrix.shape[0]) :
    for j in range (0,i) :
      

if __name__ == "__main__" :
  heteroAtom_Dict = {"O":2,"N":3}
  first_mol_batch = gen_no_of_structure(10,5,heteroAtom_Dict)
  print(first_mol_batch)
