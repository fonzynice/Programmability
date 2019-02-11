from datetime import datetime

print('-'*62)
d_t = datetime.now()
print(d_t.strftime('Today is: %A %b-%d-%Y and current Time is: %I:%M:%S %p '))
print('-'*62, '\n')

# variables
commands_lists = []

commands = {
    'description': 'description {}',
    'speed': 'speed {}',
    'duplex': 'duplex {}'
    }

config_parameters = {
    'description': 'auto description by python',
    'speed': '10000',
    'duplex': 'auto'
    }


for feature, value in config_parameters.items():
    comm = commands.get(feature).format(value)
    commands_lists.append(comm)
    # print(commands_lists)
commands_lists.insert(0, 'interface Eth1/1')
# print(commands_lists)

#

hostname = ['r1', 'r2', 'r3', 'r4', 'r5']
configurations = ['config t', 'Ethernet 1/1', 'shutdown']
ip_address = '192.168.2.1'

send = '\n'.join(configurations)
# ping = 'ping {}'.format(ip_address)
# print(ping)

operation = dict(CPU='10%', Memory='4%')
config_parameters.update(operation)
# print(config_parameters)

# for key, value in config_parameters.items():
#     print(key, ':', value)

vendors = ['Cisco', 'Arista', 'Juniper', 'HP', 'Cumulus']
approved_vendors = ['Cisco', 'Juniper']

cfg = ['config t', 'interface Eth1/1', 'ip address', '10.10.10.1 255.0.0.0', 'no shutdown' ]
cfg_join = '\n'.join(cfg)


def send_cfg():
    for vendor in vendors:
        if vendor not in approved_vendors:
            print('Vendor NOT on the approved List: *{}'.format(vendor))


# send_cfg()
c = []
for feat, value in commands.items():
    c.append(feat)
    # print(feat, value)
c.insert(0, 'Eth1/1')
# print(c)

devices = ['switch1', 'switch2', 'switch3']
vlans = [
        {'id': '10', 'name': 'USERS'},
        {'id': '20', 'name': 'VOICE'},
        {'id': '30', 'name': 'WLAN'}
        ]


def get_command(vlan, name):
    com_mands = []
    com_mands.append('vlan'+ vlan)
    com_mands.append('name: ' + name)
    return com_mands
    # print(com_mands)


def push_command(devices, com_mands):
    print('Connecting to device', devices)
    for cmd in com_mands:
        print('Sending com_mands', cmd)


for vlan in vlans:
    v_id = vlan.get('id')
    v_name = vlan.get('name')
    print('\n')
    print('Configuring Vlan:', v_id)
    com_mands = get_command(v_id, v_name)
    for device in devices:
        push_command(device, com_mands)
        print('\n')


# get_command(v_id, v_name)
#
# push_command(devices, com_mands )