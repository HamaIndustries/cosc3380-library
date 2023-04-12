import urllib.parse
import random
from web import response, redirect, HTTPRequest

#dummy function
def get_report(view: str):
    """
    returns data of corresponding view on database.
    """
    query = f"SELECT * FROM library.{view};"  # passed to connection object

    info = []
    users = [
        {
            "First_name": "John",
            "Last_name": "Doe",
            "User_type": "Student",
            "User_id": random.randint(10000000, 99999999),
        },
        {
            "First_name": "Jane",
            "Last_name": "Doe",
            "User_type": "Teacher",
            "User_id": random.randint(10000000, 99999999),
        },
        {
            "First_name": "Bob",
            "Last_name": "Smith",
            "User_type": "Staff",
            "User_id": random.randint(10000000, 99999999),
        },
    ]
    products = [
        {
            "Product_type": "Book",
            "Product_name": "The Great Gatsby",
            "Product_id": random.randint(10000000, 99999999),
        },
        {
            "Product_type": "Magazine",
            "Product_name": "National Geographic",
            "Product_id": random.randint(10000000, 99999999),
        },
        {
            "Product_type": "E-Book",
            "Product_name": "To Kill a Mockingbird",
            "Product_id": random.randint(10000000, 99999999),
        },
        {
            "Product_type": "Audio Book",
            "Product_name": "Harry Potter and the Sorcerer's Stone",
            "Product_id": random.randint(10000000, 99999999),
        },
        {
            "Product_type": "DVD",
            "Product_name": "The Lord of the Rings: The Fellowship of the Ring",
            "Product_id": random.randint(10000000, 99999999),
        },
    ]
    SKU = random.randint(1000000000, 9999999999)
    TotalChecked = random.randint(0, 1000)
    fine_status = ["Paid", "Unpaid", "Lost"]
    Status = ["Checked Out", "Held", "Stock"]
    for i in range(10):
        user = random.choice(users)
        product = random.choice(products)
        fine = round(random.uniform(0.01, 50.00), 2)
        multiplier = round(random.uniform(1.00, 2.00), 2)
        cost = round(random.uniform(1.00, 50.00), 2)
        info.append(
            {
                "User_type": user["User_type"],
                "First_name": user["First_name"],
                "Last_name": user["Last_name"],
                "User_Name": user["Last_name"] + ", " + user["First_name"],
                "User_id": user["User_id"],
                "Product_type": product["Product_type"],
                "Product_name": product["Product_name"],
                "Product_id": product["Product_id"],
                "Cost": cost,
                "Fine_status": random.choice(fine_status),
                "Fine": fine,
                "Multiplier": multiplier,
                "SKU": SKU,
                "Total_Checked": TotalChecked,
                "Status": random.choice(Status),
            }
        )
    return info

def item_management_form(request: HTTPRequest):
    items = """
<!DOCTYPE html>
    <html>
<head>
	<title>Item Management</title>
</head>
<body>
	<h1>Item Management</h1>
	
	<h2>Add Item</h2>
	<form method="POST" action="/handle-new-item">
		<label for="item-name">Item Name:</label>
		<input type="text" id="item-name" name="item-name"><br>
		
		<label for="item-description">Item Description:</label>
		<textarea id="item-description" name="item-description"></textarea><br>
		
		<label for="item-price">Item Price:</label>
		<input type="number" id="item-price" name="item-price"><br>
		
		<input type="submit" value="Add Item">
	</form>
	
	<h2>Edit Item</h2>
	<form method="POST" action="/handle-edit-item">
		<label for="item-id">Item ID:</label>
		<input type="number" id="item-id" name="item-id"><br>
		
		<label for="item-name">Item Name:</label>
		<input type="text" id="item-name" name="item-name"><br>
		
		<label for="item-description">Item Description:</label>
		<textarea id="item-description" name="item-description"></textarea><br>
		
		<label for="item-price">Item Price:</label>
		<input type="number" id="item-price" name="item-price"><br>
		
		<input type="submit" value="Update Item">
	</form>
	
	<h2>Delete Item</h2>
	<form method="POST" action="/handle-delete-item">
		<label for="item-id">Item ID:</label>
		<input type="number" id="item-id" name="item-id"><br>
		
		<input type="submit" value="Delete Item">
	</form>
</body>
</html>
"""
    if request.method == 'POST':
        # handle form submission
        item_name = request.form['item-name']
        item_description = request.form['item-description']
        item_price = request.form['item-price']

        # store the values in the database or perform any other necessary operation
        # ...

        # return a response
        return response(request, "Item added successfully")

    # if it's a GET request, just return the form
    return response(request, items)

def handle_item_management_form(request: HTTPRequest):
    # Check if the form was submitted
    if request.method == 'POST':
        # Parse the form data
        if request.path == "/handle-new-item":
            item_id = request.data.get('item-id')
            item_name = request.data.get('item-name')
            item_description = request.data.get('item-description')
            item_price = request.data.get('item-price')
        # Store the values in the database / process the data (e.g. add, update, or delete items)
            items.append({
                "name": item_name,
                "description": item_description,
                "price": item_price,
            })
        # Redirect to the item management page
            return redirect(request, "/item-management")

        # Generate the redirect URL
        success = 1  # Set to 1 to indicate success
        text = f"Item '{item_name}' was successfully updated."
        redirect_url = f"/item-management?{urllib.parse.urlencode({'success': success, 'text': text})}"
        return redirect(request, redirect_url)

    # If the form was not submitted, render the form page
    return item_management_form(request)


def product_management_form (request: HTTPRequest):
    products = """<html>
<head>
	<title>Product Management</title>
</head>
<body>
	<h1>Product Management</h1>
	
	<h2>Add Product</h2>
	<form method="POST" action="/handle-add-product">
		<label for="product-name">Product Name:</label>
		<input type="text" id="product-name" name="product-name"><br>
		
		<label for="product-description">Product Description:</label>
		<textarea id="product-description" name="product-description"></textarea><br>
		
		<label for="product-price">Product Price:</label>
		<input type="number" id="product-price" name="product-price"><br>
		
		<input type="submit" value="Add Product">
	</form>
	
	<h2>Edit Product</h2>
	<form method="POST" action="/handle-edit-product">
		<label for="product-id">Product ID:</label>
		<input type="number" id="product-id" name="product-id"><br>
		
		<label for="product-name">Product Name:</label>
		<input type="text" id="product-name" name="product-name"><br>
		
		<label for="product-description">Product Description:</label>
		<textarea id="product-description" name="product-description"></textarea><br>
		
		<label for="product-price">Product Price:</label>
		<input type="number" id="product-price" name="product-price"><br>
		
		<input type="submit" value="Update Product">
	</form>
	
	<h2>Delete Product</h2>
	<form method="POST" action="/handle-delete-product">
		<label for="product-id">Product ID:</label>
		<input type="number" id="product-id" name="product-id"><br>
		
		<input type="submit" value="Delete Product">
	</form>
</body>
</html>
"""
if request.method == 'POST':
        # handle form submission
        product_name = request.form['product-name']
        product_description = request.form['product-description']
        product_price = request.form['product-price']

        # store the values in the database or perform any other necessary operation
        # ...

        # return a response
        return response(request, "Product added successfully")
    # if it's a GET request, just return the form
    return response(request, products, 200)

def handle_product_management_form(request: HTTPRequest):
    # Check if the form was submitted
    if request.method == 'POST':
        # Parse the form data
        product_id = request.data.get('product-id')
        product_name = request.data.get('product-name')
        product_description = request.data.get('product-description')
        product_price = request.data.get('product-price')

        # Process the data (e.g. add, update, or delete products)
         products.append({
            "name": product_name,
            "description": product_description,
            "price": product_price,
        })
        # Generate the redirect URL
        success = 1  # Set to 1 to indicate success
        text = f"Product '{product_name}' was successfully updated."
        redirect_url = f"/product-management?{urllib.parse.urlencode({'success': success, 'text': text})}"
        return redirect(request, redirect_url)

    # If the form was not submitted, render the form page
    return product_management_form(request)


def new_user_form (request: HTTPRequest):
    if request.method == 'POST':
        # handle form submission
        user_name = request.form['user-name']
        user_type = request.form['user-type']

        # store the values in the database or perform any other necessary operation
        # ...

        # return a response
        return response(request, "User added successfully")

    # if it's a GET request, just return the form
    newUser = """
    <html>
<head>
	<title>User Management</title>
</head>
<body>
	<h1>User Management</h1>
	
	<h2>Create User</h2>
	<form method="POST" action="/handle-new-user">
		<label for="user-name">User Name:</label>
		<input type="text" id="user-name" name="user-name"><br>
		
		<label for="user-type">User Type:</label>
		<select id="user-type" name="user-type">
			<option value="regular">Regular</option>
			<option value="staff">Staff</option>
		</select><br>
		
		<input type="submit" value="Create User">
	</form>
</body>
</html>
"""
    return response(request, newUser, 200)

def handle_new_user_form(request: HTTPRequest):
    # Check if the form was submitted
    if request.method == 'POST':
        # Parse the form data
        user_name = request.data.get('user-name')
        user_type = request.data.get('user-type')

        # Process the data (e.g. create a new user)
        users.append({
            "name": user_name,
            "type": user_type
        })
        # Generate the redirect URL
        success = 1  # Set to 1 to indicate success
        text = f"User '{user_name}' was successfully created."
        redirect_url = f"/new-user?{urllib.parse.urlencode({'success': success, 'text': text})}"
        return redirect(request, redirect_url)

    # If the form was not submitted, render the form page
    return new_user_form(request)


def generating_holds_form(request: HTTPRequest):
    # Check if the form was submitted
    if request.method == 'POST':
        # Parse the form data
        hold_name = request.data.get('hold-name')
        hold_type = request.data.get('hold-type')
        hold_duration = request.data.get('hold-duration')
        hold_reason = request.data.get('hold-reason')

        # Store the values in the database or perform any other necessary operation
        # ...

        # Generate the redirect URL
        success = 1  # Set to 1 to indicate success
        text = f"Hold '{hold_name}' was successfully generated."
        redirect_url = f"/generating-holds?{urllib.parse.urlencode({'success': success, 'text': text})}"
        return redirect(request, redirect_url)

    # If the form was not submitted, render the form page
    holds_form = """
    <html>
    <head>
        <title>Hold Generation</title>
    </head>
    <body>
        <h1>Hold Generation</h1>

        <form method="post" action="/generate-hold">
            <label for="hold-name">Hold Name:</label>
            <input type="text" id="hold-name" name="hold-name"><br>

            <label for="hold-type">Hold Type:</label>
            <select id="hold-type" name="hold-type">
                <option value="hold-type-1">Hold Type 1</option>
                <option value="hold-type-2">Hold Type 2</option>
                <option value="hold-type-3">Hold Type 3</option>
            </select><br>

            <label for="hold-duration">Hold Duration:</label>
            <input type="number" id="hold-duration" name="hold-duration"><br>

            <label for="hold-reason">Hold Reason:</label>
            <textarea id="hold-reason" name="hold-reason"></textarea><br>

            <input type="submit" value="Generate Hold">
        </form>
    </body>
    </html>
    """
    return response(request, holds_form, 200)

def handle_generating_holds_form(request: HTTPRequest):
    # Check if the form was submitted
    if request.method == 'POST':
        # Parse the form data
        hold_name = request.data.get('hold-name')
        hold_type = request.data.get('hold-type')
        hold_duration = request.data.get('hold-duration')
        hold_reason = request.data.get('hold-reason')

        # Process the data (e.g. generate the hold)

        # Generate the redirect URL
        success = 1  # Set to 1 to indicate success
        text = f"Hold '{hold_name}' was successfully generated."
        redirect_url = f"/generating-holds?{urllib.parse.urlencode({'success': success, 'text': text})}"
        return redirect(request, redirect_url)

    # If the form was not submitted, render the form page
    success = request.args.get('success')
    text = request.args.get('text')
    return generating_holds_form(request)
