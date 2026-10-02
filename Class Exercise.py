class Car:
    dealership_Name="Yazbeck Motor Company"
    total_cars=0

    def _init_(self,make,model,year, vin,
               price, is_sold,mileage,color ):
        self.make = make
        self.model = model
        self.year = year
        self.vin = vin
        self.price = price
        self.is_sold = is_sold
        self.mileage = mileage
        self.color = color

        car.total_car +=1

        def get_car_info(self):
            print(f"make:{self.make}")
            print(f"model:{self.model}")
            print(f"year:{self.year}")
            print(f"vin:{self.vin}")
            print(f"price:{self.price}")
            print(f"is_sold:{self.is_sold}")
            print(f"mileage:{self.mileage}")
            print(f"color:{self.color}")

            def sell_car(self):
                self.is_sold = True

            def update_price(self, new_price):
                self.price = new_price
                self.get_car_info

            def is_available(self):
                if not is_sold:
                    True
                else:
                    False

            def update_mileage(self,new_mileage):
                self.mileage += new_mileage
                self.get_car_info

            @classmethod
            def get_dealership_name(cls):
                return f"dealership name:{cls.dealership_name}"
            @classmethod
            def get_total_cas(cls):
                return f"total cars #:{cls.total_cars}"

