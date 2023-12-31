""" 
This simple script verifies that all data rows in the chromosome 
files (other than the last row) have equal number of NTs per row.

This is assumed, for example, by the Fasta_segment class (see Fasta_segment.py), 
which is used by the function pull_fasta_seq().
"""
import mysys_init as si

def main() -> None:
    """Performs the validation. """
    print(f"Checking all .fa files in {si.chromosome_path} ...")
    for chrm_file in si.chromosome_path.glob("*.fa"):
        with open(chrm_file, 'rt') as fp:
            # first row is the header. Last row may have different number of NTs.
            assert len({len(x) for x in fp.readlines()[1:-1]}) == 1, f"Not all rows in {chrm_file} have equal number of characters !!"
    print("Done. All .fa files have the same number of NTs per row.")

if __name__ == "__main__":
    main()
