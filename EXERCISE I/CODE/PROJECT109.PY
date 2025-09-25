# ---------- INTEGERS ----------
feedback_scores = [78, 85, 90, 66, 74, 92, 88, 81]  # Sample course feedback ratings (out of 100)

total_score = sum(feedback_scores)
average_score = total_score / len(feedback_scores)
min_score = min(feedback_scores)
max_score = max(feedback_scores)

# ---------- STRINGS ----------
report = (
    f"Course Feedback Report:\n"
    f"Total Feedback Score: {total_score}\n"
    f"Average Feedback Score: {average_score:.2f}\n"
    f"Minimum Score: {min_score}\n"
    f"Maximum Score: {max_score}"
)
print(report)

# ---------- BOOLEANS ----------
threshold = 80
if average_score > threshold and max_score >= 90:
    print("Status: Above Standard ✅")
else:
    print("Status: Below Standard ❌")

# ---------- LISTS ----------
print("\nOriginal Feedback List:", feedback_scores)

# Add a new feedback rating
feedback_scores.append(79)

# Remove scores below 70
feedback_scores = [score for score in feedback_scores if score >= 70]

# Sort the list
feedback_scores.sort()
print("Modified Feedback List:", feedback_scores)

# ---------- ARRAYS ----------
from array import array

# Create an array from first 5 elements
feedback_array = array('i', feedback_scores[:5])

array_sum = sum(feedback_array)
list_sum = sum(feedback_scores)

print(f"\nArray Sum: {array_sum}")
print(f"List Sum: {list_sum}")
print("Array matches List subset sum:", array_sum == sum(feedback_scores[:5]))

# ---------- DICTIONARIES ----------
feedback_records = [
    {"id": 1, "name": "Alice", "value": 85},
    {"id": 2, "name": "Bob", "value": 90},
    {"id": 3, "name": "Charlie", "value": 78},
    {"id": 4, "name": "Diana", "value": 66},
]

# Update Charlie's score
for record in feedback_records:
    if record["name"] == "Charlie":
        record["value"] = 82

# Remove Diana's record
feedback_records = [r for r in feedback_records if r["name"] != "Diana"]

# Total value
total_dict_score = sum(r["value"] for r in feedback_records)

print("\nUpdated Feedback Records:")
for r in feedback_records:
    print(r)

print(f"Total Score from Dictionary Records: {total_dict_score}")
