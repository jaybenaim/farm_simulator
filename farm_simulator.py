import random 
class Farm: 
    fields = [] 
    food_per_hectar = { 
        'corn': 20, 
        'wheat': 30
    }
    total_area = [] 
    total_food = 0 
    
    def __init__(self, type_of_field, area_of_field): 
        self.type_of_field = type_of_field 
        self.area_of_field = area_of_field
    def __string__(self): 
        return f'Total Food: {self.total_food} '
    def __repr__(self): 
        return f' Field Name: {self.type_of_field} | Area of field: {self.area_of_field} '
   
    @classmethod
    def field(cls, type_of_field, area_of_field): 
        ''' this will add the type of crop 
        and a total harvest area of the feild into the farm ''' 
        new_field = Farm(type_of_field, area_of_field)
        cls.fields.append(new_field)
        return new_field 
    @classmethod
    def harvest(cls): 
        ''' this will collect food from every feild and record how much total food you have collected
        and then display the results ''' 
        for field in cls.fields: 
            cls.total_food += field.area_of_field * Farm.food_per_hectar[field.type_of_field]
        return f'Total Food: {cls.total_food}'

    @classmethod
    def status(cls, field_to_display): 
        ''' this should show size and type
        it should also check how much food you have produced up until now ''' 
        for field in cls.fields: 
            if field.type_of_field == field_to_display: 
                return f'Name of field: {field.type_of_field}  | Area: {field.area_of_field} | Total Food: {Farm.harvest()}'
    
    @classmethod
    def relax(cls): 
        ''' this will show a random feild without harvesting ''' 
        random_field = random.choice(cls.fields)
        return random_field 

    def exit(self): 
        exit("Goodbye") 

Farm.field('corn', 2)
Farm.field('wheat', 2)

# print(Farm.fields) 
# print(Farm.harvest()) 
# print(Farm.status('corn'))
# print(Farm.relax())