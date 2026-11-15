import pytest

from .fixed import artifact_path


def test_nested_artifact_stays_inside_root(tmp_path):
    path = artifact_path(str(tmp_path), "exports/2026/report.csv")
    assert path.parent == (tmp_path / "exports/2026").resolve()


@pytest.mark.parametrize("name", ["../secrets.env", "nested/../../secrets.env", "\x00bad"])
def test_traversal_and_null_bytes_are_rejected(tmp_path, name):
    with pytest.raises(ValueError):
        artifact_path(str(tmp_path), name)
