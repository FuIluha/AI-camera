"""
example import Bridge
"""

from bridge import Bridge

bridge = Bridge()
for i in range(110):
    bridge.upload_data(i, i)
for i in range(110, 0, -1):
    bridge.upload_data(i, i)
