Beasts
======

A game of beast survival Game


    python -m beasts.cli

Run a quick game

    +---------+------+-----+-----+-------+-----+-----+-----+---------+-------+--------+
    |   name  | life | age | gen | speed | str | int | exp | lustful | angry | hungry |
    +---------+------+-----+-----+-------+-----+-----+-----+---------+-------+--------+
    | Beast 1 |  10  |  0  |  0  |   50  |  50 |  50 |  50 |    50   |   50  |   50   |
    | Beast 2 |  10  |  0  |  0  |   50  |  50 |  50 |  50 |    50   |   50  |   50   |
    | Beast 3 |  10  |  0  |  0  |   50  |  50 |  50 |  50 |    50   |   50  |   50   |
    +---------+------+-----+-----+-------+-----+-----+-----+---------+-------+--------+

Run for 20 turns


    Beast 3 is hungry
    Beast 4 is angry
    Beast 4 fights Beast 8
    Beast 4 scores 82125000.0 vs Beast 8 scores 51750000.0
    Beast 4 wins
    Beast 5 is lustful
    Beast 6 is hungry
    Beast 7 is hungry
    Beast 8 is hungry
    Beast 9 is hungry
    Beast 10 is hungry
    Beast 11 is lustful
    Beast 12 is hungry
    Beast 13 is hungry
    Beast 14 is hungry
    Beast 15 is hungry
    Beast 16 is angry
    Beast 16 fights Beast 11
    Beast 16 scores 20625000.0 vs Beast 11 scores 61000000.0

Until ...

    +---------+------+-----+-----+-------+------+------+-----+---------+-------+--------+
    |   name  | life | age | gen | speed | str  | int  | exp | lustful | angry | hungry |
    +---------+------+-----+-----+-------+------+------+-----+---------+-------+--------+
    | Beast 1 |  5   |  11 |  0  |   50  |  50  |  50  |  63 |    49   |   35  |   49   |
    | Beast 2 |  8   |  11 |  0  |   50  |  50  |  50  |  54 |    49   |   47  |   49   |
    | Beast 3 |  9   |  11 |  0  |   50  |  50  |  50  |  55 |    41   |   49  |   52   |
    | Beast 4 |  9   |  7  |  1  |  50.0 | 50.0 | 50.0 |  53 |    41   |   51  |   51   |
    | Beast 5 |  8   |  6  |  2  |  50.0 | 50.0 | 50.0 |  54 |    48   |   46  |   50   |
    | Beast 6 |  10  |  5  |  1  |  50.0 | 50.0 | 50.0 |  54 |    47   |   49  |   49   |
    | Beast 7 |  10  |  4  |  3  |  50.0 | 50.0 | 50.0 |  54 |    54   |   48  |   45   |
    | Beast 8 |  8   |  2  |  3  |  50.0 | 50.0 | 50.0 |  52 |    48   |   46  |   52   |
    +---------+------+-----+-----+-------+------+------+-----+---------+-------+--------+

Run for 50 more turns

    Beast 3 is angry
    Beast 3 fights Beast 5
    Beast 3 scores 86000000 vs Beast 5 scores 8500000.0
    Beast 3 wins
    Beast 4 is hungry
    Beast 5 is angry
    Beast 5 fights Beast 3
    Beast 5 scores 77625000.0 vs Beast 3 scores 11000000
    Beast 5 wins
    Beast 9 is hungry
    Beast 10 is lustful
    Beast 11 is hungry
    Beast 12 is angry
    Beast 12 fights Beast 16
    Beast 12 scores 70875000.0 vs Beast 16 scores 67500000.0
    Beast 12 wins
    Beast 13 is lustful
    Beast 14 is angry
    Beast 14 fights Beast 21
    Beast 14 scores 15000000.0 vs Beast 21 scores 42750000.0
    Beast 21 wins
    Beast 15 is lustful
    Beast 16 is hungry
    Beast 17 is hungry
    Beast 18 is angry
    Beast 18 fights Beast 23
    Beast 18 scores 7000000.0 vs Beast 23 scores 46375000.0

Until ...

    +----------+------+-----+-----+-------+------+------+-----+---------+-------+--------+
    |   name   | life | age | gen | speed | str  | int  | exp | lustful | angry | hungry |
    +----------+------+-----+-----+-------+------+------+-----+---------+-------+--------+
    | Beast 3  |  0   |  51 |  0  |   50  |  50  |  50  |  89 |    17   |   33  |   47   |
    | Beast 5  |  3   |  28 |  1  |  50.0 | 50.0 | 50.0 |  71 |    38   |   30  |   59   |
    | Beast 9  |  2   |  22 |  2  |  50.0 | 50.0 | 50.0 |  75 |    56   |   28  |   47   |
    | Beast 10 |  5   |  19 |  3  |  50.0 | 50.0 | 50.0 |  59 |    33   |   49  |   53   |
    | Beast 11 |  2   |  17 |  1  |  50.0 | 50.0 | 50.0 |  67 |    47   |   35  |   49   |
    | Beast 12 |  2   |  17 |  3  |  50.0 | 50.0 | 50.0 |  66 |    43   |   33  |   54   |
    | Beast 13 |  5   |  16 |  4  |  50.0 | 50.0 | 50.0 |  68 |    38   |   38  |   49   |
    | Beast 15 |  4   |  14 |  3  |  50.0 | 50.0 | 50.0 |  64 |    40   |   38  |   54   |
    | Beast 16 |  1   |  14 |  4  |  50.0 | 50.0 | 50.0 |  61 |    40   |   38  |   54   |
    | Beast 17 |  5   |  14 |  5  |  50.0 | 50.0 | 50.0 |  60 |    32   |   46  |   58   |
    | Beast 18 |  3   |  12 |  4  |  50.0 | 50.0 | 50.0 |  57 |    34   |   46  |   55   |
    | Beast 19 |  3   |  10 |  4  |  50.0 | 50.0 | 50.0 |  57 |    44   |   40  |   56   |
    | Beast 20 |  4   |  10 |  6  |  50.0 | 50.0 | 50.0 |  60 |    52   |   36  |   53   |
    | Beast 21 |  7   |  10 |  5  |  50.0 | 50.0 | 50.0 |  59 |    40   |   44  |   56   |
    | Beast 22 |  4   |  9  |  4  |  50.0 | 50.0 | 50.0 |  57 |    47   |   37  |   57   |
    | Beast 23 |  7   |  9  |  5  |  50.0 | 50.0 | 50.0 |  55 |    39   |   51  |   52   |
    | Beast 24 |  5   |  8  |  1  |  50.0 | 50.0 | 50.0 |  53 |    46   |   52  |   50   |
    | Beast 25 |  7   |  8  |  3  |  50.0 | 50.0 | 50.0 |  54 |    42   |   52  |   52   |
    | Beast 26 |  4   |  7  |  7  |  50.0 | 50.0 | 50.0 |  53 |    49   |   47  |   51   |
    | Beast 27 |  8   |  6  |  6  |  50.0 | 50.0 | 50.0 |  59 |    52   |   38  |   54   |
    | Beast 28 |  5   |  5  |  6  |  50.0 | 50.0 | 50.0 |  52 |    55   |   47  |   49   |
    | Beast 29 |  6   |  4  |  2  |  50.0 | 50.0 | 50.0 |  52 |    50   |   48  |   50   |
    | Beast 30 |  10  |  4  |  8  |  50.0 | 50.0 | 50.0 |  54 |    42   |   48  |   54   |
    | Beast 31 |  7   |  3  |  6  |  50.0 | 50.0 | 50.0 |  51 |    53   |   49  |   49   |
    | Beast 32 |  9   |  3  |  5  |  50.0 | 50.0 | 50.0 |  53 |    45   |   47  |   53   |
    | Beast 33 |  8   |  3  |  6  |  50.0 | 50.0 | 50.0 |  54 |    49   |   43  |   53   |
    | Beast 34 |  8   |  2  |  6  |  50.0 | 50.0 | 50.0 |  52 |    48   |   46  |   52   |
    | Beast 35 |  10  |  1  |  4  |  50.0 | 50.0 | 50.0 |  52 |    51   |   47  |   51   |
    | Beast 36 |  9   |  1  |  5  |  50.0 | 50.0 | 50.0 |  50 |    51   |   51  |   49   |
    +----------+------+-----+-----+-------+------+------+-----+---------+-------+--------+

Final Result
------------

    World stats
    Max number of beasts 69
    Most Experienced Beast: Beast 157 (
        life:3, age:18, gen:17, spe:50.0, str:50.0,
        int:50.0, exp:72, lust:36, anger:34, hunger:58
    )
    Oldest Beast: Beast 150 (
        life:0, age:20, gen:17, spe:50.0, str:50.0,
        int:50.0, exp:63, lust:34, anger:46, hunger:56
    )
