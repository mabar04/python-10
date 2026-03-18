from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    if operation == "add":
        return reduce(add, spells)
    elif operation == "multiply":
        return reduce(mul, spells)
    elif operation == "max":
        return reduce(lambda a, b: a if a > b else b, spells)
    elif operation == "min":
        return reduce(lambda a, b: a if a < b else b, spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant":      partial(base_enchantment, 50, "fire"),
        "ice_enchant":       partial(base_enchantment, 50, "ice"),
        "lightning_enchant": partial(base_enchantment, 50, "lightning"),
    }


@lru_cache(maxsize=300)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @singledispatch
    def spell(target):
        return f"Unknown spell on {target}"

    @spell.register(int)
    def _(target):
        return f"Damage spell: {target} damage dealt!"

    @spell.register(str)
    def _(target):
        return f"Enchantment cast on {target}!"

    @spell.register(list)
    def _(target):
        multi_cast = [spell(e) for e in target]
        return "Multi-cast:\n" + "\n".join(multi_cast)

    return spell


def base_enchantment(power, element, target):
    return (f"{element} enchantment of power "
            f"{power} hits {target}!")


if __name__ == "__main__":

    print("Testing spell reducer...")
    spells = [10, 20, 30, 40]
    print(f"  Sum:      {spell_reducer(spells, 'add')}")
    print(f"  Product:  {spell_reducer(spells, 'multiply')}")
    print(f"  Max:      {spell_reducer(spells, 'max')}")
    print(f"  Min:      {spell_reducer(spells, 'min')}")

    print("\nTesting partial enchanter...")

    enchants = partial_enchanter(base_enchantment)
    print(f"  {enchants['fire_enchant']('Dragon')}")
    print(f"  {enchants['ice_enchant']('Goblin')}")
    print(f"  {enchants['lightning_enchant']('Troll')}")

    print("\nTesting memoized fibonacci...")
    print(f"  Fib(10): {memoized_fibonacci(10)}")
    print(f"  Fib(15): {memoized_fibonacci(15)}")
    print(f"  Fib(30): {memoized_fibonacci(30)}")
    print(f"  Cache info: {memoized_fibonacci.cache_info()}")

    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    print(f"  {spell(100)}")
    print(f"  {spell('Excalibur')}")
    print(f"  {spell([50, 'Shield', 30])}")
