base_price = 15

# Get user age first to determine eligibility
age = int(input("Enter your age: "))

if age < 18:
    print("You are not eligible to book a ticket (must be at least 18).")
    print("Ticket booking failed due to restrictions.")
else:
    print("You are eligible to book a ticket.")
    
    show_time = input("Enter show time (Matinee/Evening): ").strip().capitalize()
    
    # Evening shows strictly require age 21 or older
    if show_time == 'Evening' and age < 21:
        print("You are not eligible for Evening shows (must be 21+).")
        print("Ticket booking failed due to restrictions.")
    else:
        if age >= 21:
            print("User is eligible for Evening shows.")
            
        seat_type = input("Enter seat type (Premium/Gold/Regular): ").strip().capitalize()
        is_member = input("Are you a member? (yes/no): ").strip().lower() == 'yes'
        is_weekend = input("Is it a weekend? (yes/no): ").strip().lower() == 'yes'

        # Discount check (Only for members aged 21+)
        discount = 0
        if is_member and age >= 21:
            discount = 3
            print("You  are qualified for membership discount")
        else:
            print("You do not qualify for membership discount")
        print(f"Discount: ${discount}")

        # Extra charges check (Weekend or Evening show)
        extra_charges = 0
        if is_weekend or show_time == 'Evening':
            extra_charges = 2
            print("Extra charges will be applied")
        else:
            print("No extra charges will be applied")
        print(f"Extra charges: ${extra_charges}")

        # Service charges check
        if seat_type == 'Premium':
            service_charges = 5
        elif seat_type == 'Gold':
            service_charges = 3
        else:
            service_charges = 1
        print(f"Service charges: ${service_charges}")

        # Calculate final price
        final_price = base_price + service_charges + extra_charges - discount
        
        print("\nTicket booking condition satisfied")
        print(f"Final price of ticket: ${final_price}")