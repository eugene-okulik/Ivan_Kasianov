class Flowers:
    def __init__(self, price, lifetime, freshness, color, stem_length):
        self.price = price
        self.lifetime = lifetime
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length


class GardenFlowers(Flowers):
    def __init__(self, price, lifetime, freshness, color, stem_length):
        super().__init__(price, lifetime, freshness, color, stem_length)


class WildFlowers(Flowers):
    def __init__(self, price, lifetime, freshness, color, stem_length):
        super().__init__(price, lifetime, freshness, color, stem_length)


class ExoticFlowers(Flowers):
    def __init__(self, price, lifetime, freshness, color, stem_length):
        super().__init__(price, lifetime, freshness, color, stem_length)


class FlowersBouquet():

    def bouquet(self, *args):
        bouquet = []
        for arg in args:
            bouquet.append(arg)
        return bouquet

    def compile_bouquet(self, *args):
        bouquet_cost = []
        for arg in args:
            bouquet_cost.append(arg.price)
        return f"Стоимость букета составляет: {sum(bouquet_cost)} EUR"

    def average_lifetime(self, *args):
        bouquet_lifetime = []
        for arg in args:
            bouquet_lifetime.append(arg.lifetime)
        return (
            f"Букет завянет через: "
            f"{sum(bouquet_lifetime) / len(bouquet_lifetime)} "
            f"часов"
        )


rose = GardenFlowers(30, 72, "fresh", "yellow", 50)
peony = GardenFlowers(25, 48, "normal", "red", 45)

chamomile = WildFlowers(5, 24, "old", "white", 30)
cornflower = WildFlowers(10, 12, "normal", "blue", 25)

orchid = ExoticFlowers(20, 96, "fresh", "violet", 70)

first_bouquet = FlowersBouquet()

print(first_bouquet.compile_bouquet(rose, chamomile, orchid))
print(first_bouquet.average_lifetime(rose, chamomile, orchid))
