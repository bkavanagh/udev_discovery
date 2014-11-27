__author__ = 'brendan'


import pyudev
from os.path import commonprefix
import re
con = pyudev.Context()
a = set()
b = set()
cdc_devices = set()
cdc_children = list()


for dev in con.list_devices(subsystem='usb'):
    if dev.get('ID_MODEL_ID') == '2404':
        cdc_devices.add(dev)
    #print dev.get('DEVNAME')
    #print [each for each in dev.iteritems()]
    a.add(dev)
cdc_parent_nodes = set([d.parent.parent.device_path for d in cdc_devices])

cdc_children = set([d.device_path for d in a if d.parent.device_path in cdc_parent_nodes or d.parent.parent.device_path in cdc_parent_nodes]) - cdc_parent_nodes - set([d.device_path for d in cdc_devices])
slot_devices = [pyudev.Device.from_path(con, path) for path in cdc_children]
print cdc_children
for each in slot_devices:
    print each.device_path
    for x in each.iteritems():
        pass

raw_input('REMOVE A DEVICE AND PRESS ANY KEY')

for dev in con.list_devices(subsystem='usb'):
    #print dev.get('DEVNAME')
    #print [each for each in dev.iteritems()]
    b.add(dev)

#print [x for x in[y.device_path for y in slot_devices] if x.startswith('/devices/pci0000:00/0000:00:1d.7/usb2/2-1/2-1.2/')]
cp  = commonprefix([x.sys_path for x in slot_devices])
for each in slot_devices:
    new =  re.sub(cp,'', each.sys_path)
    if new.startswith('1'):
        print new, each.get('ID_SERIAL_SHORT')
        for x in each.iteritems():
            print x
    print '\n'