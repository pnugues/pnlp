"""
Functions to load CoNLL datasets.
Some of the corpora are available from github.
For some others, you need to obtain them from LDC or other sources
and store them in your computer. You will have to edit the paths.
"""
from conll_dictorizer import CoNLLDictorizer
__author__ = "Pierre Nugues"

import sys
import os
import numpy as np
from os.path import join, dirname
from urllib.request import urlopen

sys.path.append(join(dirname(__file__), '..', '..'))


def load_ud_en_ewt(url='https://raw.githubusercontent.com/UniversalDependencies/UD_English-EWT/master/'):
    """
    The English Web treebank from github
    Source: https://universaldependencies.org/
    :param url:
    :return:
    """
    train_file = url + 'en_ewt-ud-train.conllu'
    dev_file = url + 'en_ewt-ud-dev.conllu'
    test_file = url + 'en_ewt-ud-test.conllu'

    column_names = ['ID', 'FORM', 'LEMMA', 'UPOS', 'XPOS',
                    'FEATS', 'HEAD', 'DEPREL', 'HEAD', 'DEPS', 'MISC']

    # column_names = list(map(str.lower, column_names))
    train_sentences = urlopen(train_file).read().decode('utf-8').strip()
    dev_sentences = urlopen(dev_file).read().decode('utf-8').strip()
    test_sentences = urlopen(test_file).read().decode('utf-8').strip()
    return train_sentences, dev_sentences, test_sentences, column_names


def load_ud_sv_talbanken(url='https://raw.githubusercontent.com/UniversalDependencies/UD_Swedish-Talbanken/master/'):
    """
    The Swedish talbanken from the Universal Dependency corpus.
    Changed column name UPOS to POS
    Source: https://universaldependencies.org/
    :param url:
    :return:
    """
    train_file = url + 'sv_talbanken-ud-train.conllu'
    dev_file = url + 'sv_talbanken-ud-dev.conllu'
    test_file = url + 'sv_talbanken-ud-test.conllu'

    column_names = ['ID', 'FORM', 'LEMMA', 'UPOS', 'XPOS',
                    'FEATS', 'HEAD', 'DEPREL', 'HEAD', 'DEPS', 'MISC']

    # column_names = list(map(str.lower, column_names))
    train_sentences = urlopen(train_file).read().decode('utf-8').strip()
    dev_sentences = urlopen(dev_file).read().decode('utf-8').strip()
    test_sentences = urlopen(test_file).read().decode('utf-8').strip()
    return train_sentences, dev_sentences, test_sentences, column_names


def load_ud_fr_gsd(url='https://raw.githubusercontent.com/UniversalDependencies/UD_French-GSD/master/'):
    """
    French Universal Dependency corpus.
    Changed column name UPOS to POS
    :param url:
    :return:
    """
    train_file = url + 'fr_gsd-ud-train.conllu'
    dev_file = url + 'fr_gsd-ud-dev.conllu'
    test_file = url + 'fr_gsd-ud-test.conllu'

    column_names = ['ID', 'FORM', 'LEMMA', 'UPOS', 'XPOS',
                    'FEATS', 'HEAD', 'DEPREL', 'HEAD', 'DEPS', 'MISC']

    # column_names = list(map(str.lower, column_names))
    train_sentences = urlopen(train_file).read().decode('utf-8').strip()
    dev_sentences = urlopen(dev_file).read().decode('utf-8').strip()
    test_sentences = urlopen(test_file).read().decode('utf-8').strip()
    return train_sentences, dev_sentences, test_sentences, column_names


def load_persian(url='https://raw.githubusercontent.com/UniversalDependencies/UD_Persian-PerDT/master/'):
    train_file = url + 'fa_perdt-ud-train.conllu'
    dev_file = url + 'fa_perdt-ud-dev.conllu'
    test_file = url + 'fa_perdt-ud-test.conllu'

    column_names = ['ID', 'FORM', 'LEMMA', 'UPOS', 'XPOS',
                    'FEATS', 'HEAD', 'DEPREL', 'HEAD', 'DEPS', 'MISC']
    train_sentences = urlopen(train_file).read().decode('utf-8').strip()
    dev_sentences = urlopen(dev_file).read().decode('utf-8').strip()
    test_sentences = urlopen(test_file).read().decode('utf-8').strip()
    return train_sentences, dev_sentences, test_sentences, column_names


if __name__ == '__main__':

    train_sentences, dev_sentences, test_sentences, column_names = load_ud_en_ewt()
    conll_dict = CoNLLDictorizer(column_names)
    train_dict = conll_dict.transform(train_sentences)
    print(train_dict[0])
    print(train_dict[1])
