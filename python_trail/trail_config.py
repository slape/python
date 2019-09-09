# Define Trail Options (14 total options)
trails = [
    ['Fort ahead!', 'You have arrived at a Fort. Collect 1 supply.', 'supplies', 'none', False],
    ['Town ahead!', 'You have arrived at a Town. Remove 1 Calamity.', 'calamity', 'none', False],
    ['Calm road to the left.', 'As you were.', 'pass', 'none', False],
    ['Calm road to the right.', 'No trouble here, partner.', 'pass', 'None', False],
    ['Calm road straight ahead.', 'Remain calm. Carry on.', 'pass', 'None', False],
    ['Treacherous road to the right.', 'Receive one calamity.', 'None', 'None', True],
    ['Treacherous road to the left.', 'Receive one calamity.', 'None', 'None', True],
    ['Treacherous road straight ahead.', 'Receive one calamity.', 'None', 'None', True],
    ['Winding road straight ahead.', 'Receive one calamity.', 'None', 'None', True],
    ['Road crosses a river to the left.', 'Roll and Even Number to Ford the River. \n Roll a 1 and die by drowning. \n Roll a 3 or 5 and play passes to the next player.', 'None', 'even', False],
    ['Road crosses a river to the right.', 'Roll and Even Number to Ford the River. \n Roll an ODD number and lose a supply.', 'None', 'odd', False],
    ['Winding road crosses a river straight ahead.', 'Roll and Even Number to Ford the River. \n Roll a 1 and die by drowning. \n Roll a 3 or 5 and play passes to the next player.', 'None', 'even', False],
    ['Treacherous road crosses a river straight ahead.', 'Roll and Even Number to Ford the River. \n Roll a 1 and die by drowning. \n Roll a 3 or 5 and play passes to the next player.', 'None', 'even', False],
    ['Treacherous road crosses a river to the left.', 'Roll and Even Number to Ford the River. \n Roll an ODD number and lose a supply.', 'None', 'odd', False],
    ['Treacherous road crosses a river to the right.', 'Roll and Even Number to Ford the River. \n Roll an ODD number and lose a supply.', 'None', 'odd', False],
    ]

# Define Supply Options (10 total options)
supplies = [
    ['Half a Pizza', 'Peyote'],
    ['Bullets for your 9', 'Snake'],
    ['Vicodin', 'Measles'],
    ['A keg of Beer', 'Cold'],
    ['A summer dress', 'Terminator'],
    ['Spare Parts', 'Tire'],
    ['Two Oxen', 'Oxen'],
    ['A Dream Catcher', 'Treason'],
    ['A Mace', 'Dino'],
    ['A partially eaten birthday cake', 'Starving'],
    ['Soylent', 'donQ'],
    ['A Knight', 'Steam'],
    ['A Starship', 'Bomb']
]

# Define Calamities (15 total options)
Calamities = [
    ['Kenny', 'Kenny killed you.'],
    ['Dino', 'Dino ate all your pizza and beer. \nYou will need a Mace to kill him and eat him or you die.'],
    ['Starving', 'You are starving to death. \nYou will need a partially eaten birthday cake to survive.'],
    ['Soylent', 'Rejoice! You have found some extra Soylent.'],
    ['Snake', 'You were bitten by a Fractal Snake. \nYou will need bullets for your 9 to kill it before it kills you.'],
    ['Treason', 'You are being accused of Treason. \nYou will need to ward off this bad luck with a dream catcher or you die.'],
    ['Cold', 'Beat the cold by drinking as much beer as you can. \nYou need a keg of beer or you will die.'],
    ['Oxen', 'Your Oxen were misbehaving, so another member killed them. \nYou will need Two Oxen or everyone dies.'],
    ['Measles', 'You have the Measles. \nLose a turn unless you have some Vicodin to keep going.'],
    ['Dysentery', 'You died of Dysentery.'],
    ['Tire', 'Your steam mobile has a flat tire. \nYou will need some spare parts to fix it or everyone dies.'],
    ['Steam', 'Your steam mobile ran out of steam. \nYou will need a knight to pull it or everyone dies.'],
    ['Terminator', 'Terminator showed up from the future to kill you. \nYou need to disguise yourself with a new dress or he kills you.'],
    ['God', 'God killed you.'],
    ['Donq', 'Don Qixote has crossed your path. \nHe is demanding some Soylent or he kills you.'],
    ['Peyote', 'You ate some random Peyote that you found along the way. \nYou will need half a pizza to get over this or you die.'],
    ['Enterprise', 'Captian Picard has appeard in front of you as if by magic. \nHe seemed confused and shot you with his laser. You died.'],
    ['Bomb', 'In the distance you see a mushroom cloud. \nYou will need to beam aboard a starship to avoid dying by the fall out.'],
    ['Tornado', 'A tornado ripped through your camp while you were hunting. Loose half your supplies.']
]

# Define paths to ascii picture files
ascii = {
    'trail' : 'ascii_pics/trail_pic',
    '9mm' : 'ascii_pics/9mm',
    'beer' : 'ascii_pics/beer',
    'cactus' : 'ascii_pics/cactus',
    'cake' : 'ascii_pics/cake',
    'measles' : 'ascii_pics/cholera',
    'dress' : 'ascii_pics/clothes',
    'dead_oxen' : 'ascii_pics/dead_oxen',
    'death' : 'ascii_pics/death',
    'dice' : 'ascii_pics/dice',
    'dino' : 'ascii_pics/dino',
    'disentary' : 'ascii_pics/disentary',
    'disorder' : 'ascii_pics/disorder',
    'donq' : 'ascii_pics/donQ',
    'catcher' : 'ascii_pics/dream_catcher',
    'enterprise' : 'ascii_pics/enterprise',
    'cold' : 'ascii_pics/extreme_cold',
    'fort' : 'ascii_pics/fort',
    'snake' : 'ascii_pics/fractal_snake',
    'god' : 'ascii_pics/god',
    'kenny' : 'ascii_pics/kenny',
    'knight' : 'ascii_pics/knight',
    'mace' : 'ascii_pics/mace',
    'mountains' : 'ascii_pics/mountains',
    'mushroom_cloud' : 'ascii_pics/mushroom_cloud',
    'oxen' : 'ascii_pics/oxen',
    'pizza' : 'ascii_pics/pizza',
    'rain' : 'ascii_pics/rain',
    'repair' : 'ascii_pics/repair',
    'snake' : 'ascii_pics/snake',
    'spare_parts' : 'ascii_pics/spare_parts',
    'steam_wagon' : 'ascii_pics/steam_wagon',
    'terminator' : 'ascii_pics/terminator',
    'tornado' : 'ascii_pics/tornado',
    'treason' : 'ascii_pics/treason',
    'vicodin' : 'ascii_pics/vicodin',
}
