[Index](../readme.md) /
[Signals Usage](./readme.md)

# OPC UA VariableTypes

## NodeVersion (in combination with GeneralModelChangeEvent)

The NodeVersion Property is used by the UA4MT specification in all places where the address space might change during server runtime.

As defined by the OPC UA base specification ([https://reference.opcfoundation.org/v104/Core/docs/Part3/9.32.2/](https://reference.opcfoundation.org/v104/Core/docs/Part3/9.32.2/)), the NodeVersion and GeneralModelChangeEvent shall be used in conjunction to show such changes. If the address space does not change during server runtime, neither of both shall be used. An example may be a ProductionPlan node with a fixed number of jobs: the address space will never change and neither NodeVersion nor GeneralModelChangeEvent need to be used.

The NodeVersion also serves as an indication for a client, if changes in the address space are to be expected or not.

In order to ensure the NodeVersion changes with every change of the address space and never takes the same value twice, the UA4MT specification recomments using a string representation of the timestamp of the moment the node structure was changed. 

Never having the same value for NodeVersion twice ensures that a client will not falsely assume the address space to be unchanged. A scenario where this might happen is a server not using a timestamp for the NodeVersion, but e.g. an integer that is counted upwards (as string content). If a server is restarted, a client might read the NodeVersion containing the same value as before the restart, even though the address space need not be the same.
