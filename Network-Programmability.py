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


send_cfg()