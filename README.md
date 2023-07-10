# twomates-backend

# env setup
required: python >= 3.11

if you do not have poetry, install by following instructions: https://python-poetry.org/docs/
Once poetry is installed, write 
> poetry install

poetry should now set up your virtual environment.

to use python as usual, write 
> poetry run python {filename}.py



# Order the first order through API
Following the tutorial: 
 https://developers.printful.com/docs/#section/Make-your-first-order-through-the-API

Relevant http-requests in "http" folder.
The http-request that uses this app is stored as "order-1-forwarding.http-request"

To forward orders, use the endpoint "http://localhost:8000/api/orders", functionality specified under twomates_backend/forward_order/views.py.
See request format in order-1-forwarding.http-request.

# run backend

> poetry run python twomates_backend/manage.py runserver