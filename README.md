A parser to the Ensembl GFF3 gene annotation file, creating separate json file per gene. 

The json files are used by our gene annotation utility (gene_anot_utils.py) to enable gene annotation in Python.

The main notebooks are:
* parse_gff3_file.ipynb - parses the GFF3 Ensembl file and create json file per gene
* gene_annotation_example.ipynb - example of using the util gene_anot_utils.py (in the Utils/ folder) to annotate genes.
