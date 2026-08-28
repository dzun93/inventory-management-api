\# Inventory Management API



REST API for inventory management built with Django REST Framework and PostgreSQL.



The project demonstrates backend development concepts including JWT authentication, relational database design, validation, filtering, search, ordering, pagination, automated testing, and OpenAPI documentation.



\## Features



\- Product management

\- Category management

\- JWT authentication

\- Protected API endpoints

\- Product search

\- Category and status filtering

\- Price, stock, name, and date ordering

\- Pagination

\- Data validation

\- PostgreSQL integration

\- Automated API tests

\- Swagger / OpenAPI documentation



\## Tech Stack



\- Python

\- Django

\- Django REST Framework

\- PostgreSQL

\- Simple JWT

\- django-filter

\- drf-spectacular

\- Git \& GitHub



\## API Endpoints



```text

GET    /api/products/

POST   /api/products/

GET    /api/products/{id}/

PUT    /api/products/{id}/

PATCH  /api/products/{id}/

DELETE /api/products/{id}/



GET    /api/categories/

POST   /api/categories/

GET    /api/categories/{id}/

PUT    /api/categories/{id}/

PATCH  /api/categories/{id}/

DELETE /api/categories/{id}/

```



\### Authentication



```text

POST /api/token/

POST /api/token/refresh/

```



\### Documentation



```text

GET /api/docs/

GET /api/schema/

```



\## Filtering and Search



Examples:



```text

/api/products/?search=mouse

/api/products/?category=1

/api/products/?is\_active=true

/api/products/?ordering=-price

```



\## Installation



Clone the repository:



```bash

git clone https://github.com/dzun93/inventory-management-api.git

cd inventory-management-api

```



Create a virtual environment:



```bash

python -m venv venv

```



Activate it on Windows:



```bash

venv\\Scripts\\activate

```



Install dependencies:



```bash

pip install -r requirements.txt

```



Create a `.env` file based on `.env.example`:



```env

DJANGO\_SECRET\_KEY=your-secret-key

DB\_NAME=inventory\_api

DB\_USER=postgres

DB\_PASSWORD=your-password

DB\_HOST=localhost

DB\_PORT=5432

```



Create the PostgreSQL database:



```text

inventory\_api

```



Apply migrations:



```bash

python manage.py migrate

```



Run the application:



```bash

python manage.py runserver

```



\## Automated Tests



Run:



```bash

python manage.py test inventory

```



The current test suite verifies:



\- Authenticated API access

\- Rejection of unauthenticated requests

\- Product creation

\- Product price validation



\## API Documentation



Interactive Swagger documentation is available at:



```text

http://127.0.0.1:8000/api/docs/

```



\## Author



\*\*Dennis Zuniga\*\*



Computer Technology Engineering  

Python · Django · REST APIs · PostgreSQL · Git

