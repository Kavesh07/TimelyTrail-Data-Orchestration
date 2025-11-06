import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os

# Use TkAgg backend for Windows so plt.show() works
matplotlib.use('TkAgg')

# === Step 1: Load dataset ===
file_path = "enriched_pii_dataset.csv"  # Change if needed

if not os.path.exists(file_path):
    print(f"❌ File not found: {file_path}")
    exit()

df = pd.read_csv(file_path)
print("✅ File loaded successfully!")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# === Step 2: Verify 'department' column exists ===
if 'department' not in df.columns:
    print("❌ Column 'department' not found in dataset.")
    print("Available columns:", df.columns.tolist())
    exit()

# === Step 3: Group data by department ===
department_counts = df['department'].value_counts().sort_values(ascending=False)

print("📊 Department-wise data distribution:")
print(department_counts)

# === Step 4: Plot pie chart of department counts ===
plt.figure(figsize=(8, 8))
plt.pie(
    department_counts.values,
    labels=department_counts.index,
    autopct='%1.1f%%',
    startangle=140,
    shadow=True
)
plt.title("Distribution of Data Entries by Department")
plt.tight_layout()

# === Step 5: Save and show chart ===
output_file = "department_distribution_pie.png"
plt.savefig(output_file)
print(f"✅ Pie chart saved as: {output_file}")

plt.show()
