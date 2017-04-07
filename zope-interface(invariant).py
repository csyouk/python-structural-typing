from zope.interface import Interface, Attribute, implementer, invariant

def required_contact(obj):
    if not (obj.email or obj.phone):
        raise Exception("At least one info is required")


class IPerson(Interface):
    name = Attribute("name")
    email = Attribute("Email Address")
    phone = Attribute("Phone Number")

    invariant(required_contact)

@implementer(IPerson)
class DefaultPerson:
    name = "default"

@implementer(IPerson)
class FulfilledPerson:
    name = "nobody"
    email = "abc@gmail.com"
    phone = "000-000-0000"


def main():

    person1 = FulfilledPerson()
    IPerson.validateInvariants(person1)
    person2 = DefaultPerson()
    IPerson.validateInvariants(person2)

if __name__ == '__main__':
    main()