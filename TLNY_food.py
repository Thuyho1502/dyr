
import random
print("Welcome to TLNY food\n")
print("""How can TLNY food help you?")
 Whether are you wondering about the food that you are going to enjoy with your family.
        """)
print("Do you want TNLY FOOD help you to do it easier? ")
choice =input("yes or no:")
while True:
    if choice =="no":
        break
    elif choice=='yes':
        print(" Have you had your own food?")
        ans=input()
    
        while True:
            if ans=='yes':
                print('Let me know which food that you are wondering')
                print("Each dishes will separated by a space.")
                print("For example: bo_kho ca_chien nuong ")
                food=(input("Enter your dishes list:"))
                food_list=food.split()
                random_list_food=random.choice(food_list)
                print(random_list_food)
              
                break
            elif ans=="no":


                print("TLNY FOOD have a lot of suggestion about dishes that you can consider")
                print('How are you think about this dish:')
                TLNY_food=["Boiled Chicken","Sticky rice cake","Jellied meat","Dried bamboo shoot soup","Spring roll","steammed sticky rice","Lean pork paste","Pig trotters","Pork belly","Fermented pork","Pork stuffed bitter melon soup","Meate stwed in cocony juice","Steamed momordica sweet rice"]
                print(random.sample(TLNY_food,1))
                break
            else:
                print("It has something mistake")
                break
        break

               
            
             



