import click
from random import randint
from pizza import Hawaiian, Pepperoni, Margherita, Pizza


def log(message: str):
    """
    Декоратор для вывода сообщений о статусе пиццы
    """
    def log_decorator(func):
        def wrapper(*args):
            rand_time = randint(10, 20)
            ret_val = func(*args)
            print(message.format(rand_time))
            # print(func.__name__)
            return ret_val
        return wrapper

    return log_decorator


@log('🍳 Пиццу приготовили за {} сек')
def bake(pizza: Pizza) -> None:
    """Приготовление пиццы"""
    print(f'Готовится пицца {pizza.name}')
    pass


@log('🛵 Пиццу доставили за {} сек')
def deliver(pizza: Pizza) -> None:
    """Доставка пиццы"""
    pass


@log('🏠 Пиццу забрали за {} сек')
def pickup(pizza: Pizza) -> None:
    """Самовывоз пиццы"""
    pass


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
@click.option('--size', default='L', type=str)
def order(pizza: str, delivery: bool, size: str = 'L'):
    """Готовит и доставляет пиццу"""
    pizza_dict = {
        "margerita": Margherita(size),
        "pepperoni": Pepperoni(size),
        "hawaiian": Hawaiian(size)
    }
    if pizza in pizza_dict:
        bake(pizza_dict[pizza])

        if delivery:
            deliver(pizza_dict[pizza])
        else:
            pickup(pizza_dict[pizza])


@cli.command()
def menu():
    Margherita().echo()
    Pepperoni().echo()
    Hawaiian().echo()


if __name__ == '__main__':
    # print(Pepperoni(size="XL")==Pepperoni(size="XL"))
    cli()
