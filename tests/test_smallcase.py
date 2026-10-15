import pytest
from typer.testing import CliRunner

from pytoolbox.cli import app

runner = CliRunner()


def test_titlecase_simple():
    result = runner.invoke(app, ["smallcase", "HELLO WORLD"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Hello World"


@pytest.mark.xfail(strict=True, reason="See ISSUES.md")
def test_smallcase_handles_apostrophes():
    result = runner.invoke(app, ["smallcase", "don't stop"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "Don't Stop"
