import pytest
from contracts import Contract, Contracts


def test_get_top_N_open_contracts_default():
    contracts = [
        Contract(1, 1),
        Contract(2, 2),
        Contract(3, 3),
        Contract(4, 4),
        Contract(5, 5)
    ]
    renegotiated = [3]
    top_n = 3
    c_managed = Contracts()
    actual_open_contracts = c_managed.get_top_N_open_contracts(contracts, renegotiated, top_n)
    expected_open_contracts = [5, 4, 2]
    assert expected_open_contracts == actual_open_contracts

def test_get_top_N_open_contracts_empty_list():
    contracts = []
    renegotiated = []
    top_n = 3
    c_managed = Contracts()
    actual_open_contracts = c_managed.get_top_N_open_contracts(contracts, renegotiated, top_n)
    assert actual_open_contracts == []

def test_get_top_N_open_contracts_with_fewer_contracts():
    contracts = [
        Contract(1, 1),
        Contract(2, 2)
    ]
    renegotiated = []
    top_n = 3
    c_managed = Contracts()
    actual_open_contracts = c_managed.get_top_N_open_contracts(contracts, renegotiated, top_n)
    expected_open_contracts = [2, 1]
    assert expected_open_contracts == actual_open_contracts
