from functools import wraps
import time


def spell_timer(func: callable) -> callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Spell completed in {end - start:.4f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if args[1] >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(f"Spell failed, retrying... (attempt {i + 1}"
                          f"/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) >= 3:
            return name.replace(" ", "").isalpha()
        return False

    @power_validator(10)
    def cast_spell(self, power: int, spell_name: str) -> str:
        return f"Successfully cast {spell_name} with {power} power"


class Mock:
    pass


if __name__ == "__main__":

    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    result = fireball()
    print(f"Result: {result}")

    print("\nTesting power validator...")

    @power_validator(50)
    def cast(self_mock, power, spell):
        return f"Cast {spell} with {power} power!"

    m = Mock()
    print(cast(m, 100, "Fireball"))
    print(cast(m, 10,  "Fireball"))

    print("\nTesting retry spell...")
    import random
    random.seed(42)

    @retry_spell(3)
    def unstable_spell():
        if random.random() < 0.7:
            raise Exception("Fizzled!")
        return "Spell succeeded!"

    print(unstable_spell())

    print("\nTesting MageGuild...")
    guild = MageGuild()
    print(MageGuild.validate_mage_name("Zara"))
    print(MageGuild.validate_mage_name("Za"))
    print(MageGuild.validate_mage_name("Zara123"))
    print(MageGuild.validate_mage_name("Dark Mage"))
    print(guild.cast_spell(15, "Lightning"))
    print(guild.cast_spell(5,  "Lightning"))
