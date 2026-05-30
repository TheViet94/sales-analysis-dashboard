import pandas as pd
from pathlib import Path

BASE_DIR = Path(r"D:\Project\sales-analysis-dashboard")

files = [
    {
        "input": BASE_DIR / "data" / "raw" / "sales.csv",
        "output": BASE_DIR / "data" / "raw" / "sales_sample.csv",
        "rows": 10000
    },
    {
        "input": BASE_DIR / "data" / "processed" / "sales.csv",
        "output": BASE_DIR / "data" / "processed" / "sales_sample.csv",
        "rows": 10000
    },
    {
        "input": BASE_DIR / "data" / "mart" / "fact_sales.csv",
        "output": BASE_DIR / "data" / "mart" / "fact_sales_sample.csv",
        "rows": 10000
    }
]

for file in files:
    input_path = file["input"]
    output_path = file["output"]
    rows = file["rows"]

    if not input_path.exists():
        print(f"File not found: {input_path}")
        continue

    df_sample = pd.read_csv(input_path, nrows=rows)
    df_sample.to_csv(output_path, index=False, encoding="utf-8-sig")

    print(f"Created: {output_path}")

print("Done.")