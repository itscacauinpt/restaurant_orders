class TrackOrders:
    def __init__(self) -> None:
        self.orders = []
        self.busy_days = set()
        self.all_orders = set()

    def __len__(self):
        return len(self.orders)

    def get_customer_info(self, customer):
        customer_orders = []
        customer_days = []

        for order in self.orders:
            if order['customer'] == customer:
                customer_orders.append(order['order'])
                customer_days.append(order['day'])

        return customer_orders, customer_days

    def add_new_order(self, customer, order, day):
        self.orders.append({
            'customer': customer,
            'order': order,
            'day': day
        })

        self.busy_days.add(day)
        self.all_orders.add(order)

    def get_most_ordered_dish_per_customer(self, customer):
        customer_orders = self.get_customer_info(customer)[0]

        return max(customer_orders, key=customer_orders.count)

    def get_never_ordered_per_customer(self, customer):
        customer_orders = self.get_customer_info(customer)[0]

        return self.all_orders.difference(customer_orders)

    def get_days_never_visited_per_customer(self, customer):
        customer_days = self.get_customer_info(customer)[1]

        return self.busy_days.difference(customer_days)

    def get_busiest_day(self):
        ...

    def get_least_busy_day(self):
        pass
