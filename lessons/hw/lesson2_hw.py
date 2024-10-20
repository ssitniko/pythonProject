lass SuperHero:
    people='people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def hero_name(self):
        return f'My name is {self.name}'

    def increase_health(self):
        self.health_points **= 2
        return self.health_points

    def __str__(self):
        return f'Nickname: {self.nickname}, Superpower: {self.superpower}, Health points: {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)

# a_hero = SuperHero('aleks', 'cool boy', 'super strong', 10, 'be fair')
# print(a_hero.people)
# print(a_hero.hero_name())
# print(a_hero.increase_health())
# print(a_hero)
# print(len(a_hero))

class AirHero(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly='False'):
        super().__init__(name=name, nickname=nickname, superpower=superpower, health_points=health_points, catchphrase=catchphrase)
        self.damage = damage
        self.fly = fly

    def increase_health(self):
        self.health_points **= 2
        self.fly = True
        return self.health_points, self.fly

    def true_phrase(self):
        return True


class EarthHero(SuperHero):

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly='False'):
        super().__init__(name=name, nickname=nickname, superpower=superpower, health_points=health_points, catchphrase=catchphrase)
        self.damage = damage
        self.fly = fly

    def increase_health(self):
        self.health_points **= 2
        self.fly = True
        return self.health_points, self.fly

    def true_phrase(self):
        return f'True'

air_hero = AirHero('jack', 'fun', 'crazystrong', 6, 'be mercy', 10)

earth_hero = AirHero('billy', 'best', 'strongman', 7, 'life is a game', 5)

print(air_hero.true_phrase())
print(earth_hero.true_phrase())

class Villain(AirHero):
    people = 'opponent'

    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage):
        super().__init__(name, nickname, superpower, health_points, catchphrase, damage)
        self.damage = damage

    def gen_x(self):
        ...
    def crit(self, goal, exponent):
        return goal.damage ** exponent


a_villain = Villain('rocky', 'coldman', 'fast', 10, 'easy', 4)
b_villain = Villain('ricky', 'hotman', 'quick', 6, 'noproblem', 6)

print(a_villain.crit(air_hero, 2))
print(a_villain.crit(earth_hero, 2))