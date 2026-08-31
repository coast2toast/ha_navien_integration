"""Build the manually installable Home Assistant integration archive."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = "2026.06.04"
OUTPUT = ROOT / "dist" / f"navien-navilink-npe2-home-assistant-{VERSION}.zip"
COMPONENT = ROOT / "custom_components" / "navien_navilink_wh"


def main() -> None:
    """Create and verify the release archive, then print its metadata."""
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    files = [
        path
        for path in COMPONENT.rglob("*")
        if path.is_file()
        and "__pycache__" not in path.parts
        and path.suffix != ".pyc"
    ]
    files.extend(
        [ROOT / "INSTALL.md", ROOT / "README.md", ROOT / "CHANGELOG.md", ROOT / "LICENSE"]
    )

    with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, path.relative_to(ROOT).as_posix())

    with zipfile.ZipFile(OUTPUT) as archive:
        test_error = archive.testzip()
        names = archive.namelist()

    metadata = {
        "path": str(OUTPUT),
        "bytes": OUTPUT.stat().st_size,
        "sha256": hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),
        "files": len(names),
        "manifest_present": (
            "custom_components/navien_navilink_wh/manifest.json" in names
        ),
        "archive_test_error": test_error,
    }
    print(json.dumps(metadata, indent=2))


if __name__ == "__main__":
    main()
