
print("welcome to our zomato")
print("1.Sign-Up")
print("2.Login")
print("------------------------------------------------------")


flag=False

user_choice=input("enter your choice (1/2)?").strip()
print(f"your choice- {user_choice}")
print("------------------------------------------------------")

if user_choice.isdigit() :
    if int(user_choice)==1:
        print("Directing to Sign-Up")
        print("------------------------------------------------------")
        flag=True
    else:
        print("Directing to Login-Page")
        print("------------------------------------------------------")
else:
    print("Please !! enter number from choice given ")
    

passed=False
if flag:
    # sign-up
    name=input("enter your name:").strip()
    set_pass=input("enter password:").strip()
    email=input("enter email:").strip()
    
    print("------------------------------------------------------")
    print("Your Details:")
    print(f"USERNAME:{name} \n PASSWORD:{set_pass}  \n EMAIL:{email}")
    passed=True
    
    
else:
    
    user_name="vortex"
    password="vortex@123"

    
    print("Loading......")
    print("------------------------------------------------------")
   


    # login
    user_input=input("enter your username:").strip()
    user_pass=input("enter your password:").strip()
    if user_input==user_name and user_pass==password:
        print("checking credentials........")
        print("------------------------------------------------------")
        print(f"hello {user_name}! welcome back ")
        passed=True
    else:
        print(f"Wrong credentials try once again")
    
print("------------------------------------------------------")

if passed:
    print("Now Please enter your location(area):")
    print("Thaltej \n Shilaj \n Bopal \n SindhuBhavan")
    user_loc=input("enter location :").strip().lower()
    print(f"Location:{user_loc}")

    print("------------------------------------------------------")

    if user_loc == "thaltej" :
        
        print("Choose your address:")
        print("1. Silver Heights Apartment, Near Pakwan Cross Road, Thaltej, Ahmedabad")
        print("2. Gala Imperia, Opp. Doordarshan Tower, Thaltej-Shilaj Road, Thaltej, Ahmedabad")
        
        print("------------------------------------------------------")
        
        
        user_thaltej = input("Enter your choice (1/2): ").strip()
        print(f"Your choice: {user_thaltej}")
        
        print("------------------------------------------------------")

        if user_thaltej.isdigit():
                user_thaltej = int(user_thaltej)
                
                if user_thaltej == 1:
                    print("Current Location: Silver Heights Apartment, Near Pakwan Cross Road, Thaltej, Ahmedabad")
                elif user_thaltej == 2:
                    print("Current Location: Gala Imperia, Opp. Doordarshan Tower, Thaltej-Shilaj Road, Thaltej, Ahmedabad")
                else:
                    print("Please enter a valid choice again (1 or 2)")
        else:
                print("Invalid input. Please enter 1 or 2")

        

    elif user_loc == "shilaj" :
        print("Choose your address:")
        print("1. Orchid Harmony, Near Shilaj Circle, Shilaj, Ahmedabad")
        print("2. Shilaj Residency, Opp. DPS School, Shilaj Road, Ahmedabad")
        print("------------------------------------------------------")
        user_shilaj = input("Enter your choice (1/2): ").strip()
        print(f"Your choice: {user_shilaj}")
        print("------------------------------------------------------")

        if user_shilaj.isdigit():
                user_shilaj = int(user_shilaj)
                
                if user_shilaj == 1:
                    print("Current Location: Orchid Harmony, Near Shilaj Circle, Shilaj, Ahmedabad")
                elif user_shilaj== 2:
                    print("Shilaj Residency, Opp. DPS School, Shilaj Road, Ahmedabad")
                else:
                    print("Please enter a valid choice again (1 or 2)")
        else:
                print("Invalid input. Please enter 1 or 2")

        

    elif user_loc == "sindhuBhavan" :
        print("Choose your address:")
        print("1. Navratna Corporate Park, Sindhu Bhavan Road, Bodakdev, Ahmedabad")
        print("2. Iscon Emporio, Nr. Rajpath Club, Sindhu Bhavan Road, Ahmedabad")
        print("------------------------------------------------------")
        user_sindhu= input("Enter your choice (1/2): ").strip()
        print(f"Your choice: {user_sindhu}")
        print("------------------------------------------------------")

        if user_sindhu.isdigit():
                user_sindhu= int(user_sindhu)
                
                if user_sindhu == 1:
                    print("Current Location: Navratna Corporate Park, Sindhu Bhavan Road, Bodakdev, Ahmedabad")
                elif user_sindhu== 2:
                    print("Iscon Emporio, Nr. Rajpath Club, Sindhu Bhavan Road, Ahmedabad")
                else:
                    print("Please enter a valid choice again (1 or 2)")
        else:
                print("Invalid input. Please enter 1 or 2")


    elif user_loc == "bopal":
        print("Choose your address:")
        print("1. Safal Parisar 1, Near South Bopal Circle, Bopal, Ahmedabad")
        print("2. Applewoods Township, S.P. Ring Road, Bopal, Ahmedabad")
        
        print("------------------------------------------------------")
        user_bopal= input("Enter your choice (1/2): ").strip()
        print(f"Your choice: {user_bopal}")
        print("------------------------------------------------------")
        if user_bopal.isdigit():
                user_bopal= int(user_bopal)
                
                if user_bopal== 1:
                    print("Current Location: Safal Parisar 1, Near South Bopal Circle, Bopal, Ahmedabad")
                elif user_bopal== 2:
                    print("Applewoods Township, S.P. Ring Road, Bopal, Ahmedabad")
                else:
                    print("Please enter a valid choice again (1 or 2)")
        else:
                print("Invalid input. Please enter 1 or 2")

    else:
        print("Sorry, we currently don't deliver to this location.")
else:
    print("please login or Sign-Up first")


    
        





    
