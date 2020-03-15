RENAMED_COLUMNS = {
    'Province/State': 'province_state',
    'Country/Region': 'country',
    'Lat': 'lat',
    'Long': 'long',
}

# https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population#Summary_of_population_by_region
US_POPULATION = {
        'Massachusetts':        {'population': 6892503,  'sub_region': 'new_england',        'region': 'northeast'},
        'Connecticut':          {'population': 3565287,  'sub_region': 'new_england',        'region': 'northeast'},
        'New Hampshire':        {'population': 1359711,  'sub_region': 'new_england',        'region': 'northeast'},
        'Maine':                {'population': 1344212,  'sub_region': 'new_england',        'region': 'northeast'},
        'Rhode Island':         {'population': 1059361,  'sub_region': 'new_england',        'region': 'northeast'},
        'Vermont':              {'population': 623989,   'sub_region': 'new_england',        'region': 'northeast'},
        'New York':             {'population': 19453561, 'sub_region': 'mid_atlantic',       'region': 'northeast'},
        'Pennsylvania':         {'population': 12801989, 'sub_region': 'mid_atlantic',       'region': 'northeast'},
        'New Jersey':           {'population': 8882190,  'sub_region': 'mid_atlantic',       'region': 'northeast'},
        'Florida':              {'population': 21477737, 'sub_region': 'south_atlantic',     'region': 'south'},
        'Georgia':              {'population': 10617423, 'sub_region': 'south_atlantic',     'region': 'south'},
        'North Carolina':       {'population': 10488084, 'sub_region': 'south_atlantic',     'region': 'south'},
        'Virginia':             {'population': 8535519,  'sub_region': 'south_atlantic',     'region': 'south'},
        'Maryland':             {'population': 6045680,  'sub_region': 'south_atlantic',     'region': 'south'},
        'South Carolina':       {'population': 5148714,  'sub_region': 'south_atlantic',     'region': 'south'},
        'West Virginia':        {'population': 1792147,  'sub_region': 'south_atlantic',     'region': 'south'},
        'Delaware':             {'population': 973764,   'sub_region': 'south_atlantic',     'region': 'south'},
        'District of Columbia': {'population': 705749,   'sub_region': 'south_atlantic',     'region': 'south'},
        'Tenessee':             {'population': 6346105,  'sub_region': 'east_south_central', 'region': 'south'},
        'Alabama':              {'population': 4903185,  'sub_region': 'east_south_central', 'region': 'south'},
        'Kentucky':             {'population': 4467673,  'sub_region': 'east_south_central', 'region': 'south'},
        'Mississippi':          {'population': 2976149,  'sub_region': 'east_south_central', 'region': 'south'},
        'Texas':                {'population': 28995881, 'sub_region': 'west_south_central', 'region': 'south'},
        'Louisiana':            {'population': 4648794,  'sub_region': 'west_south_central', 'region': 'south'},
        'Oklahoma':             {'population': 3956971,  'sub_region': 'west_south_central', 'region': 'south'},
        'Arkansas':             {'population': 3017804,  'sub_region': 'west_south_central', 'region': 'south'},
        'Illinois':             {'population': 12671821, 'sub_region': 'east_north_central', 'region': 'midwest'},
        'Ohio':                 {'population': 11689100, 'sub_region': 'east_north_central', 'region': 'midwest'},
        'Michigan':             {'population': 9986857,  'sub_region': 'east_north_central', 'region': 'midwest'},
        'Indiana':              {'population': 6732219,  'sub_region': 'east_north_central', 'region': 'midwest'},
        'Wisconsin':            {'population': 5822434,  'sub_region': 'east_north_central', 'region': 'midwest'},
        'Missouri':             {'population': 6137428,  'sub_region': 'west_north_central', 'region': 'midwest'},
        'Minnesota':            {'population': 5639632,  'sub_region': 'west_north_central', 'region': 'midwest'},
        'Iowa':                 {'population': 3155070,  'sub_region': 'west_north_central', 'region': 'midwest'},
        'Kansas':               {'population': 2913314,  'sub_region': 'west_north_central', 'region': 'midwest'},
        'Nebraska':             {'population': 1934408,  'sub_region': 'west_north_central', 'region': 'midwest'},
        'South Dakota':         {'population': 884659,   'sub_region': 'west_north_central', 'region': 'midwest'},
        'North Dakota':         {'population': 762062,   'sub_region': 'west_north_central', 'region': 'midwest'},
        'Arizona':              {'population': 7278717,  'sub_region': 'mountain',           'region': 'west'},
        'Colorado':             {'population': 5758736,  'sub_region': 'mountain',           'region': 'west'},
        'Utah':                 {'population': 3205958,  'sub_region': 'mountain',           'region': 'west'},
        'Nevada':               {'population': 3080156,  'sub_region': 'mountain',           'region': 'west'},
        'New Mexico':           {'population': 2096829,  'sub_region': 'mountain',           'region': 'west'},
        'Idaho':                {'population': 1787065,  'sub_region': 'mountain',           'region': 'west'},
        'Montana':              {'population': 1068778,  'sub_region': 'mountain',           'region': 'west'},
        'Wyoming':              {'population': 578759,   'sub_region': 'mountain',           'region': 'west'},
        'California':           {'population': 39512223, 'sub_region': 'pacific',            'region': 'west'},
        'Washington':           {'population': 7614893,  'sub_region': 'pacific',            'region': 'west'},
        'Oregon':               {'population': 4217737,  'sub_region': 'pacific',            'region': 'west'},
        'Hawaii':               {'population': 1415872,  'sub_region': 'pacific',            'region': 'west'},
        'Alaska':               {'population': 731545,   'sub_region': 'pacific',            'region': 'west'}
}

# https://www.census.gov/data/datasets/time-series/demo/popest/2010s-counties-total.html
US_COUNTIES = {
}

CRUISE_SHIPS = [
    'Diamond Princess',
    'Grand Princess',
]
