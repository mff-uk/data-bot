"""Linked Data Platform data model

Based on https://www.w3.org/TR/ldp/ specification. 
To get overview please read https://www.w3.org/TR/ldp-primer/ .
"""
from abc import ABC
from dataclasses import dataclass
from enum import Enum


class RdfContentReference(ABC):
    """Represent RDF content."""
    ...


class ContentReference(ABC):
    """Represent arbitrary content."""
    ...


@dataclass(kw_only=True)
class LdpResources:
    """All resources are assigned identifier once they are created in the LDP.

    Specified as https://www.w3.org/TR/ldp/#dfn-linked-data-platform-resource

    Attributes
    ----------
    iri:str
      Based on 4.2.1.5
    """
    iri: str


@dataclass
class LdpRdfSources(LdpResources):
    """Resource with RDF content.

    Specified as https://www.w3.org/TR/ldp/#dfn-linked-data-platform-rdf-source

    Attributes
    ----------
    content: RdfContentReference
      Resource content without generated statements.
    """
    content: RdfContentReference


@dataclass
class LdpNonRdfSources(LdpResources):
    """Resource with non-RDF content.

    Specified as https://www.w3.org/TR/ldp/#dfn-linked-data-platform-non-rdf-source

    Attributes
    ----------
    content: ContentReference
      Reference to the content of the source.
    """
    content: ContentReference


@dataclass
class LdpContainer(LdpRdfSources, ABC):
    """Container can contain other resources.

    There are two main concepts: membership and containment.
    The main difference is that containment bound existence of contained
    LdpResources to the existence of the LdpContainer.

    Specified as https://www.w3.org/TR/ldp/#dfn-linked-data-platform-container

    Attributes
    ----------
    contains: list[str]
      List of resources in this container.
    """
    contains: list[str]


@dataclass
class LdpBasicContainer(LdpContainer):
    """Makes no distinction between membership and containment. 

    Specified as https://www.w3.org/TR/ldp/#ldpbc
    """


class MembershipDirection(Enum):
    """Represent direction of member ship triple.

    Specified as https://www.w3.org/TR/ldp/#dfn-membership-triples
    """
    OwnerToMember = "owner-to-member"
    MemberToOwner = "member-to-owner"


@dataclass
class LdpDirectContainer(LdpContainer):
    """Allow to store membership.

    It internally store membership information in a same way as LdpContainer.
    But user can specify a predicate (hasMemberRelation) that is used to 
    represent the membership in another resource (membershipResource).
    The given resource is automatically updated when this container
    change. Multiple containers direct containers can be connected to 
    the same resource (membershipResource).

    Specified as https://www.w3.org/TR/ldp/#ldpdc

    Attributes
    ----------
    membershipResource: str
      Resource to which add the membership information.
      Based on 5.4.1.3 .
    memberRelation: str
      Membership predicate, may correspond to hasMemberRelation (5.4.1.4.1) or
       isMemberOfRelation (5.4.1.4.2) based on value of memberDirection.
    memberDirection: MembershipDirection
      Specify direction of membership.
    """
    membershipResource: str
    memberRelation: str
    memberDirection: MembershipDirection


@dataclass
class LdpIndirectContainer(LdpDirectContainer):
    """

    It behaves like LdpDirectContainer (5.5.1.1) and keep track of resources 
    in the same way. Yet when adding information to connected resource 
    (membershipResource)  it does not add the resource, but value specified by
    predicate (insertedContentRelation), when new resource is created. Thus it 
    allows to indirectly address the member resources.

    The root resource of newly posted content must contain statement
    with insertedContentRelation predicate.

    Specified as https://www.w3.org/TR/ldp/#ldpic

    Attributes
    ----------
    insertedContentRelation: str
      Predicate of the request whose object should be added to the resource.
      Based on 5.5.1.2 .
    """
    insertedContentRelation: str
