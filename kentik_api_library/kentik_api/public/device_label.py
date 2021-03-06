from typing import List, Any, Optional
from dataclasses import dataclass


@dataclass
class DeviceItem:

    id: str
    device_name: str
    device_subtype: str
    device_type: Optional[str]


class DeviceLabel:
    def __init__(
        self,
        name: str,
        color: Optional[str] = None,
        id: Optional[int] = None,
        user_id: Optional[str] = None,
        company_id: Optional[str] = None,
        devices: Optional[List[DeviceItem]] = None,
        created_date: Optional[str] = None,
        updated_date: Optional[str] = None,
    ) -> None:
        # read-write
        self.name = name
        self.color = color

        # read-only
        self._id = id
        self._user_id = user_id
        self._company_id = company_id
        self._devices = devices
        self._created_date = created_date
        self._updated_date = updated_date

    @property
    def id(self) -> int:
        assert self._id is not None
        return self._id

    @property
    def user_id(self) -> Optional[str]:
        return self._user_id

    @property
    def company_id(self) -> Optional[str]:
        return self._company_id

    @property
    def devices(self) -> List[DeviceItem]:
        return [] if self._devices is None else self._devices

    @property
    def created_date(self) -> Optional[str]:
        return self._created_date

    @property
    def updated_date(self) -> Optional[str]:
        return self._updated_date
