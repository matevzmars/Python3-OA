#!/usr/bin/env python3
import ev3dev.ev3 as ev3

p=ev3.PowerSupply()

print('Max voltage %s' % p.max_voltage)
print('Measured amps %s' % p.measured_amps)
print('Measured current %s' % p.measured_current)
print('Measured voltage %s' % p.measured_voltage)
print('Measured volts %s' % p.measured_volts)
print('Min voltage %s' % p.min_voltage)
print('Technology %s' % p.technology)
print('Type %s' % p.type)

print('...Konec...')
