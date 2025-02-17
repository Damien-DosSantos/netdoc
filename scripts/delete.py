"""Delete all data.

Usage:
/opt/netbox/venv/bin/python3 /opt/netbox/netbox/manage.py shell < delete.py
"""

from dcim.models import (
    Device,
    DeviceRole,
    DeviceType,
    Manufacturer,
    Cable,
    CableTermination,
    Interface,
    CablePath,
)
from extras.models import JobResult
from ipam.models import IPAddress, Prefix, VRF
from netdoc.models import ArpTableEntry, MacAddressTableEntry, RouteTableEntry


Cable.objects.all().delete()
CableTermination.objects.all().delete()
CablePath.objects.all().delete()  # pylint: disable=no-member
Device.objects.all().delete()
DeviceRole.objects.all().delete()
DeviceType.objects.all().delete()
Manufacturer.objects.all().delete()
Prefix.objects.all().delete()
IPAddress.objects.all().delete()
Interface.objects.all().delete()
ArpTableEntry.objects.all().delete()
MacAddressTableEntry.objects.all().delete()
RouteTableEntry.objects.all().delete()
VRF.objects.all().delete()
JobResult.objects.all().delete()

# from netdoc.models import DiscoveryLog # Danger
# DiscoveryLog.objects.all().delete() # Danger
