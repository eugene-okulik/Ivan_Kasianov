class Flowers:
    def __init__(
            self,
            name_flower,
            price,
            lifetime,
            freshness,
            color,
            stem_length
    ):
        self.name_flower = name_flower
        self.price = price
        self.lifetime = lifetime
        self.freshness = freshness
        self.color = color
        self.stem_length = stem_length

    def __str__(self):
        return (
                f'{self.name_flower}, '
                f'{self.price}, '
                f'{self.lifetime}, '
                f'{self.freshness}, '
                f'{self.color}, '
                f'{self.stem_length}'
                )

    def __repr__(self):
        return (f''
                f'{self.name_flower}, '
                f'{self.price}, '
                f'{self.lifetime}, '
                f'{self.freshness}, '
                f'{self.color}, '
                f'{self.stem_length}'
                )


class GardenFlowers(Flowers):
    def __init__(self,
                 name_flower,
                 price,
                 lifetime,
                 freshness,
                 color,
                 stem_length
                 ):
        super().__init__(
            name_flower,
            price,
            lifetime,
            freshness,
            color,
            stem_length
        )


class WildFlowers(Flowers):
    def __init__(self,
                 name_flower,
                 price,
                 lifetime,
                 freshness,
                 color,
                 stem_length
                 ):
        super().__init__(
            name_flower,
            price,
            lifetime,
            freshness,
            color,
            stem_length
        )


class ExoticFlowers(Flowers):
    def __init__(self,
                 name_flower,
                 price,
                 lifetime,
                 freshness,
                 color,
                 stem_length
                 ):
        super().__init__(
            name_flower,
            price,
            lifetime,
            freshness,
            color,
            stem_length
        )


class FlowersBouquet():
    def __init__(self, flowers_list):
        self.flowers_list = flowers_list

    def bouquet_cost(self):
        bouquet_cost = []
        for flower in self.flowers_list:
            bouquet_cost.append(flower.price)
        return f"Стоимость букета составляет: {sum(bouquet_cost)} EUR"

    def average_lifetime(self):
        bouquet_lifetime = []
        for arg in self.flowers_list:
            bouquet_lifetime.append(arg.lifetime)
        return (
            f"Букет завянет через: "
            f"{sum(bouquet_lifetime) / len(bouquet_lifetime)} "
            f"часов"
        )

    def sort_bouquet_by_cost(self):
        new_bouquet = []
        result = sorted(self.flowers_list, key=lambda flower: flower.price)
        for flower in result:
            new_bouquet.append(
                f"{flower.name_flower}: "
                f"{flower.price} EUR"
            )
        return (
                f"Букет отсортирован по стоимости "
                f"от самого дешевого цветка к самому дорогому: "
                f"{', '.join(new_bouquet)}"
                )

    def sort_bouquet_by_stem_length(self):
        new_bouquet = []
        result = sorted(
            self.flowers_list,
            key=lambda flower: flower.stem_length
        )
        for flower in result:
            new_bouquet.append(
                f"{flower.name_flower}: "
                f"{flower.stem_length} cm"
            )
        return (
                f"Букет отсортирован по длине стебля "
                f"от самого короткого цветка к самому длинному: "
                f"{", ".join(new_bouquet)}"
                )

    def sort_bouquet_by_color(self):
        new_bouquet = []
        result = sorted(self.flowers_list, key=lambda flower: flower.color)
        for flower in result:
            new_bouquet.append(f"{flower.name_flower}: {flower.color}")
        return f"Букет отсортирован по цвету: {", ".join(new_bouquet)}"

    def sort_bouquet_by_freshness(self):
        new_bouquet = []
        result = sorted(self.flowers_list, key=lambda flower: flower.freshness)
        for flower in result:
            new_bouquet.append(f"{flower.name_flower}: {flower.freshness}")
        return (
                f"Букет отсортирован по свежести цветка: "
                f"{", ".join(new_bouquet)}"
                )

    def find_flower_by_average_lifetime(self):
        longest_lived_flowers = list(
            filter(
                lambda flower: flower.lifetime > 24,
                self.flowers_list)
        )
        new_longest_lived_flower = []
        for flower in longest_lived_flowers:
            new_longest_lived_flower.append(
                f"{flower.name_flower}: "
                f"{flower.lifetime} час."
            )
        return (
                f"Список цветов у которых "
                f"среднее время жизни более 24 часов.: "
                f"{", ".join(new_longest_lived_flower)}"
                )


rose = GardenFlowers("Rose", 30, 72, "fresh", "yellow", 50)
peony = GardenFlowers("Peony", 25, 48, "normal", "red", 45)

chamomile = WildFlowers("Chamomile", 5, 24, "old", "white", 30)
cornflower = WildFlowers("Cornflower", 10, 12, "normal", "blue", 25)

orchid = ExoticFlowers("Orchid", 20, 96, "fresh", "violet", 70)

bouquet = FlowersBouquet([rose, peony, chamomile, cornflower, orchid])
flowers_list = [rose, peony, chamomile, cornflower, orchid]


print(bouquet.bouquet_cost())
print(bouquet.average_lifetime())
print(bouquet.sort_bouquet_by_cost())
print(bouquet.sort_bouquet_by_stem_length())
print(bouquet.sort_bouquet_by_color())
print(bouquet.sort_bouquet_by_freshness())
print(bouquet.find_flower_by_average_lifetime())
