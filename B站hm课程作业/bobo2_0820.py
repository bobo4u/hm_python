class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def dsecribe_restaurant(self):
        print(f'{self.restaurant_name}')
        print(f'{self.cuisine_type}')

    def open_restaurant(self):
        print(f"该餐厅正在营业")



my_restaurant = Restaurant('bobo','中餐厅')
my_restaurant.dsecribe_restaurant()
my_restaurant.open_restaurant()