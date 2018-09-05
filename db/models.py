
class Customer():
    db_identifier_type = 'Customer'
    attributes_to_index = ['id','archived','name','age','phoneNumbers']


    def __init__(self,id,name:str,phone_numbers:list,age:float,remarks:str =None,archived:bool=False):
        self.id = id
        self.name = name
        self.phone_numbers = phone_numbers
        self.age = age
        self.archived = archived
        self.remarks = remarks

    def generate_from_db_dict(customer_db_dict):
        customer_obj = Customer(
            id=customer_db_dict['id'],
            name=customer_db_dict['name'],
            phone_numbers=customer_db_dict['phoneNumbers'],
            age=customer_db_dict['age'],
            archived=customer_db_dict['archived'],
            remarks=customer_db_dict['remarks'])

        return customer_obj

    def get_db_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phoneNumbers': self.phone_numbers,
            'age': self.age,
            'archived': self.archived,
            'remarks': self.remarks
        }

    def __repr__(self):
        return "<Customer:{id}|{name}|{phone_numbers}|{age}|{archived}>".format(**{
            'id': self.id,
            'name': self.name,
            'phone_numbers': self.phone_numbers,
            'age': self.age,
            'archived': self.archived
        })

    def __str__(self):
        return self.__repr__()