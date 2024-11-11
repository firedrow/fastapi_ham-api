"""app/models/repeater.py.

MongoDB model for the repeaters collection.
"""

from enum import Enum
from typing import Optional, List
from pydantic import BaseModel
from beanie import Document


class StatusEnum(str, Enum):
    """Status of Repeaters."""
    ONLINE = "online"
    OFFLINE = "offline"


class DayEnum(str, Enum):
    """Days of the Week."""
    MONDAY = "Mon"
    TUESDAY = "Tue"
    WEDNESDAY = "Wed"
    THURSDAY = "Thu"
    FRIDAY = "Fri"
    SATURDAY = "Sat"
    SUNDAY = "Sun"


class BandEnum(str, Enum):
    """Bands that support repeaters."""
    M10 = "10m"
    M6 = "6m"
    M2 = "2m"
    M125 = "1.25m"
    CM70 = "70cm"
    CM33 = "33cm"
    CM23 = "23cm"


class CtcssToneEnum(str, Enum):
    """CTCSS Tones."""
    C670 = "67.0"
    C693 = "69.3"
    C719 = "71.9"
    C744 = "74.4"
    C770 = "77.0"
    C797 = "79.7"
    C825 = "82.5"
    C854 = "85.4"
    C885 = "88.5"
    C915 = "91.5"
    C948 = "94.8"
    C974 = "97.4"
    C1000 = "100.0"
    C1035 = "103.5"
    C1072 = "107.2"
    C1109 = "110.9"
    C1148 = "114.8"
    C1188 = "118.8"
    C1230 = "123.0"
    C1273 = "127.3"
    C1318 = "131.8"
    C1365 = "136.5"
    C1413 = "141.3"
    C1462 = "146.2"
    C1514 = "151.4"
    C1567 = "156.7"
    C1598 = "159.8"
    C1622 = "162.2"
    C1655 = "165.5"
    C1679 = "167.9"
    C1713 = "171.3"
    C1738 = "173.8"
    C1773 = "177.3"
    C1799 = "179.9"
    C1835 = "183.5"
    C1862 = "186.2"
    C1899 = "189.9"
    C1928 = "192.8"
    C1966 = "196.6"
    C1995 = "199.5"
    C2035 = "203.5"
    C2065 = "206.5"
    C2107 = "210.7"
    C2181 = "218.1"
    C2257 = "225.7"
    C2291 = "229.1"
    C2336 = "233.6"
    C2418 = "241.8"
    C2503 = "250.3"
    C2541 = "254.1"


class DcsToneEnum(str, Enum):
    """DCS Tones."""
    D023N = "D023N"
    D025N = "D025N"
    D026N = "D026N"
    D031N = "D031N"
    D032N = "D032N"
    D036N = "D036N"
    D047N = "D047N"
    D051N = "D051N"
    D053N = "D053N"
    D054N = "D054N"
    D065N = "D065N"
    D071N = "D071N"
    D072N = "D072N"
    D073N = "D073N"
    D074N = "D074N"
    D114N = "D114N"
    D115N = "D115N"
    D116N = "D116N"
    D122N = "D122N"
    D125N = "D125N"
    D131N = "D131N"
    D132N = "D132N"
    D134N = "D134N"
    D143N = "D143N"
    D145N = "D145N"
    D152N = "D152N"
    D155N = "D155N"
    D156N = "D156N"
    D162N = "D162N"
    D165N = "D165N"
    D172N = "D172N"
    D174N = "D174N"
    D205N = "D205N"
    D212N = "D212N"
    D223N = "D223N"
    D225N = "D225N"
    D226N = "D226N"
    D243N = "D243N"
    D244N = "D244N"
    D245N = "D245N"
    D246N = "D246N"
    D251N = "D251N"
    D252N = "D252N"
    D255N = "D255N"
    D261N = "D261N"
    D263N = "D263N"
    D265N = "D265N"
    D266N = "D266N"
    D271N = "D271N"
    D274N = "D274N"
    D306N = "D306N"
    D311N = "D311N"
    D315N = "D315N"
    D325N = "D325N"
    D331N = "D331N"
    D332N = "D332N"
    D343N = "D343N"
    D346N = "D346N"
    D351N = "D351N"
    D356N = "D356N"
    D364N = "D364N"
    D365N = "D365N"
    D371N = "D371N"
    D411N = "D411N"
    D412N = "D412N"
    D413N = "D413N"
    D423N = "D423N"
    D431N = "D431N"
    D432N = "D432N"
    D445N = "D445N"
    D446N = "D446N"
    D452N = "D452N"
    D454N = "D454N"
    D455N = "D455N"
    D462N = "D462N"
    D464N = "D464N"
    D465N = "D465N"
    D466N = "D466N"
    D503N = "D503N"
    D506N = "D506N"
    D516N = "D516N"
    D523N = "D523N"
    D526N = "D526N"
    D532N = "D532N"
    D546N = "D546N"
    D565N = "D565N"
    D606N = "D606N"
    D612N = "D612N"
    D624N = "D624N"
    D627N = "D627N"
    D631N = "D631N"
    D632N = "D632N"
    D645N = "D645N"
    D654N = "D654N"
    D662N = "D662N"
    D664N = "D664N"
    D703N = "D703N"
    D712N = "D712N"
    D723N = "D723N"
    D731N = "D731N"
    D732N = "D732N"
    D734N = "D734N"
    D743N = "D743N"
    D754N = "D754N"


class Nets(BaseModel):
    """Pydantic Base Model for the Nets class."""
    day: DayEnum
    time: str
    name: str


class Repeaters(Document):
    """Beanie Document for the repeaters collection."""
    class Settings:
        """Set the MongoDB Collection name."""
        name = "repeaters"

    name:               str
    status:             StatusEnum
    latitude:           Optional[float] = None
    longitude:          Optional[float] = None
    frequency_downlink: str
    frequency_uplink:   str
    frequency_offset:   str
    ctone_downlink:     Optional[CtcssToneEnum] = None
    ctone_uplink:       Optional[CtcssToneEnum] = None
    dtone_downlink:     Optional[DcsToneEnum] = None
    dtone_uplink:       Optional[DcsToneEnum] = None
    band:               BandEnum
    bandwidth:          float
    nets:               Optional[List[Nets]] = None
    country:            str
    state:              str
    county:             Optional[str] = None
    grid:               str
    sponsor:            str
    coordination:       str


class RepeatersCreate(Document):
    """Beanie Document for the repeaters collection."""
    class Settings:
        """Set the MongoDB Collection name."""
        name = "repeaters"

    name:               str
    status:             StatusEnum
    latitude:           Optional[float] = None
    longitude:          Optional[float] = None
    frequency_downlink: str
    frequency_uplink:   str
    frequency_offset:   str
    ctone_downlink:     Optional[CtcssToneEnum] = None
    ctone_uplink:       Optional[CtcssToneEnum] = None
    dtone_downlink:     Optional[DcsToneEnum] = None
    dtone_uplink:       Optional[DcsToneEnum] = None
    band:               BandEnum
    bandwidth:          float
    nets:               Optional[List[Nets]] = None
    country:            str
    state:              str
    county:             Optional[str]
    grid:               str
    sponsor:            str
    coordination:       str


class RepeatersUpdate(Document):
    """Beanie Document for the repeaters collection."""
    class Settings:
        """Set the MongoDB Collection name."""
        name = "repeaters"

    name:               Optional[str] = None
    status:             Optional[StatusEnum] = None
    latitude:           Optional[float] = None
    longitude:          Optional[float] = None
    frequency_downlink: Optional[str] = None
    frequency_uplink:   Optional[str] = None
    frequency_offset:   Optional[str] = None
    ctone_downlink:     Optional[CtcssToneEnum] = None
    ctone_uplink:       Optional[CtcssToneEnum] = None
    dtone_downlink:     Optional[DcsToneEnum] = None
    dtone_uplink:       Optional[DcsToneEnum] = None
    band:               Optional[BandEnum] = None
    bandwidth:          Optional[float] = None
    nets:               Optional[List[Nets]] = None
    country:            Optional[str] = None
    state:              Optional[str] = None
    county:             Optional[str] = None
    grid:               Optional[str] = None
    sponsor:            Optional[str] = None
    coordination:       Optional[str] = None
