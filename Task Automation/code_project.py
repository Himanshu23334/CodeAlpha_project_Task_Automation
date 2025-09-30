import os
import re

# Input and output file paths
input_file = 'input.txt'
output_file = 'emails.txt'

# Email regex pattern
email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

# Check if input file exists
if os.path.isfile(input_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all email addresses
    emails = re.findall(email_pattern, content)
    unique_emails = sorted(set(emails))

    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        for email in unique_emails:
            f.write(email + '\n')

    print(f"✅ Extracted {len(unique_emails)} email(s) to '{output_file}'")
else:
    print(f"❌ File '{input_file}' not found.")