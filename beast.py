
import random
import prettytable
from random import choice
from operator import attrgetter
import glob
import pickle
import sys
__author__ = 'mm'

MAX_BEASTS = 1000
BREEDING_AGE = 5

WORLD_COUNTER = 1
WORLD_REPR = u'%s (%s beasts, %s food, round %s, steroids:%s, hormones:%s)'
BEAST_COUNTER = 1
BEAST_REPR = u'%s (life:%s, age:%s, gen:%s, spe:%s, str:%s, int:%s, exp:%s, ' \
             u'lust:%s, anger:%s, hunger:%s)'

DRIVE_ANGER = 'angry'
DRIVE_HUNGER = 'hungry'
DRIVE_LUST = 'lustful'

DECISION_PRINT = 'p'
DECISION_FOOD = 'f'
DECISION_SAVE = 's'
DECISION_HORMONES = 'h'
DECISION_STEROIDS = 'x'
DECISION_SKIP = 'n'
DECISION_END = 'e'
DECISION_QUIT = 'q'
DECISION_CONTINUE = 'c'
DECISION_STATS = 'S'

DECISIONS = (
    (DECISION_PRINT, 'Print Status'),
    (DECISION_STATS, 'Print Stats'),
    (DECISION_FOOD, 'Add Food'),
    (DECISION_SAVE, 'Save Game'),
    (DECISION_HORMONES, 'Add Hormones - (increases lust)'),
    (DECISION_STEROIDS, 'Add Hormones - (increases anger)'),
    (DECISION_SKIP, 'Skip Turns'),
    (DECISION_END, 'Run to End'),
    (DECISION_QUIT, 'Quit'),
    (DECISION_CONTINUE, 'Continue'),
)

WORLD_DECISION_LOAD = 'l'
WORLD_DECISION_NEW = 'n'

WORLD_DECISIONS = (
    (WORLD_DECISION_LOAD, 'Load Game'),
    (WORLD_DECISION_NEW, 'New Game')
)


def get_valid_int(message='Input Number'):
    user_int = raw_input(message)
    while True:
        try:
            return int(user_int)
        except ValueError:
            print 'Invalid Choice', user_int
            user_int = raw_input(message)


def get_valid_input(choices):
    _user_choice = raw_input('Choice: ')
    choices = (c[0] for c in choices)
    while _user_choice not in choices:
        print 'Invalid Choice ', _user_choice
        _user_choice = raw_input('Choice: ')
    return _user_choice


def print_choices(choices):
    for user_choice in choices:
        print user_choice[0], ': ', user_choice[1]


class World(object):

    food = 100
    round = 1

    def __init__(self, beasts=list()):
        global WORLD_COUNTER
        self.beasts = beasts
        self.hormones = 0
        self.steroids = 0
        self.skip = 0
        self.name = u'World %s' % WORLD_COUNTER
        WORLD_COUNTER += 1

        # Stats
        self.highest_exp = None
        self.oldest = None
        self.max_beasts = len(self.beasts)
        self.history = []

    def __str__(self):
        return WORLD_REPR % (self.name, len(self.beasts), self.food,
                             self.round, self.steroids, self.hormones)

    def print_world(self):
        print self
        pt = prettytable.PrettyTable(['name', 'life', 'age', 'gen', 'speed',
                                      'str', 'int', 'exp', DRIVE_LUST,
                                      DRIVE_ANGER, DRIVE_HUNGER])

        for beast in self.beasts:
            pt.add_row([beast.name, beast.life, beast.age, beast.generation,
                        beast.speed, beast.strength, beast.intelligence,
                        beast.experience, beast.lust, beast.anger,
                        beast.hunger])
        print pt

    def print_stats(self):
        print self.name, 'stats'
        print 'Max number of beasts', self.max_beasts
        print 'Most Experienced Beast:', self.highest_exp
        print 'Oldest Beast:', self.oldest
        for _round, num_beasts in self.history:
            print 'Round', _round, num_beasts*'|', num_beasts
        if not self.history:
            print 'No Graph'

    def add_beast(self, beast):
        self.beasts.append(beast)

    def run_for(self, i):
        for _ in range(0, i):
            self.run_once()
            self.print_world()
            if len(self.beasts) < 1:
                print 'World ends after %s rounds.' % self.round
                break

    def run_once(self):
        if not self.skip:
            print_choices(DECISIONS)
            user_choice = get_valid_input(DECISIONS)
            if user_choice == DECISION_FOOD:
                message = 'Amount of food to add, currently %s: ' % self.food
                self.food += get_valid_int(message)
            elif user_choice == DECISION_SKIP:
                message = 'Number of turns to skip: '
                self.skip += get_valid_int(message)
            elif user_choice == DECISION_SAVE:
                file_prefix = raw_input('Filename to save '
                                        '( .beasts will be appended ) : ')
                file_name = '%s.%s' % (file_prefix, 'beasts')
                pickle.dump(self, open(file_name, 'w'))
                return
            elif user_choice == DECISION_HORMONES:
                message = 'Set hormones, currently %s: ' % self.hormones
                self.hormones = get_valid_int(message)
            elif user_choice == DECISION_STEROIDS:
                message = 'Set steroids, currently %s: ' % self.steroids
                self.steroids = get_valid_int(message)
            elif user_choice == DECISION_END:
                self.skip = -1
            elif user_choice == DECISION_QUIT:
                sys.exit()
            elif user_choice == DECISION_PRINT:
                print self
                return
            elif user_choice == DECISION_CONTINUE:
                pass
            elif user_choice == DECISION_STATS:
                self.print_stats()
                return
            else:
                print '### Invalid Choice ###'
                return
        else:
            self.skip -= 1

        self.__run__()

    def __run__(self):
        dead = []
        for beast in self.beasts:
            beast.age += 1
            drive = beast.get_drive(world)
            print beast.name, 'is', drive
            if drive == DRIVE_ANGER:

                # Fighting
                other = choice(self.beasts)
                beast.fight(other)

            elif drive == DRIVE_LUST:

                # Breeding
                other = choice(self.beasts)
                child = beast.breed(other)
                if child:
                    if len(self.beasts) < MAX_BEASTS:
                        if beast.age < BREEDING_AGE:
                            print 'Too young to bread %s<%s' % (beast.age,
                                                                BREEDING_AGE)
                        self.beasts.append(child)
                    else:
                        print 'Too Many Beasts ', MAX_BEASTS

            elif drive == DRIVE_HUNGER:

                # Eat
                if self.food > 0:
                    self.food -= 1
                    beast.eat()
                else:
                    beast.starve()

            # Did the beast die?
            if beast.life < 1:
                dead.append(beast)

            # Gather Stats
            self.highest_exp = max(self.beasts, key=attrgetter('experience'))
            self.oldest = max(self.beasts, key=attrgetter('age'))
            self.max_beasts = max(self.max_beasts, len(self.beasts))

        for dead_beast in dead:
            print 'DEAD beast', dead_beast
            self.beasts.remove(dead_beast)

        self.history.append((self.round, len(self.beasts)))
        self.round += 1


class Beast(object):

    # Stats
    life = 10
    speed = 50
    strength = 50
    intelligence = 50
    experience = 50
    age = 0
    generation = 0

    # Drives
    lust = 50
    hunger = 50
    anger = 50

    def __init__(self, generation=0):
        global BEAST_COUNTER
        self.name = u'Beast %s' % BEAST_COUNTER
        self.generation = generation
        BEAST_COUNTER += 1

    def __str__(self):
        return BEAST_REPR % (self.name, self.life, self.age, self.generation,
                             self.speed, self.strength, self.intelligence,
                             self.experience, self.lust, self.anger,
                             self.hunger)

    def eat(self, amount=1):
        self.hunger -= amount

    def starve(self):
        self.life -= 1

    def get_drive(self, current_world):

        x1 = self.lust + current_world.hormones
        x2 = x1 + self.hunger
        x3 = x2 + self.anger + current_world.steroids

        r1 = range(0, x1)
        r2 = range(x1, x2)
        r3 = range(x2, x3)

        rand = random.randint(0, x3-1)
        if rand in r1:
            self.lust -= 1
            self.anger += 1
            self.hunger += 1
            return DRIVE_LUST
        elif rand in r2:
            self.lust += 1
            self.anger += 1
            self.hunger -= 1
            return DRIVE_HUNGER
        elif rand in r3:
            self.lust += 1
            self.anger -= 1
            self.hunger += 1
            return DRIVE_ANGER
        else:
            raise Exception('Unknown Drive %s: %s->%s %s->%s %s->%s' % (
                rand, 0, x1, x1, x2, x2, x3))

    def base_score(self):
        return self.strength * self.speed * self.intelligence * self.experience

    def create_child(self, other):
        gen = max(self.generation, other.generation)
        child = Beast(generation=gen+1)
        child.speed = (self.speed + other.speed) / 2
        child.strength = (self.strength + other.strength) / 2
        child.intelligence = (self.intelligence + other.intelligence) / 2
        return child

    def breed(self, other):
        breed_score = random.randint(1, 10)
        self.lust -= 2

        if breed_score > 8:
            return self.create_child(other)
        else:
            return None

    def fight(self, other):

        if self == other:
            # Not fighting self
            return

        self_score = random.randint(1, 10) * self.base_score()
        other_score = random.randint(1, 10) * other.base_score()
        self.anger -= 2
        other.anger -= 2

        print self.name, 'fights', other.name
        print self.name, 'scores', self_score, 'vs', other.name, 'scores', \
            other_score

        if self_score > other_score:
            self.experience += 2
            other.experience += 1
            other.life -= 1
            print self.name, 'wins'
        elif other_score > self_score:
            other.experience += 2
            self.experience += 1
            self.life -= 1
            print other.name, 'wins'
        else:
            self.experience += 1
            other.experience += 1
            print self.name, 'and', other.name, 'draws'


if __name__ == '__main__':
    print_choices(WORLD_DECISIONS)
    user_choice = get_valid_input(WORLD_DECISIONS)
    if user_choice == WORLD_DECISION_NEW:
        world = World(beasts=[Beast(), Beast(), Beast()])
        world.run_for(100)
        world.print_world()
        world.print_stats()
    elif user_choice == WORLD_DECISION_LOAD:
        files = glob.glob('*.beasts')
        if len(files) == 0:
            print 'No valid .beasts files'
            sys.exit(1)
        counter = 1
        for f in files:
            print 'Press \'%s\' to Load %s' % (counter, f)
            counter += 1
        file_index = get_valid_int()
        if file_index < len(files):
            world = pickle.load(open(files[file_index], 'r'))
            world.run_for(100)
            world.print_world()
            world.print_stats()
        else:
            raise Exception('Not a valid choice \'%s\'' % user_choice)
