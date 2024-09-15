def email_slicer(email):

    username, domain = email.split('@')

    print(f"Username: {username}")
    print(f"Domain: {domain}")



if __name__ == "__main__":
    email = input("Enter your email address: ")
    email_slicer(email)
