import argparse


def get_console_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('price', help='Enter a price.')
    arguments = parser.parse_args()
    return arguments


def format_price(price):
    if type(price) == bool:
        return None
    try:
        real_num_price = float(price)
    except (TypeError, ValueError):
        return None
    rounded_price = round(real_num_price, 2)
    if rounded_price.is_integer():
        formatted_price = '{:,.0f}'.format(rounded_price).replace(',', ' ')
    else:
        formatted_price = '{:,}'.format(rounded_price).replace(',', ' ')
    return formatted_price


if __name__ == '__main__':
    console_arguments = get_console_arguments()
    price = console_arguments.price
    formatted_price = format_price(price)
    print(formatted_price)
