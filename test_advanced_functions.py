import pytest
import advaned_functions as af

@pytest.fixture
def harmonic_input_series():
    return [1,2,3]

@pytest.fixture
def harmnic_input_empty_series():
    return []

def test_calc_harmonic_mean(harmonic_input_series):
    result = af.calculate_harmonic_mean(harmonic_input_series)
    assert result == 0.5454545454545455

def test_calc_harmonic_mean(harmnic_input_empty_series):
    try:
        result = af.calculate_harmonic_mean(harmnic_input_empty_series)
    except:
        pytest.fail("Error divide by zero")

    assert result == 0

def test_print_directories():
    try:
        af.print_directories(None)
        af.print_directories("/homee")
        af.print_directories(1)
        af.print_directories(4)
    except NotADirectoryError as ne:
        pytest.fail("Not a directory error")
    except FileNotFoundError as fe:
        pytest.fail("File not found error.")
    except OSError as oe:
        pytest.fail(f"OsError: {oe}")

    except Exception as e:
        pytest.fail(f"Exception {e}")