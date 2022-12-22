from typing import List


class Pizza:
    def __init__(self, name: str, recipe: List[str], emoji: str, size: str = 'L'):
        """
        Args:
            name (str): название
            recipe (List[str]): рецепт
            emoji (str): смайлик
            size (str, optional): размер. Defaults to 'L'.
        """
        self.name = name
        self.size = size
        self.recipe = recipe
        self.emoji = emoji

    def __eq__(self, another) -> bool:
        """Метод проверки равенства двух пицц
        Returns:
            another: пицца, с который сравниваем указанную
        """
        return self.size == another.size

    def dict(self) -> dict:
        """ Метод возвращающий рецепт пиццы в виде словаря

        Returns:
            dict: рецепт пиццы словарем
        """
        return {self.name + ' ' + self.emoji: self.recipe}

    def echo(self) -> dict:
        """ Печатает ингридиенты

        Returns:
            dict: рецепт пиццы словарем
        """
        print(f"-{self.name} {self.emoji}: {', '.join(self.recipe)}")


class Margherita(Pizza):
    """Пицца маргарита."""

    def __init__(self, size: str = 'L') -> None:
        name = 'Margherita'
        emoji = '🧀'
        recipe = ['tomato sauce', 'mozzarella', 'tomatoes']
        super().__init__(name, recipe, emoji, size)


class Pepperoni(Pizza):
    """Пицца пепперони."""

    def __init__(self, size: str = 'L') -> None:
        name = 'Pepperoni'
        emoji = '🍕'
        recipe = ['tomato sauce', 'mozzarella', 'pepperoni']
        super().__init__(name, recipe, emoji, size)


class Hawaiian(Pizza):
    """Гавайская пицца."""
    def __init__(self, size: str = 'L') -> None:
        name = 'Hawaiian'
        emoji = '🍍'
        recipe = ['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
        super().__init__(name, recipe, emoji, size)
