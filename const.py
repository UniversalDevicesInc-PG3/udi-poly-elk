

NODE_DEF_MAP = {
    'area': {
        'ST': {
            'name':    'Alarm State',
            'nls':     'ALARM',
            'keys': {
                -1: 'Unknown',
                0:  'No Alarm Active',
                1:  'Entrance Delay is Active',
                2:  'Alarm Abort Delay Active',
                3:  'Fire Alarm',
                4:  'Medical Alarm',
                5:  'Police Alarm',
                6:  'Burglar Alarm',
                7:  'Aux 1 Alarm',
                8:  'Aux 2 Alarm',
                9:  'Aux 3 Alarm',
                10: 'Aux 4 Alarm',
                11: 'Carbon Monoxide Alarm',
                12: 'Emergency Alarm',
                13: 'Freeze Alarm',
                14: 'Gas Alarm',
                15: 'Heat Alarm',
                16: 'Water Alarm',
                17: 'Fire Supervisory',
                18: 'Verify Fire'
            },
        },
        'GV0': {
            'name':    'Armed Status',
            'nls':     'ASTATUS',
            'keys': {
                -1: 'Unknown',
                0:  'Disarmed',
                1:  'Armed Away',
                2:  'Amred Stay',
                3:  'Armed Stay Instant',
                4:  'Armed Night',
                5:  'Armed Niget Instant',
                6:  'Armed Vacation',
                7:  'Armed next Away Mode',
                8:  'Amred next Stay Mode',
                9:  'Force Arm to Away Mode',
                10: 'Force Arm to Stay Mode'
            }
        },
        'GV1': {
            'name':   'Arm Up State',
            'nls':    'ARMUP',
            'keys': {
                -1:  'Unknown',
                 0:  'Not Ready To Arm',
                 1:  'Ready To Arm',
                 2:  'Ready To Arm, but a zone violated and can be Force Armed',
                 3:  'Armed with Exit Timer working',
                 4:  'Armed Fully',
                 5:  'Force Armed with a force arm zone violated',
                 6:  'Armed with a bypass'
            }
        },
        'GV3': {
            'name':   'Violated Count',
            'uom':    56,
        },
        'GV4': {
            'name':   'Bypassed Count',
            'uom':    56,
        }
    },
    'zone': {
        'GV0': {
            'name': 'Physical Status',
            'nls':  'ZLST',
            'keys': {
                -1:  'Unknown',
                 0:  'Unconfigured',
                 1:  'Open',
                 2:  'EOL',
                 3:  'SHORT',
            }
        },
        'GV1': {
            'name': 'Triggered Alarm',
            'nls':  '',
            'keys': {
                 0:  'False',
                 1:  'True',
            }
        },
        'ST': {
            'name': 'Logical Status',
            'nls':  'ZPST',
            'keys': {
                -1:  'Unknown',
                0:  'Normal',
                1:  'Trouble',
                2:  'Violated',
                3:  'Bypassed',
            }
        }
    }
}

ELK_TO_INDEX = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    ':': 10,
    ';': 11,
    '<': 12,
    '=': 13,
    '>': 14,
    '?': 15,
    '@': 16,
    'A': 17,
    'B': 18
}

SYSTEM_TROUBLE_STATUS = {
    'AC Fail': { 'driver': 'GV3' },
    'Fail To Communicate': { 'driver': 'GV5' },
    'EEProm Memory Error': { 'driver': 'GV6' },
    'Low Battery Control': { 'driver': 'GV7' },
    'Over Current': { 'driver': 'GV9' },
    'Telephone Fault': { 'driver': 'GV10' },
    'Output 2': { 'driver': 'GV11' },
    'Missing Keypad': { 'driver': 'GV12' },
    'Zone Expander': { 'driver': 'GV13' },
    'Output Expander': { 'driver': 'GV14' },
    'ELKRP Remote Access': { 'driver': 'GV15' },
    'Common Area Not Armed': { 'driver': 'GV16' },
    'Flash Memory Error': { 'driver': 'GV17' },
    'Serial Port Expander': { 'driver': 'GV19' },
    'GE Smoke CleanMe': { 'driver': 'GV21' },
    'Ethernet': { 'driver': 'GV22' },
    'Display Message In Keypad Line 1': { 'driver': 'GV23' },
    'Display Message In Keypad Line 2': { 'driver': 'GV24' },
}

SYSTEM_TROUBLE_STATUS_ZONE = {
    'Box Tamper': { 'driver': 'GV11' },
    'Transmitter Low Battery': { 'driver': 'GV12' },
    'Security Alert': { 'driver': 'GV13' },
    'Lost Transmitter': { 'driver': 'GV14' },
    'Fire': { 'driver': 'GV15' },
}

# The defined ELK Speak Words
# Do not add any to this list since it will change
# the nls order and mess up existing programs.
# If new words are added they will need to be in a
# new list.
SPEAK_WORDS = {
    1: "_Custom1",
    2: "_Custom2",
    3: "_Custom3",
    4: "_Custom4",
    5: "_Custom5",
    6: "_Custom6",
    7: "_Custom7",
    8: "_Custom8",
    9: "_Custom9",
    10: "_Custom10",
    11: "Not Implemented",
    12: "Not Implemented",
    13: "Not Implemented",
    14: "Not Implemented",
    15: "Not Implemented",
    16: "Not Implemented",
    17: "Not Implemented",
    18: "Not Implemented",
    19: "Not Implemented",
    20: "Not Implemented",
    21: "Zero",
    22: "One",
    23: "Two",
    24: "Three",
    25: "Four",
    26: "Five",
    27: "Six",
    28: "Seven",
    29: "Eight",
    30: "Nine",
    31: "Ten",
    32: "Eleven",
    33: "Twelve",
    34: "Thirteen",
    35: "Fourteen",
    36: "Fifteen",
    37: "Sixteen",
    38: "Seventeen",
    39: "Eighteen",
    40: "Nineteen",
    41: "Twenty",
    42: "Thirty",
    43: "Fourty",
    44: "Fifty",
    45: "Sixty",
    46: "Seventy",
    47: "Eighty",
    48: "Ninety",
    49: "Hundred",
    50: "Thousand",
    51: "[200ms_Silence]",
    52: "[500ms_Silence]",
    53: "[800hz_Tone]",
    54: "A",
    55: "Access",
    56: "Acknowledged",
    57: "AC_power",
    58: "Activate",
    59: "Activated",
    60: "Active",
    61: "Adjust",
    62: "Air",
    63: "Alarm",
    64: "Alert",
    65: "All",
    66: "AM",
    67: "An",
    68: "And",
    69: "Answer",
    70: "Any",
    71: "Are",
    72: "Area",
    73: "Arm",
    74: "Armed",
    75: "At",
    76: "Attic",
    77: "Audio",
    78: "Auto",
    79: "Authorized",
    80: "Automatic",
    81: "Automation",
    82: "Auxiliary",
    83: "Away",
    84: "B",
    85: "Back",
    86: "Barn",
    87: "Basement",
    88: "Bathroom",
    89: "Battery",
    90: "Bedroom",
    91: "Been",
    92: "Bell",
    93: "Bottom",
    94: "Break",
    95: "Breakfast",
    96: "Bright",
    97: "Building",
    98: "Burglar",
    99: "Button",
    100: "By",
    101: "Bypassed",
    102: "Cabinet",
    103: "Call",
    104: "Camera",
    105: "Cancel",
    106: "Carbon_monoxide",
    107: "Card",
    108: "Center",
    109: "Central",
    110: "Change",
    111: "Check",
    112: "Chime",
    113: "Circuit",
    114: "Clear",
    115: "Closed",
    116: "Closet",
    117: "Code",
    118: "Cold",
    119: "Condition",
    120: "Connect",
    121: "Control",
    122: "Cool",
    123: "Cooling",
    124: "Corner",
    125: "Crawlspace",
    126: "Danger",
    127: "Day",
    128: "Deck",
    129: "Decrease",
    130: "Defective",
    131: "Degrees",
    132: "Delay",
    133: "Den",
    134: "Denied",
    135: "Detected",
    136: "Detector",
    137: "Device",
    138: "Dial",
    139: "Dialing",
    140: "Dim",
    141: "Dining_room",
    142: "Disable",
    143: "Disarm",
    144: "Disarmed",
    145: "Dock",
    146: "Door",
    147: "Doors",
    148: "Down",
    149: "Driveway",
    150: "East",
    151: "Emergency",
    152: "Enable",
    153: "End",
    154: "Energy",
    155: "Enrollment",
    156: "Enter",
    157: "Entering",
    158: "Entertainment",
    159: "Enter_the",
    160: "Entry",
    161: "Environment",
    162: "Equipment",
    163: "Error",
    164: "Evacuate",
    165: "Event",
    166: "Exercise",
    167: "Expander",
    168: "Exit",
    169: "Exterior",
    170: "F",
    171: "Fail",
    172: "Failure",
    173: "Family_room",
    174: "Fan",
    175: "Feed",
    176: "Fence",
    177: "Fire",
    178: "First",
    179: "Flood",
    180: "Floor",
    181: "Followed",
    182: "Force",
    183: "Fountain",
    184: "Foyer",
    185: "Freeze",
    186: "Front",
    187: "Full",
    188: "Furnace",
    189: "Fuse",
    190: "Game",
    191: "Garage",
    192: "Gas",
    193: "Gate",
    194: "Glass",
    195: "Go",
    196: "Good",
    197: "Goodbye",
    198: "Great",
    199: "Group",
    200: "Guest",
    201: "Gun",
    202: "Hall",
    203: "Hallway",
    204: "Hanging_up",
    205: "Hang_up",
    206: "Has",
    207: "Has_Expired",
    208: "Have",
    209: "Hear_menu_options",
    210: "Heat",
    211: "Help",
    212: "High",
    213: "Hold",
    214: "Home",
    215: "Hot",
    216: "Hottub",
    217: "House",
    218: "Humidity",
    219: "HVAC",
    220: "If",
    221: "Immediately",
    222: "In",
    223: "Inches",
    224: "Increase",
    225: "Inner",
    226: "Input",
    227: "Inside",
    228: "Instant",
    229: "Interior",
    230: "In_The",
    231: "Intruder",
    232: "Intrusion",
    233: "Invalid",
    234: "Is",
    235: "Is_about_to_expire",
    236: "Is_active",
    237: "Is_armed",
    238: "Is_canceled",
    239: "Is_closed",
    240: "Is_disarmed",
    241: "Is_low",
    242: "Is_off",
    243: "Is_OK",
    244: "Is_on",
    245: "Is_open",
    246: "Jacuzzi",
    247: "Jewelry",
    248: "Keep",
    249: "Key",
    250: "Keypad",
    251: "Kitchen",
    252: "Lamp",
    253: "Laundry",
    254: "Lawn",
    255: "Leak",
    256: "Leave",
    257: "Left",
    258: "Less",
    259: "Level",
    260: "Library",
    261: "Light",
    262: "Lights",
    263: "Line",
    264: "Living_room",
    265: "Loading",
    266: "Lobby",
    267: "Location",
    268: "Lock",
    269: "Low",
    270: "Lower",
    271: "M",
    272: "Machine",
    273: "Mail",
    274: "Main",
    275: "Mains",
    276: "Manual",
    277: "Master",
    278: "Max",
    279: "Media",
    280: "Medical",
    281: "Medicine",
    282: "Memory",
    283: "Menu",
    284: "Message",
    285: "Middle",
    286: "Minute",
    287: "Missing",
    288: "Mode",
    289: "Module",
    290: "Monitor",
    291: "More",
    292: "Motion",
    293: "Motor",
    294: "Next",
    295: "Night",
    296: "No",
    297: "Normal",
    298: "North",
    299: "Not",
    300: "Notified",
    301: "Now",
    302: "Number",
    303: "Nursery",
    304: "Of",
    305: "Off",
    306: "Office",
    307: "Oh",
    308: "OK",
    309: "On",
    310: "Online",
    311: "Only",
    312: "Open",
    313: "Operating",
    314: "Option",
    315: "Or",
    316: "Other",
    317: "Out",
    318: "Outlet",
    319: "Output",
    320: "Outside",
    321: "Over",
    322: "Overhead",
    323: "Panel",
    324: "Panic",
    325: "Parking",
    326: "Partition",
    327: "Patio",
    328: "Pause",
    329: "Perimeter",
    330: "Personal",
    331: "Phone",
    332: "Place",
    333: "Play",
    334: "Please",
    335: "Plus",
    336: "PM",
    337: "Police",
    338: "Pool",
    339: "Porch",
    340: "Port",
    341: "Pound",
    342: "Pounds",
    343: "Power",
    344: "Press",
    345: "Pressure",
    346: "Problem",
    347: "Program",
    348: "Protected",
    349: "Pump",
    350: "Radio",
    351: "Raise",
    352: "Ready",
    353: "Rear",
    354: "Receiver",
    355: "Record",
    356: "Recreation",
    357: "Relay",
    358: "Remain_calm",
    359: "Remote",
    360: "Repeat",
    361: "Report",
    362: "Reporting",
    363: "Reset",
    364: "Restored",
    365: "Return",
    366: "Right",
    367: "Roof",
    368: "Room",
    369: "Running",
    370: "Safe",
    371: "Save",
    372: "Screen",
    373: "Second",
    374: "Secure",
    375: "Security",
    376: "Select",
    377: "Sensor",
    378: "Serial",
    379: "Service",
    380: "Set",
    381: "Setback",
    382: "Setpoint",
    383: "Setting",
    384: "Shed",
    385: "Shipping",
    386: "Shock",
    387: "Shop",
    388: "Shorted",
    389: "Shunted",
    390: "Side",
    391: "Silence",
    392: "Siren",
    393: "Sliding",
    394: "Smoke",
    395: "Someone",
    396: "South",
    397: "Spare",
    398: "Speaker",
    399: "Sprinkler",
    400: "Stairs",
    401: "Stairway",
    402: "Star",
    403: "Start",
    404: "Status",
    405: "Stay",
    406: "Stock",
    407: "Stop",
    408: "Storage",
    409: "Storm",
    410: "Studio",
    411: "Study",
    412: "Sump",
    413: "Sun",
    414: "Switch",
    415: "System",
    416: "Tamper",
    417: "Tank",
    418: "Task",
    419: "Telephone",
    420: "Television",
    421: "Temperature",
    422: "Test",
    423: "Thank_you",
    424: "That",
    425: "The",
    426: "Theater",
    427: "Thermostat",
    428: "Third",
    429: "Time",
    430: "Toggle",
    431: "Top",
    432: "Transformer",
    433: "Transmitter",
    434: "Trespassing",
    435: "Trouble",
    436: "Turn",
    437: "Twice",
    438: "Type",
    439: "Under",
    440: "Unit",
    441: "Unlocked",
    442: "Unoccupied",
    443: "Up",
    444: "User",
    445: "Utility",
    446: "Vacation",
    447: "Valve",
    448: "Video",
    449: "Violated",
    450: "Visitor",
    451: "Wake_up",
    452: "Walk",
    453: "Wall",
    454: "Warehouse",
    455: "Warning",
    456: "Water",
    457: "Way",
    458: "Welcome",
    459: "West",
    460: "What",
    461: "When",
    462: "Where",
    463: "Will",
    464: "Window",
    465: "Windows",
    466: "With",
    467: "Work",
    468: "Yard",
    469: "Year",
    470: "You",
    471: "Zone",
    472: "Zones",
}

SPEAK_PHRASES = {
    209: "Keypad Panic Alarm",
    210: "AC Power Failure",
    211: "Telephone Line Trouble",
    212: "Alarm Silence",
    213: "Alarm Acknowledged",
    214: "(Area X) Is Armed Away Mode",
    215: "(Area X) Is Armed Stay Mode",
    216: "(Area X) Is Armed Stay Instant",
    217: "(Area X) Is Armed Night Mode",
    218: "(Area X) Is Armed Night Instant",
    219: "(Area X) Is Armed Vacation Mode",
    220: "(Area X) Exit Delay Is About To Expire",
    221: "Auto Arm In 1 Minute",
    222: "Exit Error",
    223: "Closing Ring Back",
    224: "Audio Module Missing",
    225: "System Is Armed",
    226: "(Area X) Is Disarmed",
    227: "Input Expander Missing",
    228: "Keypad Missing",
    229: "No Zones Violated",
    230: "Output Expander Missing",
    231: "Welcome System Is On",
    232: "Start Module Enrollment",
    233: "Stop Module Enrollment",
    234: "System Battery Is Low",
    235: "Press Transmitter Button",
    236: "Receiver Program Invalid",
    237: "Test Volume",
    238: "Say Time",
    239: "Miscellaneous 1",
    240: "Miscellaneous 2",
    241: "Miscellaneous 3",
    242: "Miscellaneous 4",
    243: "Miscellaneous 5",
    244: "Miscellaneous 6",
    245: "Miscellaneous 7",
    246: "Miscellaneous 8",
    247: "Miscellaneous 9",
    248: "Miscellaneous 10",
    249: "Enter Pass Code",
    250: "Access Allowed",
    251: "System Not Ready",
    252: "Select Task Number",
    253: "Select Light Number",
    254: "Select Output Number",
    255: "Select Temperature Sensor",
    256: "Select Keypad Number",
    257: "Select Thermostat Number",
    258: "Press To Change",
    259: "Press To End Message",
    260: "Phone Menu 0 - Hear Menu Options",
    261: "Phone Menu 1 - Arm/Disarm Status",
    262: "Phone Menu 2 - Automation Control",
    263: "Automation Menu 1 - Automation Task",
    264: "Automation Menu 2 - Lighting Control",
    265: "Automation Menu 3 - Output Control",
    266: "Automation Menu 4 - Temperature Sensor",
    267: "Automation Menu 5 - Keypad Temperature",
    268: "Automation Menu 6 - Thermostat Temperature",
    269: "Phone Menu 3 - System Summary",
    270: "Phone Menu 4 - Zone Status",
    271: "Phone Menu 7 - Page",
    272: "Phone Menu 8 - Adjust Volume",
    273: "Phone Menu 9 - Exit and Hangup",
    274: "Phone Arming",	
}