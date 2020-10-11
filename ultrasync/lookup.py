# -*- coding: utf-8 -*-
#
# All rights reserved.
#
# This code is licensed under the MIT License.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files(the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and / or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions :
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# defaultNames Array() - v_ZW_03.02-C/en_us.js
DEFAULT_NAMES = (
    '',
    '',
    'Sensor',
    'Area',
    'Channel',
    '',
    'Schedule',
    'Action',
    'Arm-Disarm',
    '',
    'Permission',
    'Area Group',
    'Menu',
    'Holiday',
    'Sensor Type',
    'Sensor Options',
    'Event List',
    'Channel Group',
    'Action group',
    'Scene',
    '',
    'Camera',
    'UltraSync',
)

# groupingNames Array() - v_ZW_03.02-C/en_us.js
GROUPING_NAMES = (
    'Select Sensor to Configure',
    'Select Keyfob to Configure',
    'Select Area to Configure',
    'Area Timers',
    'Area Options',
    'Area Reporting',
    'System Date and Time',
    'System Time Zone',
    'System Daylight Saving Time',
    'System Timers',
    'System Options',
    'System Reporting',
    'Select Channel to Configure',
    'LAN configuration',
    'WiFi Configuration',
    'Remote Access PINS',
    'Options',
    'Select Scene to Configure',
    'Scene Trigger',
    'Scene Result',
    'Select Schedule to Configure',
    'Time and Days 1',
    'Time and Days 2',
    'Time and Days 3',
    'Time and Days 4',
    'Select Holiday List to Configure',
    'Start Date',
    'End Date',
    'Connection Status',
    'Cellular Radio Details',
    'WiFi Details',
    'Device Details',
    'Camera Configuration',
    'Camera Network Configuration',
)

# firstArray Array() - v_ZW_03.02-C/en_us.js
FIRST = (
    'Disabled',
    'Always On',
    'Backup Channel Only',
)

# setNames Array() - v_ZW_03.02-C/en_us.js
NAMES = (
    'Sensors',
    'Keyfobs',
    '',
    'Areas',
    'System',
    'Reporting and Notifications',
    'Network',
    'Automations (Scenes)',
    'Schedules',
    'Holidays',
    'Z-Wave Room Names',
    'Z-Wave Add/Remove',
    'Z-Wave Device Association',
    'Z-Wave Maintenance',
    'WiFi Setup',
    'Cameras',
    'Connection Status',
    'Details',
    'Walk Test',
    'Lock PIN Share',
)

SCENE_STATES = (
    'Disabled',
    'Sensor Bypass',
    'Arm Away',
    'Disarm',
    'Arm Stay',
    'Restart AutoArm Timer',
    'Arm Away - No Auto Stay',
    'Chime On',
    'Chime Off',
    'Activate Scene',
    'Trigger Camera Video Clip',
    'Send Area Notification',
    'Send Sensor Notification',
    'Send Notification',
    'Start Siren',
)

SCENE_ACTIVATION = (
    'Disable',
    'Sensor Open',
    'Sensor Not Open',
    'Sensor Alarm',
    'Area Armed Away',
    'Area Armed + Bypass',
    'Area Armed Stay',
    'Area Not Armed Away',
    'Entry Delay',
    'Exit Delay 1',
    'Exit Delay 2',
    'Area Sensor Bypass',
    'Area Tamper',
    'Area Not Ready to Arm',
    'Area Sensor Low Battery',
    'Area Sensor Supervision Fault',
    'Area Alarm',
    'Area Burg Alarm',
    'Area Fire Alarm',
    'Area Panic Alarm',
    'Area Auxiliary Alarm',
    'Area Siren',
    'Area Fire Siren',
    'User PIN entered',
    'Action Function True',
    'Action Function False',
    'Schedule Activated',
    'Schedule Deactivated',
    'Smoke Power Reset',
    'Turn On By User',
    'Turn Off By User',
    'Geo Radius Entered',
    'Geo Radius Exited',
    '!',
    '!',
    'Key A',
    'Key B',
    'Key C',
    'Siren On',
    'Z-Wave Devices (Beta)',
    'Sunrise',
    'Sunset',
    'Camera Motion Detection',
    'Doorbell Camera Button Press',
    '!',
)

# voicetokens Array() - v_ZW_03.02-C/en_us.js
VOICE_TOKENS = (
    'ZERO',
    'ONE',
    'TWO',
    'THREE',
    'FOUR',
    'FIVE',
    'SIX',
    'SEVEN',
    'EIGHT',
    'NINE',
    'TEN',
    'ELEVEN',
    'TWELVE',
    'THIRTEEN',
    'FOURTEEN',
    'FIFTEEN',
    'SIXTEEN',
    'SEVENTEEN',
    'EIGHTEEN',
    'NINETEEN',
    'TWENTY',
    'THIRTY',
    'FORTY',
    'FIFTY',
    'SIXTY',
    'SEVENTY',
    'EIGHTY',
    'NINETY',
    'HUNDRED',
    'THOUSAND',
    'AIR CONDITIONER',
    'AREA',
    'ATTIC',
    'AUTOMATIC',
    'AUXILLARY',
    'BACK',
    'BASEMENT',
    'BATHROOM',
    'BEDROOM',
    'BOAT',
    'CABINET',
    'CAR PARK',
    'CEILING',
    'CELLAR',
    'CHILDS',
    'ALERT',
    'CLOSET',
    'COMPUTER',
    'COOL',
    'CURTAIN',
    'DATA',
    'DEN',
    'DETECTOR',
    'DINING',
    'DOOR',
    'DOWNSTAIRS',
    'DRIVEWAY',
    'DURESS',
    'EAST',
    'EMERGENCY',
    'ENTRY',
    'FAMILY',
    'FAN',
    'FENCE',
    'FIRE',
    'FORCED ARM',
    'FOYER',
    'FREEZER',
    'FRONT',
    'GAMES',
    'GARAGE',
    'GAS',
    'GATE',
    'GLASS',
    'GLASSBREAK',
    'GROUND',
    'GUEST',
    'GUN',
    'GYM',
    'HALL',
    'HALLWAY',
    'HEAT',
    'HEATING',
    'HOLDUP',
    'HOME',
    'HOME THEATRE',
    'INFRARED',
    'INSIDE',
    'INSTANT',
    'INTERIOR',
    'KEYSWITCH',
    'KEYCHAIN',
    'KITCHEN',
    'LARGE',
    'LAUNDRY',
    'LIFT',
    'LIGHT',
    'LIVING',
    'LOCATION',
    'MASTER',
    'MEDICINE',
    'MEETING',
    'MOTION',
    'NIGHT',
    'NORTH',
    'NURSERY',
    'OFFICE',
    'OUTPUT',
    'OUTSIDE',
    'PANIC',
    'PANTRY',
    'PARTIAL',
    'PERIMETER',
    'POOL',
    'REAR',
    'RECEPTION',
    'REMOTE',
    'ROOF',
    'ROOM',
    'RUMPUS',
    'SAFE',
    'SECURITY',
    'SENSOR',
    'SHED',
    'SHOCK',
    'SHOP',
    'SIDE',
    'SKYLIGHT',
    'SLIDING',
    'SMALL',
    'SMOKE',
    'SOUTH',
    'STAIRS',
    'STORAGE',
    'STUDY',
    'TEMPERATURE',
    'SPARE3',
    'TOILET',
    'TRAINING',
    'TV',
    'UPSTAIRS',
    'USER',
    'UTILITY',
    'VOLT',
    'VERANDA',
    'WALL',
    'WAREHOUSE',
    'WATER',
    'WEST',
    'WINDOW',
    'WINDOWS',
    'WIRELESS',
    'YARD',
    '',
)

# languageStrings Array() - v_ZW_03.02-C/en_us.js
LANGUAGE_LOOKUP = (
    'Configuration Server',
    'Back',
    'Up',
    'Down',
    'Save',
    'All On',
    'All Off',
    'Shortcut',
    'disabled',
    'ON',
    'OFF',
    'Sensor Add/Remove Functions',
    'Learn',
    'Remove',
    'Cancel',
    'Select Menu:',
    'KeyFob',
    'Keypad',
    'Channel',
    'IP Address',
    'Gateway',
    'Subnet',
    'Primary DNS',
    'Secondary DNS',
    'Date',
    'Time',
    'Standard User Type (Fob Number)',
    'Discard Changes?',
    'Select a Room to Edit Names',
    'You must select a Menu before you can scroll',
    'Select a submenu from the list or select back to access the main menu',
    'Data limited to',
    'digits',
    'characters',
    'Data must only contain the following characters',
    'Date must be of the form YYYY-MM-DD.',
    'Month must be from 1 to 12 Use Get Calendar for easy formatting',
    'Day must be from 1 to 31',
    'Data entry must only contain the numbers 0 - 9 and A-F',
    'Data entry must only contain the numbers 0 - 9',
    'Data must be a number from',
    'To',
    'Enter Menu Shortcut',
    'Defaulting requires 2 levels',
    'Improper Time Value',
    'Settings Selector',
    'Reload',
    'Write Access Denied',
    'Nothing displayed can be Saved',
    'Program Success!',
    'Name Saved',
    'Select a device to Edit Names',
    'Or Click A Function Above',
    'Saving Room Name',
    'Room Name Saved',
    'Select a Room to Edit Name',
    'WiFi Mode Not Enabled',
    'Scan For WiFi Networks',
    'Are you sure you want to change the sensor ID and/or type?',
    'Activating Learn Mode',
    'New Device Found',
    'Click Save to Store New Device',
    'Learn Mode Active',
    'Activate Learn Button',
    'Wrong Device Type',
    'Activate Learn Mode Button on another device',
    'Are you sure you want to permanently delete Sensor?',
    'Use FOB Number as Standard User',
    'Please enter your WEP key',
    'No key entered',
    'WEP key is not the correct length',
    'Keys must be either:',
    '(a) 10 or 26 hexadecimal digits or',
    '(b) 5 or 13 ASCII characters',
    'Please enter your passphrase',
    'No passphrase entered',
    'WPA passphrase is not the correct length',
    'Passphrase must be 8-63 characters long',
    'SSID cannot be left blank!',
    'Please choose either adhoc or infrastructure',
    'This Page Is Under Construction',
    'System Name and Clock',
    'Area Name and Entry/Exit Times',
    'Changes Saved',
    'must be 4 to 8 digits',
    'Scan For New Cameras',
    'Unlocked',
    'Locked',
    'Unlocking…',
    'Locking…',
    'Timed Unlock',
    'Timed Unlock',
    'Open',
    'Closed',
    'Opening…',
    'Closing…',
    'Stopped',
    'Safety Delay',
    'Safety Delay',
    'Any User',
    'Voice Name',
    'Are you sure you want to delete camera',
    'High Temp',
    'Low Temp',
    'Select one or more triggers',
    'Enable External Contact',
    'Would you like to Supervise Output 2 as Sensor',
    'Would you like to Use input 1 as Sensor',
    'Would you like to Use input 2 as Sensor',
    'I/O Module',
    'Indoor Siren',
    'Outdoor Siren',
    'Transmitter Type',
)

# addRemStatus Array() - v_ZW_03.02-C/en_us.js
ADD_REMOVE_STATUS = (
    'Learn Ready. Activate Device Learn Sequence or Press Cancel',
    'Learn Ready. Activate Device Learn Sequence or Press Cancel',
    'Device Found',
    'Slave Found',
    'Adding Controller',
    'Protocol Query Done',
    'Done',
    'Failed',
)

# operatingModes Array() - v_ZW_03.02-C/en_us.js
OPERATING_MODES = (
    'OFF',
    'HEAT',
    'COOL',
    'AUTO',
    'E-HEAT',
    'RESUME',
    'FAN ONLY',
    'FURNACE',
    'DRY AIR',
    'MOIST AIR',
    'AUTOCH',
    'ESAVE-H',
    'ESAVE-C',
    'AWAY',
)

# operatingStates Array() - v_ZW_03.02-C/en_us.js
OPERATING_STATES = (
    'IDLE',
    'HEAT',
    'COOL',
    'FAN ONLY',
    'PENDING-HEAT',
    'PENDING-COOL',
    'VENT-ECONOMIZE',
)

# fanmodeNames Array() - v_ZW_03.02-C/en_us.js
FAN_MODES = (
    'AUTO',
    'ON',
    'AUTO-HIGH',
    'ON-HIGH',
    'AUTO-MED',
    'ON-MED',
    'CIRCULATE',
    'HUMIDIFY',
)

# zwaveStrings Array() - v_ZW_03.02-C/en_us.js
ZWAVE = (
    'Unavailable - Failed Device Function in progress',
    'Unavailable - Add mode active',
    'Unavailable - Remove mode active',
    'Unavailable - Resetting Network',
    'Unavailable - Backing Up Network',
    'Unavailable - Restoring Network',
    'Are you sure you want to delete all Devices?',
    'Are you sure you want to Restore a previous backup?',
    'Busy, Try Again Momentarily',
    'Not primary controller',
    'No Call Back Function',
    'Device Not found in failed list',
    'Remove Device failed - already in process',
    'Replace Device failed - already in process',
    'Remove Device Failed',
    'Replace Device Failed',
    'Device Removed',
    'Remove Failed',
    'Device ',
    ' Replaced',
    'Replace Failed',
    'Function timed out or cancelled',
    'Added Device ',
    'Enter Location Name and Device Name then click Save Device Name',
    'Removed Device ',
    'Select a device to Edit Names Or Click A Function Above',
    'No Device Added',
    'No Device Removed',
    'Network Reset ',
    'Select a device to Edit Names Or Click A Function Above',
    'Network Backed Up',
    'Network Restored',
    'Unavailable, Try Again Later',
    'Learn Ready',
    'Activate Device Learn Sequence on new Device ',
    ' Device',
    'Adding - ',
    'Removing - ',
    'Processing Request',
    'Resetting Network',
    'Backing Up Network',
    'Restoring Network',
    ' Associations',
    'Edit the Location and Device Name',
    'Then Click Save Device Name',
    'Or Click A Function Above',
    'Off',
    'On',
    'Turn Off',
    'Turn On',
    'Updating Status',
    'Command Failed',
    'Current Level ',
    'Association Add Done',
    'Association Remove Done',
    'Association Query Done',
    'FAN MODES',
    'Temperature',
    'Press Select for Set Points',
    'Fan Mode',
    'You must press Select to choose a set point',
    'You must select a failed Device other than 1',
    'Unable To Retrieve Thermostat Information',
    'SET POINT',
    'SELECT',
    'DOWN',
    'UP',
    'OPERATING MODES',
    'UNLOCK',
    'LOCK',
    'Room Selector',
    'All Lights',
    'All HVAC',
    'All Doors',
    'Z-Wave Device Selector',
    'Z-Wave Room Editor',
    'Device Room Location',
    'Device Name',
    'Add',
    'Remove',
    'Cancel',
    'Tick For High Power Add Option',
    'Device Add/Remove Functions',
    'Association Group',
    'Query',
    'Replace',
    'Remove',
    'Network Maintenance Functions',
    'Backup',
    'Restore',
    'Reset',
    'Adding devices to association',
    'Removing devices from association',
    'Querying for association devices',
    'Querying for failed devices',
    'Select Association Group',
    'Then Select Device',
    'Then Click Function Button',
    'Association Functions',
    'Failed Device Functions',
    'Failed Device Selector',
    'Association Selector',
    'There are no Failed Devices',
    'Include',
    'Open',
    'Close',
    'Mode',
    'Operating State',
    'Shift',
    'Exclude',
    'Replacing - ',
    'Room',
    'Unavailable - Rediscovering Network',
    'Rediscovery Complete',
    'Rediscovering',
    'Node Discovery Functions',
    'Rediscover',
    'Restart',
    'Select Door Lock',
    'All Users',
    'Select User(s)',
    'Send PIN(s) to Lock',
    'Remove PIN(s) from Lock',
    'Message Center',
    'Lock PIN Share Instructions',
    'Sending',
    'Removed',
    'Sent',
    'Building User List- Please Wait',
    '1. Select Door Lock.',
    '2. Select User(s).',
    '3. Press Send or Remove Function Button.',
    '4. Repeat Steps 1-3 as necessary.',
    '',
    'All PINS Updated',
    'Edit Room Name',
    'Are you sure you want to add this control to another Z-Wave network?',
    'Alarm is Primary Controller',
    'Alarm is Secondary Controller',
    'Error Occurred! Remove New Device and try again.',
)

# setPointNames Array() - v_ZW_03.02-C/en_us.js
POINT_NAMES = (
    'Not Used',
    'Heat',
    'Cool',
    'Furnace',
    'Dry Air',
    'Moist Air',
    'Auto Changeover',
    'E-Save Heat',
    'E-Save Cool',
    'Away Heat',
)

# areaStates Array() - v_ZW_03.02-C/en_us.js
AREA_STATES = (
    'Armed Away',
    'Armed Stay',
    'Ready',
    'Fire Alarm',
    'Burg Alarm',
    'Panic Alarm',
    'Auxiliary Alarm',
    'Exit Delay',
    'Exit Delay 2',
    'Entry Delay',
    'Sensor Bypass',
    'Sensor Trouble',
    'Sensor Tamper',
    'Sensor Low Battery',
    'Sensor Supervision',
    '',
)

# zoneStates Array() - v_ZW_03.02-C/en_us.js
ZONE_STATES = (
    'Not Ready',
    'Tamper',
    'Trouble',
    '',
    'Inhibited',
    'Alarm',
    'Low Battery',
    'Supervision Fault',
    'Test Fail',
    '',
    'Entry Delay',
    '',
    'Test Active',
    'Activity Fail',
    'Antimask',
)

# statusStrings Array() - v_ZW_03.02-C/en_us.js
STATUS_STATES = (
    'Updating System Data',
    'No System Faults',
    'No Areas Configured For Your Access',
    'All Areas',
    'Area',
    'Bypass',
    'Chime',
    'Ready',
    'Sensor',
    'No Sensors Configured For Your Access',
    'Away',
    'Stay',
    'Off',
    'Notify',
)

# pinStrings Array() - v_ZW_03.02-C/en_us.js
PIN = (
    'Add',
    'Edit',
    'Delete',
    'Save',
    'Entry must only contain the numbers 0 - 9',
    'You must enter a user Number between 1 and 999',
    'PIN digits must be between 0 and 9',
    'PIN must be from 4 to 8 digits!',
    'User Number',
    'Midnight',
    'Noon',
    'AM',
    'PM',
    'Schedule',
    'Select User',
    'First Name',
    'Last Name',
    'PIN',
    'User Type',
    'Standard',
    'Master',
    'Installer',
    'Master Installer',
    'Arm Only',
    'Duress',
    'Custom',
    'Start',
    'End',
    'Profile',
    'Pin Must be 4-8 digits from 0-9',
    'Configure Users',
    'Change PIN',
    'Sort by Name',
    'Language',
    'Minimum PIN length is',
    'Maximum PIN length is 8',
    'Display Area List',
    'Area Type Override',
    '',
    '',
)

# masterStrings Array() - v_ZW_03.02-C/en_us.js
MASTER = (
    'Connection Was lost before a response was received',
    'Try Switching to the new Network',
    'Menu',
    'Logout',
    'Arm/Disarm',
    'Sensors',
    'Cameras',
    'Rooms',
    'History',
    'Users',
    'Change PIN',
    'Settings',
    'Advanced',
    'Data must not contain the following characters',
    'No Cameras Configured.',
    'Contact your security and home automation dealer to add live video and '
    'recorded clips.',
    'No Camera Access On Local Area Network.',
    'Enter Your Name',
    'Enter Your Password',
    'Sign In',
    'Not Ready',
    'Not Ready - Force Armable',
    'Network Successfully Selected!',
    'Change your computer to the same network before Attempting to reconnect.',
    '',
)

# historyStrings Array() - v_ZW_03.02-C/en_us.js
HISTORY = (
    '|<',
    '<',
    '>',
    '>|',
    'Search',
    'Please select a date',
    'No Events Match Search Criteria',
    'Event History',
    'Select Date',
    'All Events',
    'Alarm Events',
    'Video Events',
    'Event Filter',
    'Press to Play',
)

# walktestStrings Array() - v_ZW_03.02-C/en_us.js
WALK_TEST = (
    'Walk Test Instuctions',
    'Start Walk Test',
    'End Walk Test',
    'Result',
    'Pass',
    'Fail',
    'To Test:',
    '1. Open (Trigger) Sensor',
    '3. Close (Restore) Sensor',
    '5. Check Result',
    'Current Noise Floor',
    'Peak Noise Floor',
    'Best Noise Floor',
    'Open (Trigger) Packets',
    'Open (Trigger) Signal Strength',
    'Close (Restore) Packets',
    'Close (Restore) Signal Strength',
    'Retrieving Data…',
    '6. Repeat Steps 1-5 for all sensors',
    'Wait 8 Seconds',
    'Excellent',
    'Good',
    'Fair ',
    'Poor',
    'None',
    'Siren Chirp ',
    'Downlink Signal Strength',
    'Uplink Signal Strength',
    'Module Noise Floor',
)
