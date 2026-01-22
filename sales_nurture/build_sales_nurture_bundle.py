from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path


def _read_utf8(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def build_bundle(base_dir: Path) -> dict[str, str]:
    bundle: dict[str, str] = {}

    include_ext = {".md"}
    exclude_names = {"sales_nurture_bundle.js"}

    for path in sorted(base_dir.rglob("*")):
        if not path.is_file():
            continue
        if path.name in exclude_names:
            continue
        if path.suffix not in include_ext:
            continue
        rel = path.relative_to(base_dir).as_posix()
        bundle[rel] = _read_utf8(path)

    return bundle


def patch_cache_bust_in_react_html(base_dir: Path, build_id: str) -> None:
    html_path = base_dir / "sales_nurture_react.html"
    if not html_path.exists():
        return

    text = _read_utf8(html_path)
    for fname in (
        "sales_nurture_data.js",
        "sales_nurture_bundle.js",
        "sales_nurture_doc_analyzers.js",
    ):
        # Replace existing ?v=... (if any) to force reload in file:// mode.
        pattern = rf'(src="\.\/{re.escape(fname)})(?:\?v=[^"]*)?"'
        text = re.sub(pattern, rf'\1?v={build_id}"', text)

    html_path.write_text(text, encoding="utf-8")


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    build_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    bundle = build_bundle(base_dir)
    out = base_dir / "sales_nurture_bundle.js"
    payload = json.dumps(bundle, ensure_ascii=False, sort_keys=True)
    out.write_text(
        f'window.SEGFLOW_SALES_NURTURE_BUNDLE_BUILD = "{build_id}";\n'
        f"window.SEGFLOW_SALES_NURTURE_BUNDLE = {payload};\n",
        encoding="utf-8",
    )
    patch_cache_bust_in_react_html(base_dir, build_id)
    print(f"Wrote {out} ({len(bundle)} files)")


if __name__ == "__main__":
    main()
