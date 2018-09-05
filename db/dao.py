import uuid
from db.models import Customer
from db.db_access import write_to_db,read_from_db,upsert_to_db,create_client

datastore_client = create_client()

def write_customer_to_db(customer: Customer) -> bool:
    customer_dict = customer.get_db_dict()
    if not customer.id:
        customer.id = str(uuid.uuid4())

    upsert_to_db(
        datastore_client,
        Customer.db_identifier_type,
        customer.id,
        customer_dict,
        Customer.attributes_to_index)

    return True

def read_customer_from_db(customer_id) -> Customer:
    customer_dict = read_from_db(
                 datastore_client,
                 Customer.db_identifier_type,
                 customer_id
    )

    customer_object = Customer.generate_from_db_dict(customer_dict)
    return customer_object