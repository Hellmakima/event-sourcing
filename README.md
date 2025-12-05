# Event Driven Architecture

**Based on [this](https://www.youtube.com/watch?v=t-LC1dWLpNs) video.**

## Event Sourcing

General idea: instead of storing the state of the system in a single place, we store the events that happened in the system. This allows us to easily replay the events to get the current state of the system. This is also useful for restoring previous states of the system.