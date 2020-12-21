[Index](../../readme.md) /
[Functional Scope](../readme.md) /
[Basic](./readme.md) /

# Monitoring

## CombinedChannelMonitoringType - Rules for Aggregation

| Component of the CombinedChannelMonitoringType | Rule for Aggregation |
|----|-----|
| ChannelState | Mode of the channel not in "active", otherwhise "active"<br><ul><li>if all channels active --> active</li><li>if >0 channel reset --> reset</li><li>else interrupted</li></ul>|
| ChannelMode> | If one or more channel of the combined channels is not in "automatic" the machine is not producing (except if the channel is not currently in use). If for example the operator is in JogManual and moving one axis, the whole machine is not producing in automatic and the combined channel can be viewed as in JogManual<br><br>Mode of the channel not in “automatic”, otherwhise “automatic” - On most multi spindle machines there is one hmi which controls the whole machine, so most of the input is applied to all combined channels |
| FeedOverride | On most multi spindle machines there is one hmi which controls the whole machine, so most of the input is applied to all combined channels<br><br>selection from hmi mirrored |
| RapidOverride | On most multi spindle machines there is one hmi which controls the whole machine, so most of the input is applied to all combined channels<br><br>selection from hmi mirrored |
| ProgramModifiers | If an element of ProgramModifiers is true in any channel, it has to be true in the combined channel |
