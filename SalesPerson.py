class SalesPerson:
    def __init__(self, name):
        """Initialize a Salesperson object with a name and an empty list of sales"""

        self.name = name
        self.sales = []


    def add_sale(self, amount):
        """
        Add a sale amount to the salespersons record.
        :param amount: float, the amount of the sale
        """
        self.sales.append(amount)
        print(f"Sale of {amount} added for {self.name}.")

    def total_sales(self):
        """
        Calculate and return the total sales amount for the sales.
        :return: float, total sales amount
        """
        return sum(self.sales)
    
    def min_sales(self):
        """Calculate min sales"""
        return min(self.sales)
    
    def max_sales(self):
        """Calculate max sales"""
        return max(self.sales)
    
    def average_sales(self):
        """Calculate average_sales"""
        average_sales = round(sum(self.sales)/len(self.sales),2)
        return average_sales

    def display_sales(self):
        """
        Display the salespersons name and total sales.
        """
        total = self.total_sales()
        min = self.min_sales()
        max = self.max_sales()
        average = self.average_sales()
        print(f"Salesman: {self.name}\nTotal Sales: {total}\nMin Sales: {min}\nMax Sales: {max}\nAverage Sales: {average}\n")