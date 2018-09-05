from db.models import Customer
from db.dao import write_customer_to_db,read_customer_from_db
from db.db_access import create_client

def run_test():
    customer = Customer(
        id=None,
        name='Bob',
        phone_numbers=['9535567035'],
        age=23.4,
        remarks='Retail Banking'
    )
    print (customer)
    customer_obj = write_customer_to_db(customer)

    customer_obj = read_customer_from_db(customer_obj.id)
    print (customer_obj)

    customer_obj.archived = True
    customer_obj = write_customer_to_db(customer_obj)
    print (customer_obj)


if __name__ == '__main__':
    run_test()