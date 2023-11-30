import bionumpy as bnp

def get_accuracy(truth_vcf_file_name: str, sample_vcf_file_name: str):
    truth, calls = (bnp.open(file_name, buffer_type=bnp.io.VCFMatrixBuffer).read() for file_name in [truth_vcf_file_name, sample_vcf_file_name])
    return calculate_accuracy(truth, calls)


def normalize_genotype(genotype):
    genotype = genotype.replace("|", "/")
    if genotype == "1/0":
        genotype = "0/1"

    return genotype


def calculate_accuracy(truth, calls):
    truth = {(variant.chromosome, variant.position, variant.ref_seq, variant.alt_seq): variant.genotypes for variant in truth.tolist()}
    success = 0
    for variant in calls.tolist():
        if normalize_genotype(variant.genotypes) == \
            normalize_genotype(truth[(variant.chromosome, variant.position, variant.ref_seq, variant.alt_seq)]):
            success += 1
    return success/len(truth)
