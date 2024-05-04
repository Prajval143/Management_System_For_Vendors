# vendor-management-system-django

Develop a Vendor Management System using Django and Django REST Framework. This
system will handle vendor profiles, track purchase orders, and calculate vendor performance
metrics

## Prerequisites

- Python (version 3.11)
- Django (version 5.0.4)
- DRF (3.15.1)

## Installation

# 1. Clone the repository:
   bash:  
   git clone https://github.com/Prajval143/Management_System_For_Vendors.git  
   cd project-directory (Management_System_For_Vendors)  

# 2.Create a virtual environment:
python -m venv venv  
source venv/bin/activate  # For Linux/Mac  
venv\Scripts\activate     # For Windows  

# 3.Install dependencies:
pip install -r requirements.txt  

# 4.Database setup:
python manage.py makemigrations  
python manage.py migrate  

## Usage
# 1.Start the server:
python manage.py runserver  

# 2.Access API endpoints:

# PRIMARY API ENDPOINTS
1) Vendor API: /vendor/
2) Purchase Order API: /purchase-order/  


# After creating user to get access token  
Use API Testing Tool like POSTMAN and URL "http://127.0.0.1:8000/api/api-token-auth/"
also provide username and password in json e.g. { "username":"superuser","password":"superuser" } 
once Token is created or received provide it to HEADER  
with key as Authorization (e.g. key : Authorization) and value as token <received-token>  



## API Endpoints
1) Vendor API 
● POST /api/vendors/: Create a new vendor.  
● GET /api/vendors/: List all vendors.  
● GET /api/vendors/{vendor_id}/: Retrieve a specific vendor's details.  
● PUT /api/vendors/{vendor_id}/: Update a vendor's details.  
● DELETE /api/vendors/{vendor_id}/: Delete a vendor
● Vendor Performance Endpoint (GET /api/vendors/{vendor_id}/performance)

2) Purchase Order API  
● POST /api/purchase_orders/: Create a purchase order.   
● GET /api/purchase_orders/: List all purchase orders with an option to filter by vendor.   
● GET /api/purchase_orders/{po_id}/: Retrieve details of a specific purchase order.   
● PUT /api/purchase_orders/{po_id}/: Update a purchase order.  
● DELETE /api/purchase_orders/{po_id}/: Delete a purchase order   
  
3) Vendor Performance Evaluation  
● GET /api/vendors/{vendor_id}/performance: Retrieve a vendor's performance metrics

4) Update Acknowledgment Endpoint:  
● POST /api/purchase_orders/{po_id}/acknowledge for vendors to acknowledge POs.  


## Running Tests  
Run the test suite:  
  python manage.py test