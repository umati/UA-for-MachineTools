[Index](../../../readme.md) /
[Functional Scope](../../readme.md) /
[Basic](../readme.md)

# Tools

## Tool Location

The intention behind the Tools list in the Equipment component of the MachineToolType is to show all exchangeable tools the machine tool control has access to. Most often this will be the tool magazine and the spindle. Other cases may be multiple magazines, tool storage options within the machine tool that are not referred to as “magazine” and the like.

Where a tool is located can be shown using the Location component of the BaseToolType. This component is available for both the ToolType and the MultiToolType due to inheritance.

To differentiate between a magazine and a tool spindle, either a special PlaceNumber or a dedicated location Name may be used.

~~~
e.g. Location
     |___Name = Magazine_Rear
     |___PlaceNumber = 9999

or Location
     |___Name = Spindle_1
     |___PlaceNumber = 1
~~~

For the individual tools within a multitool, it is advised against using the Location component. The location is already indicated for the multitool.


## Potential use for Tools and Tool location: represent changeable machining heads

Q: What would be a good option to represent spindle units/machining heads in the UA4MT Companion Specification? It is possible, that multiple such spindle units are used in a machine tool. They have their own changer system, are located in a separate magazine and can be changed like a tool.

A: Potential use cases for the spindle units are
* information which spindle unit is currently used
* information about the run time of the individual spindle units
* providing e.g. information about the number of change cycles
1.    List the spindles as tools in a different magazine and provide only one spindle for monitoring
    If there is only one spindle with different settings configured at the machine, this could be an straight forward solution.
    It would be possible to represent the usage statistics of the spindle with the ToolLife (e.g. Time and Usage). The information about the currently used SpindleUnit could be provided by the name. If there are multiple spindles configured at the machine it could be a solution to map the currently used spindle to the SpindleMonitoringType
    Pro:
    No OEM extension which might conflict with a future extension of the companion spec.
    At least the information above can be provided
    Con:
    Using the tool types in a not intended way
2.    Add the spindles as SpindleMonitoringType
    Pro:
    so far no pro arguments here
    Con:
    OEM extension necessary to provide the defined information.
    Additional information necessary which is the currently used SpindleUnit
    May lead to confusion because the Client has to monitor which spindle is used
3.    Add a spindleUnitListType and a SpindelUnitType as OEM extension
    Pro:
    clear solution
    Possibility to define all needed features
    Could be possible to define a best practice standard
    Con:
    Specification must be done by the OEM
    Will lead to conflicts with other manufactures
    Might lead to conflicts with future extensions of the companion standard
