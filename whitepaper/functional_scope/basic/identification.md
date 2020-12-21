[Index](../../readme.md) /
[Functional Scope](../readme.md) /
[Basic](./readme.md)

# Identification

## How to find the MachineToolIdentificationType when browsing from BaseObjectType

FolderType/FunctionalGroupType/MachineIdentificationType/MachineToolIdentificationType

 

Why is that so?

The DI specification (OPC UA Part 100) provides the FunctionalGroupType. This type is appropriate for the MachineIdentificationType of the Machinery specification, because it groups information content of a piece of machinery in one specific domain - Identification. See also [https://reference.opcfoundation.org/v104/DI/v102/ObjectTypes/FunctionalGroupType/](https://reference.opcfoundation.org/v104/DI/v102/ObjectTypes/FunctionalGroupType/).

The UA4MT Spec uses this MachineIdentificationType for greater interoperability with other types of machinery and adds the SoftwareIdentification to it. Thus, UA4MT specifies the MachineToolIdentificationiType.

 
## Usage of the DefaultInstanceBrowseName in the MachineToolIdentificationType

The DefaultInstanceBrowseName is intended to define the BrowseName of the Identification node to be “Identification” in the namespace of the OPC UA Part 100 specification.

It should not appear in the instances of the MachineToolIdentificationType.
