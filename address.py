#!/usr/bin/env python3.10

# Created by: Nicolas Riscalas
# Created on: May 12 2022
# Formats an address


def get_address(name, street_address, city, province, postal_code, apt_number=None):
    # return the address in capital letters

    address = name + "\n"
    if apt_number is not None:
        address = address + apt_number + "-"
    address = (
        address + street_address + "\n" + city + " " + province + " " + postal_code
    )

    return address.upper()


def main():

    apt_number = None

    user_name = input("Enter your name: ")
    street_address = input("Enter your street address: ")
    question = input("Do you have an apartment number? (y/n): ")
    if question.upper() == "Y" or question.upper() == "YES":
        apt_number = input("Enter your apartment number: ")
    city = input("Enter your city: ")
    province = input("Enter your province: ")
    postal_code = input("Enter your postal code: ")
    print("")

    if apt_number is not None:
        address = get_address(
            user_name, city, province, street_address, postal_code, apt_number
        )
    else:
        address = get_address(user_name, city, province, street_address, postal_code)
    print(address)


if __name__ == "__main__":
    main()
