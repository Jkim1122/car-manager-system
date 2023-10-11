class CarManager:
    all_cars = []
    total_cars = 0

    def __init__(self, color, make, model, year, mileage, services):
        self._color = color
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = services
        CarManager.total_cars += 1
        self._id = CarManager.total_cars
        CarManager.all_cars.append(self)

    def __str__(self):
        return f"Car ID:{self._id}, {self._year} {self._make} {self._model} with {self._mileage} miles. List of services:{self._services}"

    @property
    def get_id(self):
        return self._id
    @get_id.setter
    def set_id(self, new_id):
        if new_id.isnumeric():
            self._id = new_id

    @property
    def get_color(self):
        return self._color
    @get_color.setter
    def set_color(self, new_color):
        self._color = new_color

    @property
    def get_make(self):
        return self._make
    @get_make.setter
    def set_make(self, new_make):
        self._make = new_make

    @property
    def get_model(self):
        return self._model
    @get_model.setter
    def set_model(self, new_model):
        self._model = new_model

    @property
    def get_year(self):
        return self._year
    @get_year.setter
    def set_year(self, new_year):
        self._year = new_year

    @property
    def get_mileage(self):
        return self._mileage
    @get_year.setter
    def set_year(self, new_mileage):
        self._mileage = new_mileage

    @property
    def get_services(self):
        return self._services
    @get_services.setter
    def set_services(self, new_services):
        self._services.append(new_services)

def view_all_cars():
    for obj in CarManager.all_cars:
        print(obj)

def view_car_details():
    return f"Car ID:{CarManager.all_cars.get_id}"#, {CarManager.all_cars.get_year} {self._make} {self._model} with {self._mileage} miles. List of services:{self._services}"


welcome_message = """
----  WELCOME  ---- 
1. Add a car                  4. See a car's details  7. Quit
2. View all cars              5. Service a car
3. View total number of cars  6. Update mileage

"""

quit = False
while quit == False:
    user_input = input(
        f"""{welcome_message}What would you like to do? input one of the numbers to execute command: """
    )
    match user_input:
        case "1":
            color = input("Input car's color:     ")
            year = int(input("Input car's year:     "))
            make = input("Input car's make:     ")
            model = input("Input car's model:     ")
            mileage = int(input("Input car's mileage:     "))
            services = input("Input car's services:     ")
            CarManager(color, year, make, model, mileage, services)
            view_all_cars()
        case "2":
            view_all_cars()
        case "3":
            print(CarManager.total_cars)
        case "4":
            which_car = input("Enter car's ID:  ")
            for key in CarManager.all_cars:
                # print(key)
                if which_car == key:
                    view_car_details()
                    # print(f"Color: {CarManager.get_color},  Year: {CarManager.get_year}")
        case "7":
            quit = True