import pandas as pd
import numpy as np
import random as rm

def gen_structure(n_of_carbon,n_of_hetero = 0) :
  mol_matrix = np.zeros((n_of_carbon,n_of_carbon),dtype=int)
  print(f"Original Matrix \n {mol_matrix}")

  for row in range(0,n_of_carbon) :
    for col in range(0,row+1) :
      mol_matrix[row][col] = rm.randint(0,1)
  

  for row in range(0,n_of_carbon) :
    for col in range(row,n_of_carbon) :
      mol_matrix[row][col] = mol_matrix[col][row]
      if row == col :
        mol_matrix[row][col] = 0

  return mol_matrix

def gen_no_of_structure(n_of_structures,n_of_carbons,n_of_heteroatoms=0) :
  mol_dict = {}
  for i in range(1,n_of_structures + 1) :
    mol = gen_structure(n_of_carbons,n_of_heteroatoms)
    mol_dict[f"mol_{i}"] = mol
  return mol_dict

if __name__ == "__main__" :
  first_mol_batch = gen_no_of_structure(10,5)
  print(first_mol_batch)
