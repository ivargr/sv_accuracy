import bionumpy as bnp

def get_accuracy(truth_vcf_file_name: str, sample_vcf_file_name: str):
    truth, calls = (bnp.open(file_name, buffer_type=bnp.io.VCFMatrixBuffer).read() for file_name in [truth_vcf_file_name, sample_vcf_file_name])
    return calculate_accuracy(truth, calls)


def calculate_accuracy(truth, calls):
    truth = {(variant.id, variant.position, variant.ref_seq, variant.alt_seq): variant.genotypes for variant in truth.tolist()}
    success = 0
    for variant in calls.tolist():
        if variant.genotypes == truth[(variant.id, variant.position, variant.ref_seq, variant.alt_seq)]:
            success += 1
    return success/len(truth)
