class Solution:
    def defangIPaddr(self, address: str) -> str:
    """
    defangIPaddr takes in address str (IPv4 address) and replaces the "." with "[.]"
    address str (is a valid IPv4 address)
    """
        address_new = address.replace('.','[.]')
        return address_new
