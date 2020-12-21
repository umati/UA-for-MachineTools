[Index](../../../readme.md) /
[Functional Scope](../../readme.md) /
[Basic](../readme.md)

# Production

## Relation of ActiveProgram and Programs in the ProductionPlan

* ActiveProgram is required to be always available in an UA4MT server. Using only the ActiveProgram is recommended for machine tools that don’t work with jobs.
* If Jobs are modeled beneath the ProductionPlan node, the ActiveProgram shall relate to the Job it is used in. This is done via both the JobIdentifier and JobNodeId variables. The JobNodeId is considered more useful for OPC UA clients, that want to browse to the job node. The JobIdentifier is considered more useful to humans, e.g. on a HMI or dashboard.
* When implementing an OPC UA server with jobs beneath the ProductionPlan node and programs within this job, it is important to have the same content in the ActiveProgram and the same program represented in the job. The same data is shown in both locations.


## Information given in CurrentState in the Production[XY]StateMachineType instances

* CurrentState is a LocalizedText with additional Properties, see [https://reference.opcfoundation.org/v104/Core/docs/Part5/B.4.6/](https://reference.opcfoundation.org/v104/Core/docs/Part5/B.4.6/). In the MachineTools specification the Properties Id and Number are required.
* The value of the LocalizedText shall be the name of the state in human readable form. As a LocalizedText, this value may be available for multiple locales. As an implementation suggestion, for the english locale the BrowseNames of the states may be used (Initializing, Running, Ended, Interrupted, Aborted).
* The Id property is of type NodeId. This property contains the NodeId of the state in the state machine definition. For Example, this is the NodeId of “Running” in the ProductionStateMachineTyp in the UA4MT Namespace.
* The Number property contains the number for the state as found in table 35 in the UA4MT specification.
* This makes the Id and Number properties two ways to express the same information. In part, this applies as well to the value of CurrentState, but due to it being a LocalizedText, this value is not strictly defined.
* The same principle of using the value, Id and Name applies to the CurrentState component of the state machines.
