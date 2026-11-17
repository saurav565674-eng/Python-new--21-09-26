
lines = [
    ' asha VERMA ; ASHA.V@Example.COM ; +91 98765-43210 ;pune ',
    'ravi kumar;ravi@@corp.in;9123456780;Mumbai',
    'meera;meera@mail;9123456780;Delhi',
    'john doe; john@x.org ;12345; Goa',
    'Neha Rao;neha.rao@firm.co.in;919876501234;nashik',
    'amit;amit@site.com;9876543210'
]


def clean_customer(raw):

    # Split record
    data = raw.split(';')

    # Check exactly 4 fields
    if len(data) != 4:
        return None

    name = data[0].strip()
    email = data[1].strip().lower()
    phone = data[2].strip()
    city = data[3].strip()

    # A. Validate Name
    name = " ".join(name.split())

    if name == "":
        return None

    words = name.split()

    for word in words:
        if not word.isalpha():
            return None

    name = name.title()

    # Validate City
    if city == "":
        return None

    city = city.title()

    # B. Validate Email
    if email.count('@') != 1:
        return None

    parts = email.split('@')

    username = parts[0]
    domain = parts[1]

    if username == "":
        return None

    if '.' not in domain:
        return None

    if domain.startswith('.') or domain.endswith('.'):
        return None

    # C. Validate Phone Number
    phone = phone.replace(" ", "")
    phone = phone.replace("-", "")

    if phone.startswith('+91'):
        phone = phone[3:]

    elif phone.startswith('91') and len(phone) == 12:
        phone = phone[2:]

    if not phone.isdigit():
        return None

    if len(phone) != 10:
        return None

    if phone[0] not in '6789':
        return None

    # Return valid customer
    return {
        'name': name,
        'email': email,
        'phone': phone,
        'city': city
    }


# Process all records
rejected = 0

for raw in lines:

    result = clean_customer(raw)

    if result is not None:
        print(result)

    else:
        rejected += 1

print("Rejected:", rejected)



