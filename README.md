This package contains examples for annotating genes based on the Ensembl GFF3 annotation file. 

It also contains a parser to the Ensembl GFF3 gene annotation file (used to generate separate json file per gene), and gene annotation examples based on the generated json files, both of which are not used anymore.

The main notebook is:
* `gene_annotation_example.ipynb` - an example of using the `Gene_annotation.py` util (in the `Utils/` folder) to annotate genes, based on the Ensembl GFF3 annotation file.

**To update to a new Ensembl annotation version**:
- Download the new GFF3 file from the [Ensembl Human site](https://useast.ensembl.org/Homo_sapiens/Info/Index) (e.g. `Homo_sapiens.GRCh38.110.gff3.gz`, from `https://ftp.ensembl.org/pub/release-110/gff3/homo_sapiens/`) to `Projects/Cancer_mut/Data/Ensembl_gene_annotation/` folder
- Update the `Ensembl_release` variable value in `Utils/Gene_annotation.py` to the new version number

**To update to a new Genomic Build (new chromosome files)**:
- Go to https://www.ensembl.org/Homo_sapiens/Info/Index and click on `Download DNA sequence (FASTA)` (for example, for version 110 it takes you [here](https://ftp.ensembl.org/pub/release-110/fasta/homo_sapiens/dna/)). 
- Download the chromosome files (to `Data/Genomes/Human/human_<version>/Chromosome` on MAC or `/tamir2/lab_resources/Genomes/Human/human_<version>/Chromosome` on Power)
- Download the `.toplevel.fa.gz` toplevel file to the `human_<version>/All` folder
- Update `chromosome_path` in `Utils/mys_init.py`. If needed, update also `get_chrm_file_name`
- Add `chrm_size_<ver>` variable in `Utils/genetic_human_utils.py`

Old Notebooks (not used any more):
* `parse_gff3_file.ipynb` - parses the GFF3 Ensembl file and creates json file per gene.
* `json_gene_annotation_example.ipynb` - example of using the `gene_anot_utils.py` util (in the `Utils/` folder) to annotate genes, based on the generated json files.

