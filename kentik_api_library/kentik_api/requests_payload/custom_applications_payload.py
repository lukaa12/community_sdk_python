import json
from typing import Optional, List
from dataclasses import dataclass

from kentik_api.public.custom_application import CustomApplication


@dataclass
class GetResponse:
    name: str
    description: str
    ip_range: str
    protocol: str
    port: str
    asn: str
    id: int
    company_id: str
    user_id: str
    cdate: Optional[str] = None
    edate: Optional[str] = None

    @classmethod
    def from_json(cls, json_string: str):
        dic = json.loads(json_string)
        return cls(**dic)

    def to_custom_application(self) -> CustomApplication:
        return CustomApplication(
            name=self.name,
            description=self.description,
            ip_range=self.ip_range,
            protocol=self.protocol,
            port=self.port,
            asn=self.asn,
            id=self.id,
            company_id=self.company_id,
            user_id=self.user_id,
            cdate=self.cdate,
            edate=self.edate,
        )


class GetAllResponse(List[GetResponse]):
    @classmethod
    def from_json(cls, json_string: str):
        dic = json.loads(json_string)
        apps = cls()
        for item in dic:
            a = GetResponse(**item)
            apps.append(a)
        return apps

    def to_custom_applications(self) -> List[CustomApplication]:
        return [a.to_custom_application() for a in self]


@dataclass
class CreateRequest:
    name: str
    description: Optional[str] = None
    ip_range: Optional[str] = None
    protocol: Optional[str] = None
    port: Optional[str] = None
    asn: Optional[str] = None


CreateResponse = GetResponse


@dataclass
class UpdateRequest:
    name: Optional[str] = None
    description: Optional[str] = None
    ip_range: Optional[str] = None
    protocol: Optional[str] = None
    port: Optional[str] = None
    asn: Optional[str] = None


UpdateResponse = GetResponse


# @dataclass()
# class DeleteResponse:
#     """ Currently custom application delete response carries no body data just http code 204 for succcess """
