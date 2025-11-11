import re

input_file = "data.txt"
output_file = "extracted_emails.txt"

try:
    with open(input_file, "r") as f:
        content = f.read()

    emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", content)

    if emails:
        with open(output_file, "w") as f:
            for email in emails:
                f.write(email + "\n")
        print(f"Found {len(emails)} email(s) and saved to '{output_file}'")
    else:
        print("No email addresses found in the file.")

except FileNotFoundError:
    print(f"Error: '{input_file}' not found. Please make sure it exists in this folder.")
