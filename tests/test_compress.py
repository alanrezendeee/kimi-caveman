"""Tests for caveman-compress script."""

from caveman_mode.scripts.compress import compress_markdown, compress_line


def test_compress_line_drops_filler():
    line = "Actually, you should check the config file."
    result = compress_line(line)
    assert "Actually" not in result
    assert "you should" not in result
    assert "config file" in result


def test_compress_line_preserves_code():
    line = "    def hello():"
    result = compress_line(line)
    assert result == line


def test_compress_markdown_preserves_code_blocks():
    text = """# Title

Some text here.

```python
def hello():
    pass
```

More text.
"""
    result = compress_markdown(text)
    assert "```python" in result
    assert "def hello():" in result
    assert "```" in result


def test_compress_markdown_drops_filler():
    text = "Basically, you should actually check the file."
    result = compress_markdown(text)
    assert "Basically" not in result
    assert "actually" not in result.lower()
