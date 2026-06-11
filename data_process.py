import csv
import os

# Current script directory
DATA_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "data"
)
OUTPUT_FILE = os.path.join(DATA_DIR, "formatted_output.csv")
TARGET_PRODUCT = "Pink Morsel"

output_fields = ["sales", "date", "region"]

print("Starting data aggregation and filtering...")

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=output_fields)

    writer.writeheader()

    for filename in os.listdir(DATA_DIR):

        # Process only source CSV files
        if filename.endswith(".csv") and filename != "formatted_output.csv":

            file_path = os.path.join(DATA_DIR, filename)

            print(f"Processing {filename}")

            with open(file_path, "r", newline="", encoding="utf-8") as infile:

                reader = csv.DictReader(infile)

                for row in reader:

                    if row["product"].strip().lower() == TARGET_PRODUCT.lower():

                        price = float(row["price"].replace("$", ""))
                        quantity = int(row["quantity"])

                        sales = price * quantity

                        writer.writerow({
                            "sales": round(sales, 2),
                            "date": row["date"],
                            "region": row["region"]
                        })

print("Success! formatted_output.csv created.")