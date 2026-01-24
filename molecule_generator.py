import pandas as pd
import numpy as np
import random as rm
from rdkit import Chem
from enum import Enum
from rdkit.Chem import rdmolops
from rdkit.Chem import Draw
from rdkit.Chem import rdCoordGen
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
    print("Given number of atoms out of bounds of vertex adjacency matrix, try again")
    return
  
  for row in range(0,len(matrix_column)) :
    for col in range(0,row+1) :
      mol_matrix[row][col] = rm.randint(0,1)

  for row in range(0,len(matrix_column)) :
    mol_matrix[row][row] = 0
    if np.sum(mol_matrix[row]) == 0 :
      col_to_set = rm.choice([i for i in range(mol_matrix.shape[1]) if i != row])
      if col_to_set > row :
        mol_matrix[col_to_set][row] = 1
      else :
        mol_matrix[row][col_to_set] = 1

  for row in range(0,len(matrix_column)) :
    for col in range(row+1,len(matrix_column)) :
      mol_matrix[row][col] = mol_matrix[col][row]

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

  mol = Chem.RWMol()
  for atom_symbol in hetero_info :
    atom = Chem.Atom(atom_symbol)
    mol.AddAtom(atom)

  for i in range(0,adj_matrix.shape[0]) :
    for j in range (0,i+1) :
      if (adj_matrix[i][j] == 1) :
        mol.AddBond(i,j,Chem.BondType.SINGLE)
      if (adj_matrix[i][j] == 2) :
        mol.AddBond(i,j,Chem.BondType.DOUBLE)
      if (adj_matrix[i][j] == 3) :
        mol.AddBond(i,j,Chem.BondType.TRIPLE)     

  final_mol=mol.GetMol()
  try :
    rdmolops.SanitizeMol(final_mol)
    rdCoordGen.AddCoords(final_mol)
    return final_mol
  except (Chem.rdchem.AtomValenceException) :
    print("Molecule doesnt satisfy the laws of chemistry")
    return

if __name__ == "__main__" :
  heteroAtom_Dict = {"O":1,"N":0}
  first_mol_batch = gen_no_of_structure(200,4,heteroAtom_Dict)
  print(first_mol_batch)
  final_mols = []
  for mol in first_mol_batch.values() :
    actual_mol = matrix_to_structure(mol)
    if actual_mol not in final_mols and actual_mol is not None :
      final_mols.append(actual_mol)
  print(f"No of mols finally = {len(final_mols)}")
  if final_mols:
    mols_display = Draw.MolsToImage(final_mols)
    mols_display.show()
  else:
    print("The molecule list is empty")
  