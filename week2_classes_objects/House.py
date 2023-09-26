class House():
    def __init__(self, area_code, sq_ft, num_bedrms, num_bathrms, age_home, garage_code, tax_info):
        self.area_code = area_code
        self.sq_ft = sq_ft
        self.num_bathrms = num_bathrms
        self.num_bedrms = num_bedrms
        self.age_home = age_home
        self.__garage_code = garage_code
        self.__tax_info = tax_info
        
        
        
    # getters
    def get_area_code(self):
        return self.area_code
        
    def get_sq_ft(self):
        return self.sq_ft
        
    def get_num_bathrms(self):
        return self.num_bathrms
        
    def get_num_bedrms(self):
        return self.num_bedrms
        
    def get_age_home(self):
        return self.age_home
        
    #setters
    def set_area_code(self, area_code):
        self.area_code = area_code
        
    def set_sq_ft(self, sq_ft):
        self.sq_ft = sq_ft
        
    def set_num_bathrms(self, num_bathrms):
        self.num_bathrms = num_bathrms
        
    def set_num_bedrms(self, num_bedrms):
        self.num_bedrms = num_bedrms
        
    def set_age_home(self, age_home):
        self.age_home = age_home
        
    
        
our_house = House(435, 3000, 3, 5, 0, 1234, 7)

our_house.set_sq_ft(3500)

our_house.__garage_code = 2468

print(our_house.__garage_code)

print(our_house.get_sq_ft())



