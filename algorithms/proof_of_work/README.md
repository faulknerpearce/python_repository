# Simple Proof of Work Demonstration

## Overview

This Python script demonstrates a simple implementation of the Proof of Work (PoW) algorithm, often used in blockchain technology. The script includes a basic transaction list and a function to find a hash with a required number of leading zeros, simulating a fundamental aspect of blockchain mining processes.

## Features

- **Transaction Simulation**: Includes a basic structure for simulating transactions between parties.
- **Proof of Work Algorithm**: Implements a simple Proof of Work mechanism to find a hash with a specific number of leading zeros.
- **Customizable Difficulty**: Allows setting the difficulty level by specifying the number of leading zeros required in the hash.

## Function Description

`proof_of_work(transactions, difficulty)`

- Finds a hash of the transactions that has the specified number of leading zeros.
- Parameters:
  - `transactions`: A list of transaction dictionaries.
  - `difficulty`: The number of leading zeros required in the hash.
- Returns a string representing the hash that satisfies the Proof of Work condition.

## Setup and Usage

1. **Setup:**
   - Ensure Python is installed on your system.
   - The script uses the `hashlib` library, which should be included in standard Python installations.

2. **Running the Script:**
   - Define a list of transactions. Each transaction is a dictionary with `amount`, `sender`, and `receiver` keys.
   - Call the `proof_of_work` function with the list of transactions and the desired difficulty level.
   - Run the script to obtain the hash that satisfies the specified Proof of Work condition.