from email_validator import validate_email, EmailNotValidError

# Function to extract valid emails from a given text
def extract_emails(text):
    emails = text.split()
    valid_emails = []

    for email in emails:
        try:
            # Validate the email
            v = validate_email(email)
            valid_emails.append(v.email)
        except EmailNotValidError as e:
            # This email is not valid, ignore it
            pass

    return valid_emails

# Take the filename as input
file_name = input("Enter the filename: ")

# Read the content of the file
try:
    with open(file_name, 'r') as file:
        file_content = file.read()

    # Extract and validate emails from the content
    emails = extract_emails(file_content)

    # Print the valid emails
    for email in emails:
        print(f'"{email}"')

except FileNotFoundError:
    print(f"File '{file_name}' not found. Please provide a valid filename.")
except Exception as e:
    print(f"An error occurred: {e}")
