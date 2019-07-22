from farm_simulator import * 
import sys

class FARM_RUNNER: 
    def main_menu(self): 
        try: 
            while True: 
                self.print_main_menu()
                user_selected = int(input())
                self.call_option(user_selected) 
        except ValueError: 
            sys.exit("Goodbye!")

    def print_main_menu(self): 
        print("[1] Add a new field")
        print("[2] Harvest all fields")
        print("[3] Display a field")
        print("[4] Relax and enjoy the crops")
        print("[5] Exit")
        print("Enter a number: ")

    def call_option(self, user_selected): 
        if user_selected == 1: 
            self.add_field() 
        elif user_selected == 2: 
            self.harvest_fields() 
        elif user_selected == 3: 
            self.display_field() 
        elif user_selected == 4: 
            self.relax_and_view()
        elif user_selected == 5: 
            sys.exit("Goodbye") 


    def add_field(self): 
        type_of_field = input("Which type of field would you like to add?\n")
        area_of_field = input("What is the area of the field you are trying to create? \n")
        Farm.field(type_of_field, area_of_field)

    def harvest_fields(self): 
        print(f'\n{Farm.harvest()}\n') 
        
    def display_field(self): 
        field = input("Which field would you like to view?\n")
        print(f'\n{Farm.status(field)}\n')

    def relax_and_view(self): 
        print(Farm.relax())
    

farm = FARM_RUNNER() 
farm.main_menu() 

# farm.add_field() 
# print(Farm.fields)