import numpy as np

applicant = np.array([
    29,
    700000,
    1500000,
    82
])

# print("Applicant:", applicant)
# print("Number of features:", applicant.shape)

applicant_2 = np.array([
    35,
    450000,
    900000,
    71
])

applicants = np.array([
    applicant,
    applicant_2
])

print(applicants)
print(applicants.shape)
