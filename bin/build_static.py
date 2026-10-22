"""Build a copy of the dashboard that works without a server (for a static host).

The model coefficients and the metrics are put inside the page, so it needs nothing else.
Run from the project root (after `make train`): python bin/build_static.py
The result is dist/abalone/index.html
"""

import json
from pathlib import Path

from src.web_service.main import DASHBOARD, metrics, model_info

OUT = Path("dist/abalone/index.html")

data = json.dumps({"model": model_info(), "metrics": metrics()})
html = DASHBOARD.read_text()
# the data must be defined before the page script runs
html = html.replace("<script>", f"<script>window.STATIC_DATA = {data};</script>\n<script>", 1)

OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(html)
print(f"Written {OUT} ({len(html) // 1024} KB), upload this folder to your site as /abalone/")
