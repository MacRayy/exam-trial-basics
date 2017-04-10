import unittest
from pirates import list_o_pirates

def test_list_o_pirates():
    assertEqual([
        {'Name': 'Ericssen', 'has_wooden_leg': True, 'gold': 19},
        {'Name': 'Tomas', 'has_wooden_leg': False, 'gold': 9},
        {'Name': 'Tim', 'has_wooden_leg': True, 'gold': 6},
        {'Name': 'Roger', 'has_wooden_leg': True, 'gold': 17},
        {'Name': 'Bob', 'has_wooden_leg': False, 'gold': 20},
    ], ['Ericssen', 'Roger'])

if __name__ == '__main__':
    unittest.main()
