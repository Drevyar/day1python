# Use DICTIONARIES when:
# 1. You need key-value relationships
student_info = {
    "id": "12345",
    "name": "Alice",
    "courses": ["Python", "Math"],
    "gpa": 3.8
}

# 2. Fast lookups by key
phone_book = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-123-4567"
}

# 3. Counting occurrences
text = "hello world hello python"
word_count = {}
for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1
print(f"Word count: {word_count}")

# Use SETS when:
# 1. You need unique elements
email_subscribers = {"alice@email.com", "bob@email.com", "charlie@email.com"}
email_subscribers.add("alice@email.com")  # Won't add duplicate
print(f"Unique subscribers: {email_subscribers}")

# 2. Mathematical set operations
active_users = {"user1", "user2", "user3", "user4"}
premium_users = {"user2", "user4", "user5"}
active_premium = active_users & premium_users
print(f"Active premium users: {active_premium}")

# 3. Fast membership testing
valid_codes = {"A001", "B002", "C003", "D004"}
user_code = "B002"
if user_code in valid_codes:  # O(1) average time
    print("Valid code!")

# 4. Removing duplicates from lists
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5]
unique_numbers = list(set(numbers_with_duplicates))
print(f"Unique numbers: {unique_numbers}")