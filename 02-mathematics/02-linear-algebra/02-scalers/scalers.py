# --- Applicant Profile Data ---
# All attributes below are scalars (single values)
age = 30
monthly_income = 450000     # Expressed in Nigerian Naira (₦)
loan_amount = 1350000       # Expressed in Nigerian Naira (₦)
trust_score = 85            # Scaled 0 to 100

print("--- Applicant Raw Data ---")
print(f"Age: {age}")
print(f"Monthly Income: ₦{monthly_income:,.2f}")
print(f"Loan Amount: ₦{loan_amount:,.2f}")
print(f"Trust Score: {trust_score}\n")

print("--- Intermediate & Final Calculations ---")

# 1. Calculate Loan-to-Income Ratio
# Formula: loan / income
loan_to_income_ratio = loan_amount / monthly_income
print(f"1. Loan-to-Income Ratio: {loan_to_income_ratio:.2f}")

# 2. Calculate Remaining Income
# Formula: income - 100,000
remaining_income = monthly_income - 100000
print(f"2. Remaining Income after ₦100,000 payment: ₦{remaining_income:,.2f}")

# 3. Calculate Simple Weighted Score
# Formula: 0.5*(trust_score) + 0.3*(age) + 0.2*(income/100,000)
income_scaling_factor = monthly_income / 100000
weighted_score = (0.5 * trust_score) + (0.3 * age) + (0.2 * income_scaling_factor)

print(f"   - Income Scaling Factor Component: {income_scaling_factor:.2f}")
print(f"3. Final Weighted Score: {weighted_score:.2f}")
