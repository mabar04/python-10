def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda item: item["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda spell: "*" + spell + "*", spells))


def mage_stats(mages: list[dict]) -> dict:
    return {
        'max_power': max(mages, key=lambda m: m["power"])["power"],
        'min_power': min(mages, key=lambda m: m["power"])["power"],
        'avg_power': round(sum(m["power"] for m in mages) / len(mages), 2)
    }


if __name__ == "__main__":
    print("Testing artifact sorter...")
    artifacts = [
        {"name": "Crystal Orb", "power": 85, "type": "orb"},
        {"name": "Fire Staff",   "power": 92, "type": "staff"},
        {"name": "Shadow Blade", "power": 78, "type": "blade"},
    ]
    for a in artifact_sorter(artifacts):
        print(f"  {a['name']} ({a['power']} power)")

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    for s in spell_transformer(spells):
        print(f"  {s}")

    print("\nTesting power filter (min 80)...")
    mages = [
        {"name": "Zara",  "power": 95, "element": "fire"},
        {"name": "Leo",   "power": 72, "element": "water"},
        {"name": "Mira",  "power": 88, "element": "wind"},
    ]
    for m in power_filter(mages, 80):
        print(f"  {m['name']} ({m['power']} power)")

    print("\nTesting mage stats...")
    print(mage_stats(mages))
