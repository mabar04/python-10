from typing import Callable


def spell_combiner(spell1, spell2) -> Callable:
    return lambda *args, **kwargs: (spell1(*args, **kwargs),
                                    spell2(*args, **kwargs))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda *args, **kwargs: (base_spell(*args, **kwargs) * multiplier)


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def caster(*args, **kwargs):
        results = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return results
    return caster


def fireball(target: str) -> str:
    return f"Fireball hits {target}"


def heal(target: str) -> str:
    return f"Heals {target}"


def shield(target: str) -> str:
    return f"Shield protects {target}"


def damage(target: str) -> int:
    return 10


def has_mana(target: str) -> bool:
    return True


def no_mana(target: str) -> bool:
    return False


if __name__ == "__main__":

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result1, result2 = combined("Dragon")
    print(f"Combined spell result: {result1}, {result2}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(damage, 3)
    original = damage("Dragon")
    amplified = mega_fireball("Dragon")
    print(f"Original: {original}\nAmplified: {amplified}")

    print("\nTesting conditional caster...")
    caster1 = conditional_caster(has_mana, fireball)
    caster2 = conditional_caster(no_mana, fireball)
    print(f"With mana:    {caster1('Dragon')}")
    print(f"Without mana: {caster2('Dragon')}")

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal, shield])
    results = sequence("Dragon")
    for r in results:
        print(f"{r}")
