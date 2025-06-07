#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        if not isinstance(discount, int) or not (0 <= discount <= 100):
            print("Not valid discount")
            self.discount = 0
        else:
            self.discount = discount

        self.total = 0
        self.items = []
        self.previous_transactions = []

    def add_item(self, item, price, quantity=1):
        self.total += price * quantity
        self.items.extend([item] * quantity)
        self.previous_transactions.append({
            "item": item,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if not self.previous_transactions:
            print("There is no discount to apply.")
            return

        discount_amount = self.total * (self.discount / 100)
        self.total -= discount_amount
        print(f"After the discount, the total comes to ${self.total:.2f}")

    def void_last_transaction(self):
        if self.previous_transactions:
            last_transaction = self.previous_transactions.pop()
            item = last_transaction["item"]
            price = last_transaction["price"]
            quantity = last_transaction["quantity"]

            self.total -= price * quantity
            for _ in range(quantity):
                if item in self.items:
                    self.items.remove(item)
        else:
            print("No transaction to void.")
