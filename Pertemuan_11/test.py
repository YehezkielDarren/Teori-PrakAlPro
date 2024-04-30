email_count = {}

def count_emails(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            if line.startswith('From: '):
                email = line.split()[1]
                email_count[email] = email_count.get(email, 0) + 1

    print_histogram(email_count)
    print_email_count(email_count)

def print_histogram(email_count):
    print('Histogram:')
    for email, count in email_count.items():
        print(f'{email:<30} {count}')

def print_email_count(email_count):
    print('\nEmail count:')
    print(email_count)

if __name__ == '__main__':
    file_name = input('Enter the name of the file: ')
    count_emails(file_name)