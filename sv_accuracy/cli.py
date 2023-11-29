"""Console script for sv_accuracy."""
import typer
from sv_accuracy.sv_accuracy import get_accuracy


def main_function(truth_vcf_file_name: str, sample_vcf_file_name: str):
    accuracy = get_accuracy(truth_vcf_file_name, sample_vcf_file_name)
    print(accuracy)


def main():
    typer.run(main_function)


if __name__ == "__main__":
    main()
