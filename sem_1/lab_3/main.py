class HouseScheme:
    def __init__(self, count_rooms, area, bathroom_is):
        if type(count_rooms) != int or count_rooms < 0 or type(area) != int or area < 0 or type(bathroom_is) != bool:
            raise ValueError("Invalid value")
        self.count_rooms = count_rooms
        self.area = area
        self.bathroom_is = bathroom_is
    
class CountryHouse(HouseScheme):
    def __init__(self, count_rooms, area, bathroom_is, count_floors, area_site):
        super().__init__(count_rooms, area, bathroom_is)
        if type(count_floors) != int or count_floors < 0 or type(area_site) != int or area_site < 0:
            raise ValueError("Invalid value")
        self.count_floors = count_floors
        self.area_site = area_site
    def __str__(self):
        return 'Country House: Количество жилых комнат {}, Жилая площадь {}, Совмещенный санузел {}, Количество этажей {}, Площадь участка {}.'.format(self.count_rooms, self.area, self.bathroom_is, self.count_floors, self.area_site)
    def __eq__(self, other):
        if self.area == other.area and self.area_site == other.area_site and abs(self.count_floors - other.count_floors) <= 1:
            return True
        else:
            return False
            
class Apartment(HouseScheme):
    def __init__(self, count_rooms, area, bathroom_is, count_floors, windows_where):
        super().__init__(count_rooms, area, bathroom_is)
        if type(count_floors) != int or count_floors < 1 or count_floors > 15 or type(windows_where) != str or windows_where != 'N' and windows_where != 'S' and windows_where != 'W' and windows_where != 'E':
            raise ValueError("Invalid value")
        self.count_floors = count_floors
        self.windows_where = windows_where
    def __str__(self):
        return 'Apartment: Количество жилых комнат {}, Жилая площадь {}, Совмещенный санузел {}, Этаж {}, Окна выходят на {}.'.format(self.count_rooms, self.area, self.bathroom_is, self.count_floors, self.windows_where)

class CountryHouseList(list):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def append(self, p_object):
        if isinstance(p_object, CountryHouse):
            super().append(p_object)
        else:
            raise TypeError("Invalid type {}".format(type(p_object)))
    def total_square(self):
        return sum(list(map(lambda x: x.area, self)))
        
class ApartmentList(list):
    def __init__(self, name):
        super().__init__()
        self.name = name
    def extend(self, iterable):
        for i in iterable:
            if isinstance(i , Apartment):
                super().append(i)
    def floor_view(self, floors, directions):
        for i in filter(lambda x: x.count_floors >= floors[0] and x.count_floors <= floors[1] and x.windows_where in directions, self):
            print("{}: {}".format(i.windows_where, i.count_floors))
