import pytest
from boyer_moore import *


@pytest.mark.parametrize("full_string", 
['ATCGATCGTCGATGCCCTGATCGCGATCGATCGATCGATG',
'CCTGATCGCGATCATCGATCGATCGATCGTGACTAGCTGGCGCGC',
'ACTGATCAGCGCGCGCGATATATCTGATGCATCCTGATCGCG'])
def test_BM_works(full_string):
    search_string = 'CCTGATCGCG'
    result, _ = boyer_moore(full_string, search_string)
    assert result[0] == True

@pytest.mark.parametrize("full_string", [
    'ACTGATCAGCGCGCGCGATATATCTGATGCATCCTGATCGC',
    'ACTGATCAGCGCGCGCGATATATCTGATGCATCCTGATCG',
    'ACTGATCAGCGCGCGCGATATATCTGATGCATCCTGATC'
])
def test_BM_not_works_edge_partial_match(full_string):
    search_string = 'CCTGATCGCG'
    result, _ = boyer_moore(full_string, search_string)
    assert result[0] == False

def test_BM_search_string_len_is_equal_to_full_str():
    full_string = 'CCTGATCGCG'
    search_string = 'CCTGATCGCG'
    result, _ = boyer_moore(full_string, search_string)
    assert result[0] == True

def test_BM_search_string_len_is_equal_to_full_str_not_matching():
    full_string = 'CCTGATGGCG'
    search_string = 'CCTGATCGCG'
    result, _ = boyer_moore(full_string, search_string)
    assert result[0] == False

def test_BM_search_string_len_longer_than_full_str():
    full_string = 'CGTA'
    search_string = 'CCTGATCGCG'
    result, _ = boyer_moore(full_string, search_string)
    assert result[0] == False

def test_BM_full_string_is_blank():
    full_string = ''
    search_string = 'CCTGATCGCG'
    result, _ = boyer_moore(full_string, search_string)
    assert result[0] == False

def test_BM_search_string_is_blank():
    full_string = 'ATCGATCGTCGATGCCCTGATCGCGATCGATCGATCGATG'
    search_string = ''
    # assert result[0] == False
    # #This test case returned True, which needs to be rectified
    with pytest.raises(Exception) as err:
        boyer_moore(full_string, search_string)
    assert str(err.value) == "The given search string is empty"

def test_BM_search_string_is_one_letter():
    full_string = 'ATCGATCGTCGATGCCCTGATCGCGATCGATCGATCGATG'
    search_string = 'C'
    result, _ = boyer_moore(full_string, search_string)
    assert result[0] == True