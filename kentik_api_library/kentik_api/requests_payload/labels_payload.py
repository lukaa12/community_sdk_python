# Standard library imports
import json
from typing import Optional, Dict, List, Any
from dataclasses import dataclass

# Local imports
from kentik_api.public.device_label import DeviceLabel, DeviceItem


@dataclass()
class _Device:
    id: str
    device_name: str
    device_subtype: str
    device_type: Optional[str] = None

    def to_device_item(self) -> DeviceItem:
        return DeviceItem(
            id=self.id, device_name=self.device_name, device_subtype=self.device_subtype, device_type=self.device_type
        )


class _DeviceArray(List[_Device]):
    @classmethod
    def from_list(cls, items: List[Dict[str, Any]]):
        devices = cls()
        for item in items:
            d = _Device(**item)
            devices.append(d)
        return devices

    def to_device_items(self) -> List[DeviceItem]:
        return [d.to_device_item() for d in self]


@dataclass()
class GetResponse:
    id: int
    name: str
    color: str
    user_id: str
    company_id: str
    devices: _DeviceArray
    created_date: str
    updated_date: str
    order: Optional[int] = None

    @classmethod
    def from_json(cls, json_string):
        dic = json.loads(json_string)
        dic["devices"] = _DeviceArray.from_list(dic["devices"])
        return cls(**dic)

    def to_device_label(self) -> DeviceLabel:
        return DeviceLabel(
            self.name,
            self.color,
            self.id,
            self.user_id,
            self.company_id,
            self.devices.to_device_items(),
            self.created_date,
            self.updated_date,
        )


class GetAllResponse(List[GetResponse]):
    @classmethod
    def from_json(cls, json_string):
        dic = json.loads(json_string)
        labels = cls()
        for item in dic:
            l = GetResponse(
                id=item["id"],
                name=item["name"],
                color=item["color"],
                user_id=item["user_id"],
                company_id=item["company_id"],
                devices=_DeviceArray.from_list(item["devices"]),
                created_date=item["created_date"],
                updated_date=item["updated_date"],
                order=item.get("order"),
            )
            labels.append(l)
        return labels

    def to_device_labels(self) -> List[DeviceLabel]:
        return [l.to_device_label() for l in self]


@dataclass()
class CreateRequest:
    name: str  # eg. "apitest-label-1"
    color: str  # eg. "#00FF00"


CreateResponse = GetResponse


@dataclass()
class UpdateRequest:
    name: str
    color: Optional[str] = None


UpdateResponse = GetResponse


@dataclass()
class DeleteResponse:
    success: bool

    @classmethod
    def from_json(cls, json_string):
        dic = json.loads(json_string)
        return cls(**dic)
