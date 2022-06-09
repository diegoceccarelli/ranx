import pytest
from ranx.fusion import rrf
from ranx import Run


# FIXTURES =====================================================================
@pytest.fixture
def run_1():
    run_dict = {
        "q1": {"d1": 1, "d2": 2, "d3": 3},
        "q2": {"d1": 1, "d2": 2},
    }

    return Run(run_dict)


@pytest.fixture
def run_2():
    run_dict = {
        "q1": {"d1": 3, "d2": 2},
        "q2": {"d1": 1, "d3": 3},
    }

    return Run(run_dict)


@pytest.fixture
def run_3():
    run_dict = {
        "q1": {"d3": 1},
        "q2": {"d2": 2, "d3": 3},
    }

    return Run(run_dict)


# TESTS ========================================================================
def test_rrf(run_1, run_2, run_3):
    combined_run = rrf([run_1, run_2, run_3])

    assert combined_run.name == "rrf"

    assert len(combined_run) == 2
    assert len(combined_run["q1"]) == 3
    assert len(combined_run["q2"]) == 3

    assert combined_run["q1"]["d1"] == ((1 / (60 + 3)) + (1 / (60 + 1)))
    assert combined_run["q1"]["d2"] == ((1 / (60 + 2)) + (1 / (60 + 2)))
    assert combined_run["q1"]["d3"] == ((1 / (60 + 1)) + (1 / (60 + 1)))
    assert combined_run["q2"]["d1"] == ((1 / (60 + 2)) + (1 / (60 + 2)))
    assert combined_run["q2"]["d2"] == ((1 / (60 + 1)) + (1 / (60 + 2)))
    assert combined_run["q2"]["d3"] == ((1 / (60 + 1)) + (1 / (60 + 1)))
