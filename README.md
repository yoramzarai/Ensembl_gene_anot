This package contains a parser to the Ensembl GFF3 gene annotation file (creating separate json file per gene), and examples for annotating genes (based on either the Ensembl GFF3 annotation file, or the generated json files (older version)).

The main notebooks are:
* `gene_annotation_example.ipynb` - an example of using the `Gene_annotation.py` util (in the `Utils/` folder) to annotate genes, based on the Ensembl GFF3 annotation file.
* `parse_gff3_file.ipynb` - parses the GFF3 Ensembl file and creates json file per gene.
* `json_gene_annotation_example.ipynb` - example of using the `gene_anot_utils.py` util (in the `Utils/` folder) to annotate genes, based on the json files. This is an older version of annotation. Follow the annotation shown in `gene_annotation_example.ipynb` instead.
