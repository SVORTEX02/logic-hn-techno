
print("welcome to our zomato")
print("1.Sign-Up")
print("2.Login")
print("------------------------------------------------------")

flag=False

user_choice=input("enter your choice (1/2)?").strip()
if user_choice.isalpha():
    print("kindly enter a valid choice")
elif user_choice.isdigit() and int(user_choice)>0:
    print(f"your choice- {user_choice}")
    print("------------------------------------------------------")
else:
    print(f"your choice {user_choice} is not valid try again!!")

if user_choice.isdigit() :
    if int(user_choice)==1:
        print("Directing to Sign-Up page..........")
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


# lOCATION CHOOSING HERE 
if passed:
    print("Now Please enter your location( or area):")
    print("=>Thaltej \n =>Shilaj \n =>Bopal \n =>SindhuBhavan")
    user_loc=input("enter location :").strip().lower()
    print(f"Location:{user_loc}")

    print("------------------------------------------------------")
    
    location=False

    if user_loc == "thaltej" :
        
        print("Choose your address:")
        print("1. Silver Heights Apartment, Near Pakwan Cross Road, Thaltej, Ahmedabad")
        print("2. Gala Imperia, Opp. Doordarshan Tower, Thaltej-Shilaj Road, Thaltej, Ahmedabad")
        
        print("------------------------------------------------------")
        
        
        user_thaltej = input("Enter your choice (1/2): ").strip()
        print(f"Your choice: {user_thaltej}")
        
        print("------------------------------------------------------")

        if user_thaltej.isdigit() and user_thaltej!=user_thaltej.isalpha():
                user_thaltej = int(user_thaltej)
            
                location=True
                
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

        if user_shilaj.isdigit() and user_shilaj!=user_shilaj.isalpha():
                user_shilaj = int(user_shilaj)
                
                location=True
                
                if user_shilaj == 1:
                    print("Current Location: Orchid Harmony, Near Shilaj Circle, Shilaj, Ahmedabad")
                elif user_shilaj== 2:
                    print("Current Location:Shilaj Residency, Opp. DPS School, Shilaj Road, Ahmedabad")
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

        if user_sindhu.isdigit() and user_sindhu!=user_sindhu.isalpha():
                user_sindhu= int(user_sindhu)
                
                
                location=True
                
                if user_sindhu == 1:
                    print("Current Location: Navratna Corporate Park, Sindhu Bhavan Road, Bodakdev, Ahmedabad")
                elif user_sindhu== 2:
                    print("Current Location:Iscon Emporio, Nr. Rajpath Club, Sindhu Bhavan Road, Ahmedabad")
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
        if user_bopal.isdigit() and user_bopal!=user_bopal.isalpha():
                user_bopal= int(user_bopal)
                
                location=True
                
                if user_bopal== 1:
                    print("Current Location: Safal Parisar 1, Near South Bopal Circle, Bopal, Ahmedabad")
                elif user_bopal== 2:
                    print("Current Location: Applewoods Township, S.P. Ring Road, Bopal, Ahmedabad")
                else:
                    print("Please enter a valid choice again (1 or 2)")
        else:
                print("Invalid input. Please enter 1 or 2")

    else:
        print("Sorry, we currently don't deliver to this location.")
        
        
    if location:
            print("------------------------------------------------------")
            print("Welcome to our food paradise")
            user_want=input("what you want to see ?.. \n1) membership \n2) offers \n3) dinning or delievery \n4) food on train \noptions:(1,2,3,4):=> ").strip()
            print("------------------------------------------------------")
            print(f"choice:{user_want}")
            
            payment=False
            
            
            if user_want.isalpha():
                print("Please Enter a valid choice especially from (1,2,3,4)")
            elif user_want.isdigit():
                user_want=int(user_want)
                if user_want==1:
                    print("------------------------------------------------------")
                    print("Memberships Available: \n 1)Gold-30$ \n Perks:\n-Free Delivery \n-Reduced Delivery Charges \n-Dining Out Benefits \n-Complimentary Items   \n2)Platinum-100$ \n  Perks: \n-Special Offers \n-Faster Delivery \n-Free Delivery")
                    print("------------------------------------------------------")
                    
                    
                    user_mem=input("enter your choice of membership you want (1/2) ?").strip()
                    if user_mem=="1":
                        payment=True
                    elif user_mem=="2":
                        payment=True
                    else:
                        print("enter a valid choice for obtaining membership!!")
                        payment=False
                elif user_want==2:
                    pass
                #order and dinning section -------------- 
                elif user_want==3:
                    order=False
                    user_h = input("Order or Dine-in? What’s your vibe today? \n ---for dinning press:1 and for ordering press:2=> ").strip()
                    if user_h=="1":
                        user_h1 = input("Choose your vibe for today: \n1) Rooftop Views\n2) Cozy Cafes\n3) Romantic Dining\n4) All-you-can-eat Buffet\nEnter the number that suits your mood: ").strip()
                        if user_h1.isdigit():
                            order=False
                            user_h1=int(user_h1)
                            if user_h1==1:
                                print("Top Rooftop Dining Options in Ahmedabad ")
                                print("1) Vertu - The Lounge & Terrace | SG Highway | ₹1600 for two | Popular for its skyline view, chill vibes & mocktails")
                                print("2) Spirit O Soul - The Restro Lounge | Bodakdev  | ₹1400 for two | Loved for open-air seating and live music nights")
                                
                                user_roof=input("Which place would you like to explore or book? (Enter 1 for Vertu or 2 for Spirit O Soul)").strip()
                                print(f"Choosed:{user_roof}")
                                
                                user_res=input("Awesome! What would you like to do next? 1) View Menu | 2) Book a Table").strip()
                                # y niche wla part common out krke bhi rkh skte h pn ek issue hoga k rooftop k menu aur table with guests and cafe or buffet m alg hoga isliye nhi kr rha 
                                
                                if user_res=='1':
                                        print("Starters:\n1. Paneer Tikka ₹250 | 2. Cheese Corn Balls ₹220 | 3. Peri Peri Fries ₹180")
                                        print("Main Course:\n4. Alfredo Pasta ₹290 | 5. Veg Club Sandwich ₹270 | 6. Sizzling Brownie Sizzler ₹330")
                                        print("Desserts:\n7. New York Cheesecake ₹200 | 8. Chocolate Lava Cake ₹190")
                                elif user_res=='2':
                                        # giving user the pricing of the tables 
                                        print("Table Booking Prices:\n1-2 Guests: ₹500  (Cozy Table)\n3-4 Guests: ₹900  (Family Table)\n 5-8 Guests: ₹1500 🎉 (Celebration Table)\n More than 8 Guests: ₹2500 🏢 (Party Hall)\n")
                                        guests = input("Enter number of guests: ").strip()
                                        date = input("Enter booking date dd:mm:yyyy : ").strip()
                                        time = input("Enter time : ").strip()
                                        
                                        date2 = "12-02-2024"
                                        time2 = "10:30"

                                        if len(date)==10 and date[2]=='-' and date[5]=='-' and time:
                                            print("Date format is valid and also slots are available")
                                            if date == date2:
                                                print("your date slot is available")
                                                if len(time)==5 and time[2]==":" and time.replace(":", "").isdigit():
                                                    print("Time Format is valid and also slots are available ")
                                                    if time == time2:
                                                        print("Time slot available")
                                                    else:
                                                        print(f"sorry!! we don't have a slot at this time {time}")
                                                else:
                                                    print("Please enter a valid time format")
                                            else:
                                                print(f"sorry! we don't have slots available on this date {date}")
                                        else:
                                            print("Invalid date format! Please use dd-mm-yyyy")

                                       
                                        
                                        if guests.isdigit():
                                            guests=int(guests)
                                            payment=True
                                            
                                        else:
                                            print("please number of guests in digit")        
                                            
                            elif user_h1==2:
                                print("Top Cozy Cafes in Ahmedabad:")
                                print("1) Turquoise Villa – Off C.G. Road | ₹800 for two | Known for its peaceful vibe and vintage decor ")
                                print("2) Zen Cafe – Near Gujarat University | ₹600 for two | Chill, minimalistic spot perfect for a relaxed chat ")
                                user_cafe = input("Which cozy cafe would you like to explore or book? (Enter 1 for Turquoise Villa or 2 for Zen Cafe): ").strip()
                                print(f"Choosed: {user_cafe}")
                                user_res = input("Awesome! What would you like to do next? 1) View Menu | 2) Book a Table: ").strip()
                                
                                if user_res == "1":
                                    print("Cafe Menu:")
                                    print("Beverages:\n1. Cold Coffee ₹180 | 2. Hazelnut Cappuccino ₹200 | 3. Masala Chai ₹100")
                                    print("Snacks:\n4. Veg Panini ₹220 | 5. Waffles with Ice Cream ₹250 | 6. Hummus Pita ₹190")
                                    print("Desserts:\n7. Brownie Sundae ₹230 | 8. Red Velvet Pastry ₹210")

                                elif user_res == "2":
                                    # giving user the pricing of the tables 
                                    print("Table Booking Prices:\n1-2 Guests: ₹500  (Cozy Table)\n3-4 Guests: ₹900  (Family Table)\n 5-8 Guests: ₹1500 🎉 (Celebration Table)\n More than 8 Guests: ₹2500 🏢 (Party Hall)\n")
                                    guests = input("Enter number of guests: ").strip()
                                    date = input("Enter booking date dd-mm-yyyy: ").strip()
                                    time = input("Enter time (hh:mm): ").strip()

                                    date2 = "12-02-2024"
                                    time2 = "10:30"

                                    if len(date) == 10 and date[2] == '-' and date[5] == '-' and time:
                                        print("Date format is valid and checking slots...")
                                        if date == date2:
                                            print("Your date slot is available!")
                                            if len(time) == 5 and time[2] == ":" and time.replace(":", "").isdigit():
                                                print("Time format is valid")
                                                if time == time2:
                                                    print("Time slot available")
                                                else:
                                                    print(f"Sorry! No slot at this time {time}")
                                            else:
                                                print("Please enter a valid time format")
                                        else:
                                            print(f"No slots available on {date}")
                                    else:
                                        print("Invalid date format! Use dd-mm-yyyy")

                                   

                                    if guests.isdigit():
                                        guests = int(guests)
                                        payment = True
                                    else:
                                        print("Please enter number of guests in digit")
                                        

                            elif user_h1==3:
                                print("Top Romantic Dining Spots in Ahmedabad:")
                                print("1) @Mango – Sindhu Bhavan Road | ₹1600 for two | Fairy lights, garden seating – pure romance ")
                                print("2) Earthen Oven – Fortune Landmark Hotel | ₹1800 for two | Elegant vibes with amazing North Indian cuisine ")
                                user_rom = input("Which romantic place would you like to explore or book? (Enter 1 for @Mango or 2 for Earthen Oven): ").strip()
                                print(f"Choosed: {user_rom}")
                                user_res = input("Sweet! What would you like to do next? 1) View Menu | 2) Book a Table: ").strip()
                                
                                if user_res == "1":
                                    print("Romantic Dinner Menu:")
                                    print("Starters:\n1. Stuffed Mushrooms ₹280 | 2. Tomato Basil Soup ₹200")
                                    print("Main Course:\n3. Risotto ₹420 | 4. Red Sauce Pasta ₹400 | 5. Paneer Lababdar + Naan ₹450")
                                    print("Desserts:\n6. Chocolate Fondue ₹320 | 7. Strawberry Mousse ₹300")

                                elif user_res == "2":
                                # giving user the pricing of the tables 
                                    print("Table Booking Prices:\n1-2 Guests: ₹500  (Cozy Table)\n3-4 Guests: ₹900  (Family Table)\n 5-8 Guests: ₹1500 🎉 (Celebration Table)\n More than 8 Guests: ₹2500 🏢 (Party Hall)\n")    
                                    guests = input("Enter number of guests: ").strip()
                                    date = input("Enter booking date dd-mm-yyyy: ").strip()
                                    time = input("Enter time (hh:mm): ").strip()

                                    date2 = "12-02-2024"
                                    time2 = "10:30"

                                    if len(date) == 10 and date[2] == '-' and date[5] == '-' and time:
                                        print("Checking date format & slot availability...")
                                        if date == date2:
                                            print("Date is available")
                                            if len(time) == 5 and time[2] == ":" and time.replace(":", "").isdigit():
                                                print("Time format valid")
                                                if time == time2:
                                                    print("Perfect! Slot available")
                                                else:
                                                    print(f"Oops! No slot at {time}")
                                            else:
                                                print("Time format invalid")
                                        else:
                                            print(f"Sorry, no availability on {date}")
                                    else:
                                        print("Invalid date format")

                                    print("Romantic Table Pricing:\n1-2 Guests: ₹800\n3-4 Guests: ₹1200\n5+ Guests: ₹2000")

                                    if guests.isdigit():
                                        guests = int(guests)
                                        payment = True
                                    else:
                                        print("Enter number of guests properly")

                            elif user_h1==4:
                                print("All-You-Can-Eat Buffet Places in Ahmedabad:")
                                print("1) Barbeque Nation – Drive-In Road | ₹900 per person | Live grill, unlimited starters and desserts 🔥🍖")
                                print("2) The Grand Thakar – S.G. Highway | ₹500 per person | Unlimited Gujarati Thali with royal vibes 🍛🪔")
                                user_buffet = input("Which buffet place are you heading to? (Enter 1 for Barbeque Nation or 2 for The Grand Thakar): ").strip()
                                print(f"Choosed: {user_buffet}")
                                user_res = input("Nice! What would you like to do next? 1) View Menu | 2) Book a Table: ").strip()
                                
                                
                                if user_res == "1":
                                    print("Buffet Highlights:")
                                    print("Starters:\n1. Crispy Corn ₹220 | 2. Tandoori Paneer ₹250 | 3. Nachos ₹200")
                                    print("Main Course:\n4. Dal Makhani ₹300 | 5. Butter Naan ₹40 (per piece) | 6. Hyderabadi Biryani ₹350")
                                    print("Desserts:\n7. Ice Cream Counter | 8. Gulab Jamun | 9. Chocolate Cake")

                                elif user_res == "2":
                                    # giving user the pricing of the tables 
                                    print("Table Booking Prices:\n1-2 Guests: ₹500  (Cozy Table)\n3-4 Guests: ₹900  (Family Table)\n 5-8 Guests: ₹1500 🎉 (Celebration Table)\n More than 8 Guests: ₹2500 🏢 (Party Hall)\n")
                                    guests = input("Enter number of guests: ").strip()
                                    date = input("Enter booking date dd-mm-yyyy: ").strip()
                                    time = input("Enter time (hh:mm): ").strip()

                                    date2 = "12-02-2024"
                                    time2 = "10:30"

                                    if len(date) == 10 and date[2] == '-' and date[5] == '-' and time:
                                        print("Validating your date and time...")
                                        if date == date2:
                                            print("Date slot confirmed")
                                            if len(time) == 5 and time[2] == ":" and time.replace(":", "").isdigit():
                                                print("Time format correct")
                                                if time == time2:
                                                    print("Time slot available")
                                                else:
                                                    print(f"No slot at {time}")
                                            else:
                                                print("Invalid time format")
                                        else:
                                            print(f"No availability on {date}")
                                    else:
                                        print("Invalid date format")

                                    print("Buffet Pricing Per Head:\nBarbeque Nation: ₹900\nThe Grand Thakar: ₹500")

                                    if guests.isdigit():
                                        guests = int(guests)
                                        payment = True
                                    else:
                                        print("Guests input must be numeric")

                        else:
                            print("Please enter a valid stuff from this \n\n1) Rooftop Views\n2) Cozy Cafes\n3) Romantic Dining\n4) All-you-can-eat Buffet")

                
                    elif user_h=="2":
                        
                        print("Order")
                        print("Options Available:")
                        print("1-THALI \n2-PIZZA  \n3-BIRYANI ")
                        user_h2=input("what's ur mood today? want to  order something or not!! \n for choosing from options: press(1,2,3):").strip()
                        print(f"Your mood has choosen to order:{user_h2}")
                            
                        
                        
                        if user_h2.isalpha():
                            print("Please enter a valid choice dont enter characters !!")
                        elif user_h2.isdigit():
                            user_h2=int(user_h2)
                            
                            if user_h2==1:
                                order=True
                                payment=True
                                print("Thali Availabe:\n(----North indian----)  \n(----South Indian---)")
                                user_thali=input("Which Thali you want to order \n for North indian Thali please enter 1 and For South indian Thali please Enter :2=>").strip()
                                print(f"You Choosed:{user_thali}")
                                if user_thali.isalpha():
                                    print("Please Enter a digit not character")
                                elif user_thali.isdigit():
                                    user_thali=int(user_thali)
                                    if user_thali==1:
                                        print("North Indian Thali Options \nPunjabi \nGujarati")
                                        user_north=input("For choosing punjabi thali enter 1 and for gujarati enter  2").strip()
                                        print(f"You choosed:{user_north}")
                                        if user_north.isalpha():
                                            print("please enter a digit")
                                        elif user_north.isdigit():
                                            user_north=int(user_north)
                                            if user_north==1:
                                                print("-----------------------")
                                                print("Punjabi Thali - Option 1 (Tandoori Junction) ₹349:")
                                                print("2 Butter Naan/Tandoori Roti, Paneer Butter Masala, Dal Makhani, Jeera Rice, Mixed Veg Raita, Gulab Jamun (1 pc), Salad + Pickle + Papad")

                                                print("-----------------------")
                                                print("Punjabi Thali - Option 2 (Punjabi Rasoi) ₹399:")
                                                print("2 Lachha Paratha/Missi Roti, Amritsari Chole, Shahi Paneer, Steamed Basmati Rice, Boondi Raita, Rasgulla (1 pc), Onion Salad + Pickle")

                                                print("-----------------------")
                                                user_punjabi = input("Enter 1 for Tandoori Junction or 2 for Punjabi Rasoi: ").strip()

                                                if user_punjabi== "1":
                                                    print("You selected Punjabi Thali from Tandoori Junction. ₹349 will be added to your bill.")
                                                elif user_punjabi=="2":
                                                    print("You selected Punjabi Thali from Punjabi Rasoi. ₹399 will be added to your bill.")
                                                else:
                                                    print("Invalid selection. Please choose 1 or 2.")
                                                    
                                            elif user_north==2:
                                                print("-----------------------")
                                                print("Gujarati Thali - Option 1 (Ghar Ka Swad) ₹299:")
                                                print("2 Phulka Rotis, Gujarati Kadhi, Aloo Shaak, Tuver Dal, Steamed Rice, Kachumber Salad, Chhaas, Papad, 1 Sweet (Mohanthal)")

                                                print("-----------------------")
                                                print("Gujarati Thali - Option 2 (Rajwadi Rasoi) ₹349:")
                                                print("3 Rotla/Thepla, Undhiyu, Dal Dhokli, Masala Khichdi, Kadhi, Dahi, Pickle, Farsan (Dhokla), 1 Sweet (Shrikhand)")

                                                print("-----------------------")
                                                
                                                print("-----------------------")
                                                user_gujju = input("Enter 1 for Gordhan Thal or 2 for Gopi Dining Hall: ").strip()
                                                user_gujju=int(user_gujju)
                                                if user_gujju == 1:
                                                    print("You selected Gujarati Thali from Gordhan Thal.")
                                                    print("₹320 will be added to your bill.")
                                                    print("Includes: 3 Rotis, Undhiyu, Dal, Rice, Dhokla, Kachumber Salad, Sweet (Moong Dal Halwa), Chaas")
                                                elif user_gujju == 2:
                                                    print("You selected Gujarati Thali from Gopi Dining Hall.")
                                                    print("₹299 will be added to your bill.")
                                                    print("Includes: 2 Theplas, Sev Tameta, Gujarati Kadhi, Khichdi, Farsan (Patra), Pickle, Gulab Jamun, Buttermilk")
                                                else:
                                                    print("Invalid selection. Please choose 1 or 2.")
                                                print("-----------------------")



                                            else:
                                                print("please enter a valid number to choose form punjabi or gujarati thali")
                                        else:
                                            print("please enter a valid choice out of north or south !!")
                                else:
                                    print("order cant be done because of wrong input given")
                                
                            elif user_h2==2:
                                payment=True
                                order=True
                                print("Pizza Gallery:")
                                user_pizza=input("Enter which kind of pizza do you prefer oven baked or wood-fired: \n to order oven baked please hit 1 and for wood fired baked please enter  2:=> ").strip()
                                print(f"Your choosed option: {user_pizza}")
                                user_pizza=int(user_pizza)
                                if user_pizza==1:
                                        print("Oven-Baked \n 1) Sale & Pepe:\nMenu--> 1. Classic Margherita – ₹250\n2. Veggie Loaded Pizza – ₹320")
                                        print(" 2) The Blue Oven:\nMenu--> 1. Cheese Burst Paneer Pizza – ₹300\n2. Spicy Mexican Veg Pizza – ₹340")
                                        
                                        
                                        user_oven=input("enter the choice from above two option's 1(Sale & Pepe) or 2(The Blue Oven)=>").strip()
                                        print(f"Your choice {user_oven}")
                                        
                                        if user_oven == '1':
                                            print("\nMenu--> 1. Classic Margherita – ₹250\n2. Veggie Loaded Pizza – ₹320")
                                            oven_item=input("enter the pizza you want ?? please enter 1 or 2 ").strip()
                                            print(f"Your choosen:{oven_item}")
                                            if oven_item=='1':
                                                print("YOu ordred:Classic Margherita \nBill:250 \nThank you for your order!")
                                            elif oven_item=='2':
                                                print("YOu ordred: Veggie Loaded Pizza \n Bill:320 \nThank you for your order!")
                                            else:
                                                print("Please Enter a vlaid choice from menu given")
                                        elif user_oven == '2':
                                            print("\nnMenu--> 1. Cheese Burst Paneer Pizza – ₹300\n2. Spicy Mexican Veg Pizza – ₹340")
                                            oven_item=input("enter the pizza you want ?? please enter 1 or 2 ").strip()
                                            print(f"Your choosen:{oven_item}")
                                            if oven_item=='1':
                                                print("YOu ordred:Cheese Burst Paneer Pizza \nBill:300 \nThank you for your order!")
                                            elif oven_item=='2':
                                                print("YOu ordred: Spicy Mexican Veg Pizza\n Bill:340 \nThank you for your order!")
                                            else:
                                                print("Please Enter a vlaid choice from menu given")
                                        else:
                                            print("Invalid choice. kindly enter 1 0r 2 ")
                                elif user_pizza==2:
                                        print("Wood-Fired Options: 1. The Wood Oven – Smoky Farmhouse ₹350, Rustic Margherita ₹280 \n 2. La Pino'z – Smoky Barbecue Paneer ₹360, Italian Herb Delight ₹300")
                                        
                                        user_fire=input("enter the choice from above two option's 1(The Wood Oven) or 2(La Pino'z)=>").strip()
                                        print(f"Your choice {user_fire}")
                                        
                                        if user_fire == '1':
                                            print("\nMenu--> 1. Smoky Farmhouse – ₹350\n2. Rustic Margherita – ₹280")
                                            fire_item=input("enter the pizza you want ?? please enter 1 or 2 ").strip()
                                            print(f"Your choosen:{fire_item}")
                                            if fire_item=='1':
                                                print("YOu ordred: Smoky Farmhouse \nBill:350 \nThank you for your order!")
                                            elif fire_item=='2':
                                                print("YOu ordred: Rustic Margherita \n Bill:280 \nThank you for your order!")
                                            else:
                                                print("Please Enter a vlaid choice from menu given")
                                        elif user_fire== '2':
                                            print("\nnMenu--> 2. La Pino'z Smoky Barbecue Paneer ₹360, Italian Herb Delight ₹300")
                                            fire_item=input("enter the pizza you want ?? please enter 1 or 2 ").strip()
                                            print(f"Your choosen:{fire_item}")
                                            if fire_item=='1':
                                                print("YOu ordred:Smoky Barbecue Paneer \nBill:360 \nThank you for your order!")
                                            elif fire_item=='2':
                                                print("YOu ordred: Italian Herb Delight\n Bill:300 \nThank you for your order!")
                                            else:
                                                print("Please Enter a vlaid choice from menu given")
                                        else:
                                            print("Invalid choice. kindly enter 1 0r 2 ")
                            elif user_h2==3:
                                order=True
                                payment=True
                                print("Biryani Zaika")
                                print("Biryani Options: \n1. Biryani Blues – Hyderabadi Chicken ₹280, Veg Dum Biryani ₹240 \n2. Behrouz Biryani – Murgh Makhani Biryani ₹320, Subz-E-Biryani ₹270")
                                
                                user_biryani=input("Let’s settle this like foodies — which biryani  are you going for? \n kidnly enter from 1(Biryani Blue)or2(Behrouz Biryani):=>").strip()
                                print(f"your choice:{user_biryani}")
                                
                                if user_biryani=='1':
                                    print("\nMenu--> Hyderabadi Chicken ₹280, Veg Dum Biryani ₹240")
                                    biryani_item=input("enter the biryani you want ?? please enter 1 or 2 ").strip()
                                    print(f"Your choosen:{biryani_item}")
                                    if  biryani_item=='1':
                                                print("YOu ordred:Hyderabadi Chicken \nBill:280 \nThank you for your order!")
                                    elif  biryani_item=='2':
                                                print("YOu ordred: Veg Dum Biryani\n Bill:240 \nThank you for your order!")
                                    else:
                                                print("Please Enter a vlaid choice from menu given")
                                elif user_biryani=='2':
                                        print("\nMenu-->  Murgh Makhani Biryani ₹320, Subz-E-Biryani ₹270")
                                        biryani_item=input("enter the biryani you want ?? please enter 1 or 2 ").strip()
                                        print(f"Your choosen:{ biryani_item}")
                                        if  biryani_item=='1':
                                                print("YOu ordred:Murgh Makhani Biryani  \nBill:320 \nThank you for your order!")
                                        elif  biryani_item=='2':
                                                print("YOu ordred: Subz-E-Biryani \n Bill:270 \nThank you for your order!")
                                        else:
                                                print("Please Enter a vlaid choice from menu given")
                                else:
                                    print("please enter a valid input either 1 or 2")
                                
                                
                    else:
                        print("Oops! That doesn't seem right. Please enter a valid choice ORder or Dinning")


                elif user_want==4:
                    pass
                else:
                    print("enter a valid option!!!")
                    
            balance = 10000
            if payment:
                print("balance:$10000")

                if user_want == 1:
                    print("Directing to make Payment..........")
                    if user_mem == "1":
                        gold = 30
                        print("Gold membership price: $30 \nMaking Payment.....")
                        balance -= gold
                        print(f"Payment Done \nBalance: ${balance}")
                    elif user_mem == "2":
                        platinum = 150
                        print("Platinum membership price: $150 \nMaking Payment.....")
                        balance -= platinum
                        print(f"Payment Done \nBalance: ${balance}")

                elif user_want == 2:
                    pass

                elif user_want == 3:
                    print("Here im am in the section of payemnt")
                    if order:
                        print("hello im in the order section ")
                        price=0
                        if user_h=="2":
                            if user_h2=="1":
                                if user_thali=="1" and user_north=="1":
                                    if user_punjabi=="1":
                                        price=349
                                    elif user_punjabi=="2":
                                        price=399
                                elif  user_thali=="1" and user_north=="2":
                                    if user_gujju=="1":
                                        price=299
                                    elif user_gujju=="2":
                                        price=349
                                else:
                                    print("order has not choosen yet!!!")
                            elif user_h2=="2":
                                if user_pizza=="1":
                                    if user_oven=="1" :
                                        if oven_item=="1":
                                            price=250
                                        elif oven_item=="2":
                                            price=320
                                        else:
                                            print("Wrong input/item for the order given")
                                    elif user_oven=="2":
                                        if oven_item=="1":
                                            price=300
                                        elif oven_item=="2":
                                            price=250
                                        else:
                                            print("Wrong input/item for the order given")
                                    else:
                                        print("YOu have choosen wrong oven restaurant!!")
                                elif user_pizza=="2":
                                    if user_fire=="1" :
                                        if fire_item=="1":
                                            price=350
                                        elif fire_item=="2":
                                            price=250
                                        else:
                                            print("Wrong item choosen that deosnt exist in the menu !")
                                    elif user_fire=="2":
                                        if fire_item=="1":
                                            price=360
                                        elif fire_item=="2":
                                            price=300
                                        else:
                                            print("Wrong item choosen that deosnt exist in the menu !")
                                    else:
                                        print("YOu have choosen wrong oven restaurant!!")
                                else:
                                    print("Please Choose a specific restaurant either 1 or 2")
                                
                                    
                            elif user_h2=="3":
                                if user_biryani=='1':
                                    if biryani_item=='1':
                                        price=280
                                    elif biryani_item=='2':
                                        price=240
                                    else:
                                        print("Wrong item choosen that deosnt exist in the menu !")
                                elif user_biryani=='2':
                                    if biryani_item=='1':
                                        price=320
                                    elif biryani_item=='2':
                                        price=250
                                    else:
                                        print("WRong item choosen form the menu that doesnot exist")
                                else:
                                    print("You have choosen a wrong restaurant")
                            else:
                                print("--------------------------------\npayment of order cant be proceeded !!!!!!!-------------------------------------\n")
                            
                            
                            balance -= price
                            print(f"Your order is about {price} Remaining balance: ${balance}")

                        else:
                            print("Payment cant be done because of null order")
                    else:
                        if user_h=="1":
                                if user_h1 == 1 and user_res == '2':
                                    if guests == 1 or guests == 2:
                                        price = 500
                                    elif guests == 3 or guests == 4:
                                        price = 900
                                    elif guests == 5 or guests == 8:
                                        price = 1500
                                    elif guests >= 8:
                                        price = 2500

                                    balance -= price
                                    print(f"Your table for {guests} guests is booked at Rooftop Dining. Remaining balance: ${balance}")

                                elif user_h1 == 2 and user_res == '2':
                                    if guests == 1 or guests == 2:
                                        price = 300
                                    elif guests ==3 or guests == 4:
                                        price = 700
                                    elif guests == 5 or guests == 8:
                                        price = 1100
                                    elif guests >= 8:
                                        price = 2000

                                    balance -= price
                                    print(f"Your table for {guests} guests is booked at a Cozy Cafe. Remaining balance: ${balance}")

                                elif user_h1 == 3 and user_res == '2':
                                    if guests == 1 or guests == 2:
                                        price = 600
                                    elif guests == 3 or guests == 4:
                                        price = 1000
                                    elif guests == 5 or guests == 8:
                                        price = 1800
                                    elif guests >= 8:
                                        price = 3000

                                    balance -= price
                                    print(f"Your table for {guests} guests is booked at an All You Can Eat Buffet. Remaining balance: ${balance}")
                                else:
                                    print("Payment cant be done because of null order")
        
    else:
        print("enter your location first")


    
else:
    print("please login or Sign-Up first")
    
    
    



    
        





    
