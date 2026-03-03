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
        return (
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
        return '; '.join(
            map(
                str,
                sorted(
                    self.flowers_list,
                    key=lambda flower: flower.price
                )
            )
        )

    def sort_bouquet_by_stem_length(self):
        return '; '.join(
            map(
                str,
                sorted(
                    self.flowers_list,
                    key=lambda flower: flower.stem_length
                )
            )
        )

    def sort_bouquet_by_color(self):
        return '; '.join(
            map(
                str,
                sorted(
                    self.flowers_list,
                    key=lambda flower: flower.color
                )
            )
        )

    def sort_bouquet_by_freshness(self):
        return '; '.join(
            map(
                str,
                sorted(
                    self.flowers_list,
                    key=lambda flower: flower.freshness
                )
            )
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
        return ', '.join(new_longest_lived_flower)


rose = GardenFlowers("Rose", 30, 72, "fresh", "yellow", 50)
peony = GardenFlowers("Peony", 25, 48, "normal", "red", 45)

chamomile = WildFlowers("Chamomile", 5, 24, "old", "white", 30)
cornflower = WildFlowers("Cornflower", 10, 12, "normal", "blue", 25)

orchid = ExoticFlowers("Orchid", 20, 96, "fresh", "violet", 70)

bouquet = FlowersBouquet([rose, peony, chamomile, cornflower, orchid])
flowers_list = [rose, peony, chamomile, cornflower, orchid]


print(bouquet.bouquet_cost())
print(bouquet.average_lifetime())
print(
    f"Цветы в букете отсортированы по стоимости: "
    f"{bouquet.sort_bouquet_by_cost()}"
)
print(
    f"Цветы в букете отсортированы по длине стебля: "
    f"{bouquet.sort_bouquet_by_stem_length()}"
)
print(
    f"Цветы в букете отсортированы по цвету: "
    f"{bouquet.sort_bouquet_by_color()}"
)
print(
    f"Цветы в букете отсортированы по свежести: "
    f"{bouquet.sort_bouquet_by_freshness()}"
)
print(
    f"Цветы у которых среднее время жизни более 24 часов: "
    f"{bouquet.find_flower_by_average_lifetime()}"
)
