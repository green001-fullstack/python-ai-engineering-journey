value = Input("Enter score:")

score = int(value)

if score >= 90:
    print("Excellent")
elif score >= 75:
    print("Very good")
elif score >= 50:
    print("Pass")
else:
    print("Fail")
