# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T13:32:14+00:00

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel, Field, RootModel, conint, constr


class AccessDeniedException(RootModel[Any]):
    root: Any


class AwsAccountId(RootModel[constr(pattern=r'^\d{12}$')]):
    root: constr(pattern=r'^\d{12}$')


class CapacityInBytes(RootModel[int]):
    root: int


class CidrBlock(RootModel[str]):
    root: str


class ConflictException(RootModel[Any]):
    root: Any


class CreationTime(RootModel[datetime]):
    root: datetime


class CustomerOwnedIpv4Pool(
    RootModel[constr(pattern=r'^ipv4pool-coip-([0-9a-f]{17})$')]
):
    root: constr(pattern=r'^ipv4pool-coip-([0-9a-f]{17})$')


class DeleteEndpointRequest(BaseModel):
    pass


class EndpointAccessType(Enum):
    Private = 'Private'
    CustomerOwnedIp = 'CustomerOwnedIp'


class EndpointArn(
    RootModel[
        constr(
            pattern=r'^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):s3-outposts:[a-z\-0-9]*:[0-9]{12}:outpost/(op-[a-f0-9]{17}|ec2)/endpoint/[a-zA-Z0-9]{19}$'
        )
    ]
):
    root: constr(
        pattern=r'^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):s3-outposts:[a-z\-0-9]*:[0-9]{12}:outpost/(op-[a-f0-9]{17}|ec2)/endpoint/[a-zA-Z0-9]{19}$'
    )


class EndpointId(RootModel[constr(pattern=r'^[a-zA-Z0-9]{19}$')]):
    root: constr(pattern=r'^[a-zA-Z0-9]{19}$')


class EndpointStatus(Enum):
    Pending = 'Pending'
    Available = 'Available'
    Deleting = 'Deleting'
    Create_Failed = 'Create_Failed'
    Delete_Failed = 'Delete_Failed'


class ErrorCode(RootModel[str]):
    root: str


class InternalServerException(RootModel[Any]):
    root: Any


class ListEndpointsRequest(BaseModel):
    pass


class ListOutpostsWithS3Request(BaseModel):
    pass


class ListSharedEndpointsRequest(BaseModel):
    pass


class MaxResults(RootModel[conint(ge=0, le=100)]):
    root: conint(ge=0, le=100)


class Message(RootModel[str]):
    root: str


class NetworkInterfaceId(RootModel[str]):
    root: str


class NextToken(
    RootModel[
        constr(pattern=r'^[A-Za-z0-9\+\:\/\=\?\#-_]+$', min_length=1, max_length=1024)
    ]
):
    root: constr(pattern=r'^[A-Za-z0-9\+\:\/\=\?\#-_]+$', min_length=1, max_length=1024)


class OutpostArn(
    RootModel[
        constr(
            pattern=r'^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):outposts:[a-z\-0-9]*:[0-9]{12}:outpost/(op-[a-f0-9]{17}|ec2)$'
        )
    ]
):
    root: constr(
        pattern=r'^arn:(aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b):outposts:[a-z\-0-9]*:[0-9]{12}:outpost/(op-[a-f0-9]{17}|ec2)$'
    )


class OutpostId(RootModel[constr(pattern=r'^(op-[a-f0-9]{17}|\d{12}|ec2)$')]):
    root: constr(pattern=r'^(op-[a-f0-9]{17}|\d{12}|ec2)$')


class OutpostOfflineException(RootModel[Any]):
    root: Any


class ResourceNotFoundException(RootModel[Any]):
    root: Any


class SecurityGroupId(RootModel[constr(pattern=r'^sg-([0-9a-f]{8}|[0-9a-f]{17})$')]):
    root: constr(pattern=r'^sg-([0-9a-f]{8}|[0-9a-f]{17})$')


class SubnetId(RootModel[constr(pattern=r'^subnet-([0-9a-f]{8}|[0-9a-f]{17})$')]):
    root: constr(pattern=r'^subnet-([0-9a-f]{8}|[0-9a-f]{17})$')


class ThrottlingException(RootModel[Any]):
    root: Any


class ValidationException(RootModel[Any]):
    root: Any


class VpcId(RootModel[str]):
    root: str


class AccessType(Enum):
    Private = 'Private'
    CustomerOwnedIp = 'CustomerOwnedIp'


class S3OutpostsCreateEndpointPostRequest(BaseModel):
    AccessType_1: Optional[AccessType] = Field(
        None,
        alias='AccessType',
        description='<p>The type of access for the network connectivity for the Amazon S3 on Outposts endpoint. To use the Amazon Web Services VPC, choose <code>Private</code>. To use the endpoint with an on-premises network, choose <code>CustomerOwnedIp</code>. If you choose <code>CustomerOwnedIp</code>, you must also provide the customer-owned IP address pool (CoIP pool).</p> <note> <p> <code>Private</code> is the default access type value.</p> </note>',
    )
    CustomerOwnedIpv4Pool: Optional[
        constr(pattern=r'^ipv4pool-coip-([0-9a-f]{17})$')
    ] = Field(
        None,
        description='The ID of the customer-owned IPv4 address pool (CoIP pool) for the endpoint. IP addresses are allocated from this pool for the endpoint.',
    )
    OutpostId: constr(pattern=r'^(op-[a-f0-9]{17}|\d{12}|ec2)$') = Field(
        ..., description='The ID of the Outposts. '
    )
    SecurityGroupId: constr(pattern=r'^sg-([0-9a-f]{8}|[0-9a-f]{17})$') = Field(
        ..., description='The ID of the security group to use with the endpoint.'
    )
    SubnetId: constr(pattern=r'^subnet-([0-9a-f]{8}|[0-9a-f]{17})$') = Field(
        ...,
        description='The ID of the subnet in the selected VPC. The endpoint subnet must belong to the Outpost that has Amazon S3 on Outposts provisioned.',
    )


class CreateEndpointRequest(BaseModel):
    AccessType: Optional[EndpointAccessType] = None
    CustomerOwnedIpv4Pool_1: Optional[CustomerOwnedIpv4Pool] = Field(
        None, alias='CustomerOwnedIpv4Pool'
    )
    OutpostId_1: OutpostId = Field(..., alias='OutpostId')
    SecurityGroupId_1: SecurityGroupId = Field(..., alias='SecurityGroupId')
    SubnetId_1: SubnetId = Field(..., alias='SubnetId')


class CreateEndpointResult(BaseModel):
    EndpointArn_1: Optional[EndpointArn] = Field(None, alias='EndpointArn')


class FailedReason(BaseModel):
    ErrorCode_1: Optional[ErrorCode] = Field(None, alias='ErrorCode')
    Message_1: Optional[Message] = Field(None, alias='Message')


class NetworkInterface(BaseModel):
    NetworkInterfaceId_1: Optional[NetworkInterfaceId] = Field(
        None, alias='NetworkInterfaceId'
    )


class NetworkInterfaces(RootModel[List[NetworkInterface]]):
    root: List[NetworkInterface]


class Outpost(BaseModel):
    CapacityInBytes_1: Optional[CapacityInBytes] = Field(None, alias='CapacityInBytes')
    OutpostArn_1: Optional[OutpostArn] = Field(None, alias='OutpostArn')
    OutpostId_1: Optional[OutpostId] = Field(None, alias='OutpostId')
    OwnerId: Optional[AwsAccountId] = None


class Outposts(RootModel[List[Outpost]]):
    root: List[Outpost]


class Endpoint(BaseModel):
    AccessType: Optional[EndpointAccessType] = None
    CidrBlock_1: Optional[CidrBlock] = Field(None, alias='CidrBlock')
    CreationTime_1: Optional[CreationTime] = Field(None, alias='CreationTime')
    CustomerOwnedIpv4Pool_1: Optional[CustomerOwnedIpv4Pool] = Field(
        None, alias='CustomerOwnedIpv4Pool'
    )
    EndpointArn_1: Optional[EndpointArn] = Field(None, alias='EndpointArn')
    FailedReason_1: Optional[FailedReason] = Field(None, alias='FailedReason')
    NetworkInterfaces_1: Optional[NetworkInterfaces] = Field(
        None, alias='NetworkInterfaces'
    )
    OutpostsId: Optional[OutpostId] = None
    SecurityGroupId_1: Optional[SecurityGroupId] = Field(None, alias='SecurityGroupId')
    Status: Optional[EndpointStatus] = None
    SubnetId_1: Optional[SubnetId] = Field(None, alias='SubnetId')
    VpcId_1: Optional[VpcId] = Field(None, alias='VpcId')


class Endpoints(RootModel[List[Endpoint]]):
    root: List[Endpoint]


class ListEndpointsResult(BaseModel):
    Endpoints_1: Optional[Endpoints] = Field(None, alias='Endpoints')
    NextToken_1: Optional[NextToken] = Field(None, alias='NextToken')


class ListOutpostsWithS3Result(BaseModel):
    NextToken_1: Optional[NextToken] = Field(None, alias='NextToken')
    Outposts_1: Optional[Outposts] = Field(None, alias='Outposts')


class ListSharedEndpointsResult(BaseModel):
    Endpoints_1: Optional[Endpoints] = Field(None, alias='Endpoints')
    NextToken_1: Optional[NextToken] = Field(None, alias='NextToken')
