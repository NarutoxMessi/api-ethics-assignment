import pandas as pd
import hashlib

# Load dataset
df = pd.read_csv("sample_data.csv")

# --- Pseudonymization function ---
def hash_value(value):
    return hashlib.sha256(str(value).encode()).hexdigest()

# --- Apply transformations ---

# Drop full_name
df = df.drop(columns=["full_name"])

# Pseudonymize email
df["email"] = df["email"].apply(hash_value)

# Mask date_of_birth (keep only year)
df["date_of_birth"] = pd.to_datetime(df["date_of_birth"]).dt.year

# Mask zip_code (keep first 3 digits)
df["zip_code"] = df["zip_code"].astype(str).str[:3] + "XX"

# Optional: Keep job_title as is

# Drop diagnosis_notes (sensitive)
df = df.drop(columns=["diagnosis_notes"])

# Save processed data
df.to_csv("processed_data.csv", index=False)

print("PII handling completed successfully!")
