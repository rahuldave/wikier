import click.testing

from wikier import console

def test_main_succeeds():
    runner = click.testing.CliRunner()
    result = runner.invoke(console.main)
    assert result.exit_code == 0
