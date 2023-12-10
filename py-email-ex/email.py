import re

# Function to extract emails from a given text
def extract_emails(text):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(pattern, text)

# Read the content of the file
with open('Trident_EP_Dehash.txt', 'r') as file:
    file_content = file.read()

# Extract emails from the content
emails = extract_emails(file_content)

# Print the emails
for email in emails:
    print(f'"{email}"')
