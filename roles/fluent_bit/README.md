# FluentBit

FluentBit is the little brother or sister of Fluentd. It is optimized for a very low footprint of only a few megabytes.
It is written `C` only and therefore platform independent.
It runs on everything from your Arduino, Raspberry Pi, switches, firewalls, server over virtual machines up to containers.

It is truly universal as it has inputs for files as well as http, it can forward logs and metrics to a lot of destinations.

This versatility is interesting to me, personally, because I play with all of those things in private and at work.

In this project we focus on OpenSearch and Elasticsearch and send metrics as well as logs.

As with any other role provided, we try to focus on universality for configuration. However, if you wanna configure your
ingest filters or processors here, you are on the wrong place.

It is better to provide such grade of customization in a package or another role.
