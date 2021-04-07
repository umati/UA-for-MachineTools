[Index](../readme.md) /
[Signals Usage](./readme.md)

# ConditionClassTypes

The ConditionClasses described in OPC UA for Machine Tools in section 10 are used to further describe an event derived from the ConditionType (e.g. the [AlertType](https://reference.opcfoundation.org/v104/MachineTool/v100/docs/9.1/)).
They are abstract, so they are never instantiated.
Neither are they used like an event themselves.
They provide possible values for the ConditionClassId (and ConditionClassName) Properties of the [ConditionType](https://reference.opcfoundation.org/v104/Core/ObjectTypes/ConditionType/).

So, when implementing a ConditionType, the ConditionClassId is filled with the NodeId of a ConditionClassType.
Possible ConditionClassTypes are defined in [Part 9, Sec. 5.9](https://reference.opcfoundation.org/v104/Core/docs/Part9/5.9.1/) and in OPC UA for Machine Tools, Sec. 10.
