import pytest
import lint
import os


def test_linter_raises_if_grepped_file_has_text(file_with_text, file_name):
    with pytest.raises(AssertionError):
        lint.check_grep(file_name)


def test_linter_does_not_raise_if_grepped_file_is_empty(file_with_no_text, file_name):
    try:
        lint.check_grep(file_name)
    except AssertionError:
        assert False, "not expecting a raise"
    assert True, "check_grep did not raise"


@pytest.fixture
def file_name():
    return "lint_result.txt"


@pytest.fixture
def file_with_text(file_name):
    write_file(file_name, "contentlink-missing")
    yield
    remove_results(file_name)


@pytest.fixture
def file_with_no_text(file_name):
    write_file(file_name, "")
    yield
    remove_results(file_name)


# helpers


def write_file(file_name, content):
    with open(file_name, "w") as file:
        file.write(content)


def remove_results(file_name):
    os.remove(file_name)


