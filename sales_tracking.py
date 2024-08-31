# sales_tracking_program.py

from SalesPerson import SalesPerson

def main():
    salesmen = []  # List to store Salesman objects

    while True:
        name = input("Enter the salesperson's name (or type 'done' to finish adding salesperson): ")
        if name.lower() == 'done':
            break
        
        salesman = SalesPerson(name)
        salesmen.append(salesman)

        while True:
            sale_input = input(f"Enter sale amount for {name} (or type 'done' to finish entering sales for this salesperson): ")
            if sale_input.lower() == 'done':
                break
            try:
                sale = float(sale_input)
                salesman.add_sale(sale)
            except ValueError:
                print("Invalid input. Please enter a numeric value for the sale amount.")

    # Display total sales for each salesman
    for salesman in salesmen:
        salesman.display_sales()
    
    # Optional: Display total sales for all salesmen combined
    total_all_sales = sum(salesman.total_sales() for salesman in salesmen)
    print(f"Total sales for all salesmen: {total_all_sales}")


# Run the main function if the script is executed
if __name__ == "__main__":
    main()
