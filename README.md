# Cheminformatics-ML-Model
An ML model to predict various physical properties using chemical graph theory and topological indices

# TODO
1) An ML Model that takes in a vertex edge adjacency matrix of a molecule and converts in into a suitable cheminformatics file format (I am currently leaning towards MOL/SDF since all bond related informations can be extracted from within it for easier processing).
2) A helper file that sanitises the molecule (ensures that all molecules follow valences, IUPAC rules etc)
3) A Python code to display all the generated structures in the form of a HTML file that contains the structures, their respective topographical indices (yet to decide) as well as the predicted chemical and physical properties (for now boiling point and heat of vaporization is what I am considering, may change depending on scope and application)

# Update 0.1 (10-01-2026)

1) The first Python file that generates a Random Vertex Adjacency matrix (basically a chemical molecule) based on no of carbon atoms (currently not implemented heteroatoms, that is a headache for later)
