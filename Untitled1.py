import pandas as pd


# --- Step 1: Load the dataset ---
df = pd.read_csv("C:\\Users\\akila\\OneDrive\\Desktop\\imputer module.csv")
print("Original Dataset:\n", df)
print("\nMissing Value Count:\n", df.isnull().sum())

# --- Step 2: Basic Numerical Imputation (Mean) ---
def impute_numerical_mean(df):
    for col in df.select_dtypes(include=['float64', 'int64']).columns:
        mean_value = df[col].mean()
        df[col]=df[col].fillna(mean_value)
        print(f"[INFO] Filled missing values in {col} with mean: {mean_value}")
    return df

# --- Step 3: Categorical Imputation (Mode) ---
def impute_categorical_mode(df):
    for col in df.select_dtypes(include=['object']).columns:
        mode_value = df[col].mode()[0]  # most frequent value
        df[col] = df[col].fillna(mode_value)
        print(f"[INFO] Filled missing values in {col} with mode: {mode_value}")
    return df



# --- Step 4: Run Imputation ---
df = impute_numerical_mean(df)       # Step 1: Mean Imputation
df = impute_categorical_mode(df)     # Step 2: Mode Imputation


print("\nCleaned Dataset:\n", df)

# --- Step 5: Save Cleaned Data ---
df.to_csv("cleaned_data.csv", index=False)
print("\n Cleaned dataset saved as cleaned_data.csv")

# --- Step 6: Summary Report ---
missing_summary = df.isnull().sum()
print("\nSummary Report After Handling Missing Data :\n")
print(missing_summary)
print("\n All missing values handled successfully!")


