#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

moscow = sites['Moscow']
london = sites['London']
paris = sites ['Paris']

msk_lnd = ((moscow[0] - london[0]) ** 2) + ((london[1] - moscow[1]) ** 2) ** 0.5
msk_prs = ((moscow[0] - paris[0]) ** 2) + ((london[1] - paris[1]) ** 2) ** 0.5
prs_lnd = ((paris[0] - london[0]) ** 2) + ((paris[1] - moscow[1]) ** 2) ** 0.5

distances = {}

distances['Moscow'] = {}
distances['Moscow']['London'] = msk_lnd
distances['Moscow']['Paris'] = msk_prs

distances['London'] = {}
distances['London']['Moscow'] = msk_lnd
distances['London']['Paris'] = prs_lnd

distances['Paris'] = {}
distances['Paris']['Moscow'] = msk_prs
distances['Paris']['London'] = prs_lnd

print(distances)




