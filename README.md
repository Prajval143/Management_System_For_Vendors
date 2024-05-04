# Management System For Vendors

   - Application is built using Django and Django-Rest_Framework.
   - Manages Vendors , Purchase Orders and Vendors Performance by Tracking the Purchase Order

## Prerequisites :-
 
   - Python (version 3.11)
   - Django (version 5.0.4)
   - DRF (3.15.1)
   - Docker (Optional)

## Installation :-

   - Installation can be performed using the two methods :
     - A) Use the project as a Docker Container
     - B) Install project in the local machine

## Common steps :-
### Clone the repository or Download the zip file:
      bash:  
     - git clone https://github.com/Prajval143/Management_System_For_Vendors.git  
     - cd project-directory (Management_System_For_Vendors)  

# A) Use the project as a Docker Container
    - run command "docker-compose up"
    # To run test :- 
    - Open separte terminal / cmd and run following command :-
      - docker exec -it Django-Vendor-Management-System /bin/bash
      - python manage.py test
# B) Install project in the local machine
    # 1.Create a virtual environment and actiavte it using following command:
        - python -m venv venv  
        - source venv/bin/activate  # For Linux/Mac
        - venv\Scripts\activate     # For Window  

      # 2.Install dependencies:
        - pip install -r requirements.txt  

      # 3.Database setup:
        - python manage.py makemigrations  
        - python manage.py migrate  

      # 4.Usage
        - Start the server:
        - python manage.py runserver  

      # 5.Run the test suite:  
        - python manage.py test

# 2.Access API endpoints:

# PRIMARY API ENDPOINTS
1) Vendor API: /vendors/
2) Purchase Order API: /purchase-orders/  


# After creating user to get access token  
    - Use API Testing Tool like POSTMAN and URL "http://127.0.0.1:8000/api/api-token-auth/"
      also provide username and password in json e.g. { "username":"superuser","password":"superuser" } 
      to get the token. 
    - Once Token is created or received provide it to HEADER with key as Authorization 
      (e.g. key : Authorization) and value as token <received-token>  



# API Endpoints :-
   ## - Vendor API :-
   ### -: Create a new vendor.
        POST /api/vendors/ 
   ### -: List all vendors.
        GET /api/vendors/:   
   ### -: Retrieve a specific vendor's details.
        GET /api/vendors/{vendor_id}/   
   ### -: Update a vendor's details.  
        PUT /api/vendors/{vendor_id}/
   ### -: Delete a vendor
        DELETE /api/vendors/{vendor_id}/
   ### -: Vendor Performance Endpoint
        GET /api/vendors/{vendor_id}/performance

  
   ## Purchase Order API  
   ### -: Create a purchase order 
       POST /api/purchase_orders/
   ### -: List all purchase orders with an option to filter by vendor
       GET /api/purchase_orders/
   ### -: Retrieve details of a specific purchase order
       GET /api/purchase_orders/{po_id}/ 
   ### -: Update a purchase order
       PUT /api/purchase_orders/{po_id}/
   ### -: Delete a purchase order
       DELETE /api/purchase_orders/{po_id}/
   ### -: Update Acknowledgment Endpoint:  
        POST /api/purchase_orders/{po_id}/acknowledge/  


  