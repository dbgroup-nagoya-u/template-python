# coding=utf-8

import sample_module


def test_sample_function():
    assert sample_module.sample_func() == 1


def test_sample_class():
    sample_class = sample_module.SampleClass()
    assert sample_class.sample_func() == 1
