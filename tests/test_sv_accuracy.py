#!/usr/bin/env python

"""Tests for `sv_accuracy` package."""

import bionumpy as bnp

from sv_accuracy.sv_accuracy import calculate_accuracy


def test_calculate_accuracy():
    calls = bnp.open('calls_small.vcf', buffer_type=bnp.io.VCFMatrixBuffer).read()
    truth = bnp.open('truth_small.vcf', buffer_type=bnp.io.VCFMatrixBuffer).read()
    assert calculate_accuracy(truth, truth) == 1  # 5/7
    assert calculate_accuracy(truth, calls) == 5 / 7
    assert calculate_accuracy(truth, calls[1:]) == 4 / 7
    assert calculate_accuracy(truth, calls[6:]) == 0 / 7

def test_calculate_accuracy_big_acceptance():
    calls = bnp.open('population_large.vcf.gz', buffer_type=bnp.io.VCFMatrixBuffer).read()
    assert calculate_accuracy(calls, calls) == 1
