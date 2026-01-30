from __future__ import annotations
from pathlib import Path
import duckdb

RAW_DIR = Path("data/raw")
OUT_DIR = Path("data/processed")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def run_etl() -> None:
    train = RAW_DIR / "train.csv"
    transactions = RAW_DIR / "transactions.csv"
    stores = RAW_DIR / "stores.csv"

    missing = [p for p in [train, transactions, stores] if not p.exists()]
    if missing:
        raise FileNotFoundError(
            "Missing files in data/raw: " + ", ".join(str(m) for m in missing)
        )

    con = duckdb.connect(database=":memory:")

    query = """
    WITH sales_per_store_day AS (
        SELECT
            store_nbr,
            CAST(date AS DATE) AS date,
            SUM(sales) AS daily_sales
        FROM read_csv_auto(?, HEADER=TRUE)
        GROUP BY 1,2
    ),
    active_days AS (
        SELECT
            store_nbr,
            CAST(date AS DATE) AS date,
            transactions
        FROM read_csv_auto(?, HEADER=TRUE)
    ),
    aligned AS (
        SELECT
            a.store_nbr,
            a.date,
            a.transactions,
            COALESCE(s.daily_sales, 0) AS daily_sales
        FROM active_days a
        LEFT JOIN sales_per_store_day s
          ON a.store_nbr = s.store_nbr AND a.date = s.date
    ),
    store_features AS (
        SELECT
            store_nbr,
            COUNT(*) AS active_days,
            AVG(transactions) AS avg_transactions,
            AVG(daily_sales) AS avg_daily_sales,
            SUM(daily_sales) AS total_sales_active
        FROM aligned
        GROUP BY 1
    )
    SELECT
        f.store_nbr,
        s.city,
        s.type,
        f.active_days,
        f.avg_transactions,
        f.avg_daily_sales,
        CASE WHEN f.avg_transactions = 0 THEN NULL
             ELSE f.avg_daily_sales / f.avg_transactions
        END AS basket_units
    FROM store_features f
    LEFT JOIN read_csv_auto(?, HEADER=TRUE) s
      ON f.store_nbr = s.store_nbr
    ORDER BY f.store_nbr
    """

    df = con.execute(query, [str(train), str(transactions), str(stores)]).df()

    out_csv = OUT_DIR / "store_kpis.csv"
    df.to_csv(out_csv, index=False)

    print("✅ ETL OK ->", out_csv)

if __name__ == "__main__":
    run_etl()
