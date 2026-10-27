
from datetime import datetime, timezone


def generate_report():
    now = datetime.now(timezone.utc)

    report = {
        "task": "Daily Business Report",
        "generated_at_utc": now.strftime("%Y-%m-%d %H:%M:%S"),
        "total_orders": 128,
        "total_revenue": 25600,
        "status": "success",
    }

    print("=" * 40)
    print("Business Report")
    print("=" * 40)

    for key, value in report.items():
        print(f"{key}: {value}")

    print("=" * 40)


if __name__ == "__main__":
    generate_report()
