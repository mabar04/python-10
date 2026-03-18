from typing import Any


def mage_counter() -> callable:
    count = 0

    def count_calls():
        nonlocal count
        count += 1
        return count
    return count_calls


def spell_accumulator(initial_power: int) -> callable:
    power = initial_power

    def accumulate(amount: int) -> int:
        nonlocal power
        power += amount
        return power

    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(name: str) -> str:
        return f"{enchantment_type} {name}"
    return enchant


def memory_vault() -> dict[str, callable]:
    memories = {}

    def store(key: str, value) -> None:
        memories[key] = value

    def recall(key: str) -> Any:
        return memories.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":

    print("Testing mage counter...")
    counter = mage_counter()
    print(f"  Call 1: {counter()}")
    print(f"  Call 2: {counter()}")
    print(f"  Call 3: {counter()}")

    counter2 = mage_counter()
    print(f"  New counter starts fresh: {counter2()}")
    print(f"  Original counter keeps going: {counter()}")

    print("\nTesting spell accumulator...")
    accumulator = spell_accumulator(100)
    print("  Initial power: 100")
    print(f"  After +10:  {accumulator(10)}")
    print(f"  After +25:  {accumulator(25)}")
    print(f"  After +50:  {accumulator(50)}")
    mage2 = spell_accumulator(50)
    print(f"  Independent mage starts at 50, after +10: {mage2(10)}")
    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    electric = enchantment_factory("Electric")
    print(f"  {flaming('Sword')}")
    print(f"  {frozen('Shield')}")
    print(f"  {electric('Staff')}")
    items = ["Sword", "Shield", "Staff"]
    enchanted = list(map(flaming, items))
    print(f"  Map all with flaming: {enchanted}")
    print("\nTesting memory vault...")
    vault = memory_vault()
    vault["store"]("spell",   "Fireball")
    vault["store"]("level",   42)
    vault["store"]("element", "Fire")
    print(f"  Recall spell:   {vault['recall']('spell')}")
    print(f"  Recall level:   {vault['recall']('level')}")
    print(f"  Recall element: {vault['recall']('element')}")
    print(f"  Recall unknown: {vault['recall']('unknown')}")
    vault2 = memory_vault()
    print(f"  Independent vault: {vault2['recall']('spell')}")
