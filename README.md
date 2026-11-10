# Project NOSE
### Neural Olfactory Sensing Engine

**An experimental hybrid olfaction system combining computational odor prediction, physical gas sensing, and language-model-assisted interpretation.**

## Overview

Project NOSE explores how computational models and physical sensing hardware can work together to investigate the sense of smell.

The project combines three complementary components:

1. **OpenPOM — Computational Olfaction:** Uses a graph neural network to predict human-perceived odor descriptors from molecular structures.
2. **Electronic Nose — Physical Sensing:** Uses gas-sensor hardware connected to a Raspberry Pi to collect environmental measurements.
3. **LLM-Assisted Intelligence:** Uses a language model to interpret structured observations, explain experimental results, and answer questions grounded in available data.

The objective is to develop an experimental system that connects molecular-level odor prediction with real-world chemical sensing.

## System Architecture

### 1. Computational Odor Prediction

OpenPOM is an open-source molecular odor prediction framework.

It takes molecular representations as input and predicts odor descriptors. It operates independently of the physical gas-sensing pipeline.

### 2. Physical Gas Sensing

A Raspberry Pi 3 will act as the hardware interface for an electronic nose prototype.

A candidate sensor is the Bosch BME688.

The sensor will collect environmental measurements and transmit structured readings to the primary application running on a Mac.

### 3. Intelligence and Interpretation

The Mac will host the primary application and intelligence layer.

It will:

- Receive sensor observations from the Raspberry Pi.
- Store and process experimental readings.
- Support sensor-data classification as labelled datasets become available.
- Integrate OpenPOM for molecular odor prediction.
- Connect to a language model for grounded question answering.
- Present observations and experimental results through an interactive interface.

## High-Level Architecture

```text
                  PROJECT NOSE
                       |
          +------------+------------+
          |                         |
   COMPUTATIONAL              PHYSICAL SENSING
     OLFACTION                       |
          |                    Raspberry Pi 3
       OpenPOM                        |
          |                      Gas Sensor
  Molecular Structures                 |
          |                         Wi-Fi
   Odor Predictions                    |
          |                            |
          +-------------+--------------+
                        |
                   Mac Application
                        |
              Data Processing Layer
                        |
             Sensor Classification
                        |
               Intelligence Layer
                        |
                  LLM Interface
                        |
                Interactive Q&A
```

## Development Environment

Primary development machine: MacBook Pro

Hardware interface: Raspberry Pi 3

Programming language: Python

Planned technologies:

- OpenPOM
- DeepChem and its required dependencies
- Raspberry Pi sensor interfaces
- FastAPI or an equivalent lightweight communication layer
- Data processing and machine learning tools
- An LLM integration
- Git and GitHub

Specific libraries and model providers will be selected and validated during development.

## Development Roadmap

| Milestone | Objective |
|---|---|
| 00 | Project definition, architecture and repository setup |
| 01 | Build the Mac-based application foundation using simulated sensor data |
| 02 | Explore and integrate OpenPOM for molecular odor prediction |
| 03 | Establish communication between the Raspberry Pi and Mac |
| 04 | Integrate the physical gas sensor and collect readings |
| 05 | Build a sensor-data classification and experimental analysis pipeline |
| 06 | Integrate an LLM for grounded question answering |
| 07 | Build the unified interface and evaluate the complete prototype |

## Research and Engineering Principles

- Separate molecular odor prediction from physical gas sensing.
- Never treat raw gas-sensor measurements as direct odor identities.
- Distinguish measured observations from model predictions and LLM-generated explanations.
- Preserve raw experimental data.
- Document sensor calibration, environmental conditions and limitations.
- Validate model outputs against actual experimental observations.
- Avoid claiming capabilities that have not been demonstrated.

## Current Status

**Stage:** Project setup and architecture definition.

The hardware integration, sensor-data collection, OpenPOM integration and LLM interface are planned development components. Their functionality will be documented as they are implemented and tested.

## Project Goal

To explore a practical computational and physical olfaction architecture that connects molecular odor prediction with real-world sensing and natural-language interaction.

---

*Project NOSE — Exploring the intersection of computational olfaction, physical AI and intelligent systems.*
