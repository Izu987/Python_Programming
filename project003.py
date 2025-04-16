"""Build a Budget App Project
"""
class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            desc = entry["description"][:23]
            amt = f"{entry['amount']:.2f}"
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # Step 1: Calculate total spend and individual spends
    spends = []
    total_spent = 0
    for category in categories:
        spent = sum(-item['amount'] for item in category.ledger if item['amount'] < 0)
        spends.append(spent)
        total_spent += spent

    # Step 2: Calculate percentage spent
    percentages = [int((spend / total_spent) * 10) * 10 for spend in spends]

    # Step 3: Create chart header
    chart = "Percentage spent by category\n"

    # Step 4: Add the bars
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for percent in percentages:
            chart += " o " if percent >= i else "   "
        chart += " \n"

    # Step 5: Bottom line
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Step 6: Add category names vertically
    max_len = max(len(c.name) for c in categories)
    for i in range(max_len):
        line = "     "
        for category in categories:
            name = category.name
            line += name[i] + "  " if i < len(name) else "   "
        if i < max_len - 1:
            line += "\n"
        chart += line

    return chart


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)