"""
{{cookiecutter.repo_name}}
"""

from {{cookiecutter.repo_name}}.core import demo, power, start


def test_start() -> None:
    """Test start"""
    start()
    assert True

def test_demo() -> None:
    """Test demo"""
    assert demo("name", "demo") == "name: demo"

def test_power() -> None:
    """Test power"""
    assert power(2) == 4
