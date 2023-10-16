# Dragon Class

## Overview

The Dragon Class is a Python class that models dragons with various attributes, including name, kind, power, and health.
This script can be used to create and manage dragon characters in a fantasy-themed application or game.

## Features

- The class initializes dragons with attributes like name, kind, power, and health.
- Dragons can form tribes with other dragons of the same kind, increasing their tribe size.
- Dragons can increase or decrease their health points based on certain conditions.
- The class provides a user-friendly string representation of dragons, including their name, kind, and tribe size.

## Class Methods

 `__init__(self, name, kind, power, health)`

- Initializes a Dragon instance with the provided attributes: `name`, `kind`, `power`, and `health`.
- Also initializes an empty list, `tribe`, to store other dragons in the same tribe.

`__repr__(self)`

- Provides a string representation of the dragon.
- If the dragon is part of a tribe, it includes the tribe size.
- If not, it mentions that the dragon has not joined a tribe.

`join_tribe(self, other_dragon)`

- Allows a dragon to join a tribe with another dragon if they share the same kind.
- Adds both dragons to each other's tribe lists.
- Displays a message to confirm the tribe formation.

 `adjust_health(self, adjusted_health, damage)`

- Adjusts the dragon's health points.
- Decreases health points if `damage` is `True`, otherwise increases them.
- Displays a message indicating the change in health points.

## Usage

1. Create instances of the Dragon class with specific attributes (name, kind, power, and health).

2. Dragons can join tribes using the `join_tribe()` method. Dragons of the same kind can form tribes together.

3. You can adjust a dragon's health points using the `adjust_health()` method, specifying the amount and whether it's damage or healing.

