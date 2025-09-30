import app
import pytest
from pprint import pprint as pp


@pytest.mark.parametrize(
    ["path"], [pytest.param(".\\tests\\doc\\"), pytest.param("tests/doc/")]
)
def test_check(path: str):
    files = app.lookup_file(path)

    pp(files)

    assert len(files) == 2


def test_main():
    res = app.main(["tests/doc/"])
