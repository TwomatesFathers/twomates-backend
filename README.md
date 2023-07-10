# twomates-backend

# env setup
required: python >= 3.11

if you do not have poetry, install by following instructions: https://python-poetry.org/docs/
Once poetry is installed, write 
> poetry install

poetry should now set up your virtual environment.

to use python as usual, write 
> poetry run python {filename}.py

# run backend

> poetry run python twomates_backend/manage.py runserver

# Order the first order through API
Following the tutorial: 
 https://developers.printful.com/docs/#section/Make-your-first-order-through-the-API

Relevant http-requests in "http/orders" folder.
The http-request that uses this app is stored as "order-1-forwarding.http-request"

To forward orders, use the endpoint "http://localhost:8000/api/orders/", functionality specified under twomates_backend/forwarder/views.py.
See request format in http/orders/order-1-forwarding.http-request

# get an product overview
To forward orders, use the endpoint "http://localhost:8000/api/products/", functionality specified under twomates_backend/forwarder/views.py.

Also, include id to get a specific product by using the same endpoint but with an id: "http://localhost:8000/api/products/<id>"
