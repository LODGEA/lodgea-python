
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from lodgea-python.api.availability_api import AvailabilityApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from com.lodgea.controllers.availability_api import AvailabilityApi
from com.lodgea.controllers.location_api import LocationApi
from com.lodgea.controllers.property_api import PropertyApi
