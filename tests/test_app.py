from .context import thuggs

def test_app(capsys, example_fixture):

    thuggs.Thuggs.run()
    captured = capsys.readouterr()

    assert "hello world" in captured.out
