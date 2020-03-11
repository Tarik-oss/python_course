# такий вид написання змінних можливий
# однак, можна спростити назву
# price_of_the_cheese -> cheesePrice або cheese_price

price_of_the_chesse = int(input('Enter price of the chesse: '))
# Добре було б робити перевірки на коректність значення з підказкою що трапилося
# це можна робити як з if, так і через assert

for weight in range(50, 1050, 50):
    # розрахунок ціни за шматок можна винести за межі циклу
    # він буде однаковий завжди і після ми можемо його помножити на вагу
    # price_for_the_weight -> price_per_weight
    price_for_the_weight = price_of_the_chesse * weight / 1000
    #ця стрічка поміщається в 120 символів, тому її можна не ділити на 2
    print('Weight of the chesse {0} gr. and how much coast {1} grn'.format(weight, price_for_the_weight))
