# Week 1.3, Session 2: Sales Data Statistics

# We want to analyse a set of sales data in sales.csv

# Open the file and read the data
# find the:
#   - largest sale day (highest sale amount)
#   - average sale amount
#   - the widget which has been sold the most
# and print these out in a nice, human-readable format

try:
    # Open the file and read the data
    with open("sales.csv", "r") as file:
        data = file.readlines()

    # Skip the header row
    data = data[1:]

    # Create variables for statistics
    total_sales = 0
    number_of_sales = 0
    largest_sale = 0
    largest_sale_date = ""
    product_units = {}

    # Loop through the sales data
    for row in data:
        columns = row.strip().split(",")

        date = columns[0]
        product = columns[1]
        sales_amount = int(columns[2])
        units_sold = int(columns[3])

        # Calculate total sales
        total_sales += sales_amount
        number_of_sales += 1

        # Find the largest sale
        if sales_amount > largest_sale:
            largest_sale = sales_amount
            largest_sale_date = date

        # Count units sold for each product
        if product in product_units:
            product_units[product] += units_sold
        else:
            product_units[product] = units_sold

    # Calculate average sale amount
    if number_of_sales > 0:
        average_sale = total_sales / number_of_sales

        # Find the most sold product
        most_sold_product = max(product_units, key=product_units.get)

        # Display results
        print("Sales Statistics")
        print("----------------")
        print(f"Largest sale: {largest_sale} on {largest_sale_date}")
        print(f"Average sale amount: {average_sale:.2f}")
        print(f"Most sold product: {most_sold_product}")
        print(f"Total sales: {total_sales}")

    else:
        print("No sales data found.")

except FileNotFoundError:
    print("Error: sales.csv file not found.")



# additional: you can calculate other sales statistics such as:
# - total sales for each region
# - most sold widget for each region
# - total sales for each widget


# Hints:
# - Remember to handle file errors
# - The first row contains headers: Date, Product, Sales_Amount, Units_Sold, Region
# - Sales amounts are stored as strings - you'll need to convert to int() for math
# - For finding the highest selling widget, use a dictionary to count units sold per product
# - For average, sum all sales amounts and divide by number of rows
