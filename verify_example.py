"""Validate recorded evidence only; does not call Apify or start a run."""
import json
from pathlib import Path
root = Path(__file__).resolve().parent / "examples"
input_data = json.loads((root / "input.json").read_text())
output = json.loads((root / "output.json").read_text())
dataset = json.loads((root / "dataset.json").read_text())
assert input_data == {"urls": ["https://example.com/"]}
assert output["results"] == dataset
assert output["successful"] == 1 and output["unprocessed"] == 0
assert output["billing_enabled"] is False and output["confirmed_events"] == 0
assert dataset[0]["status"] == "ok" and dataset[0]["title"] == "Example Domain"
assert dataset[0]["charge_state"] == "disabled"
print("PASS: recorded input/output/dataset match; billing OFF; no network or credit use.")
