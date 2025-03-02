# FluentBit

FluentBit is the little brother or sister of Fluentd. It is optimized for a very low footprint of only a few megabytes.
It is written `C` only and therefore platform independent.
It runs on everything from your Arduino, Raspberry Pi, switches, firewalls, server over virtual machines up to containers.

It is truly universal as it has inputs for files as well as http, it can forward logs and metrics to a lot of destinations.

This versatility is interesting to me, personally, because I play with all of those things in private and at work.

## Inputs

Define your custom inputs using `fluentbit.inputs` array.
The list contains of dictionaries. We will not check if your config is correct within ansible.
Please refer to the (documentation)[https://docs.fluentbit.io/manual/pipeline/inputs]

## Outputs

Define your custom inputs using `fluentbit.outputs` array.
The list contains of dictionaries. We will not check if your config is correct within ansible.
Please refer to the (documentation)[https://docs.fluentbit.io/manual/pipeline/outputs

## Filters

Define your custom inputs using `fluentbit.filters` array.
The list contains of dictionaries. We will not check if your config is correct within ansible.
Please refer to the (documentation)[https://docs.fluentbit.io/manual/pipeline/filters

## Processors
Define your custom inputs using `fluentbit.processors` array.
The list contains of dictionaries. We will not check if your config is correct within ansible.
Please refer to the (documentation)[https://docs.fluentbit.io/manual/pipeline/processors
