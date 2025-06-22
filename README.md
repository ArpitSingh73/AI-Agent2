# AI-Agent2

# Mini Agent-Based Data Fixing System

This repository implements a modular, agent-based system that automatically cleans and enriches messy CSV datasets containing customer records.

## What This System Does

The system simulates an agentic workflow where each "agent" performs a specific task in the data processing pipeline. Agents work sequentially but are modular enough to function independently.

### 1. Detection Agent
- Scans the dataset to identify:
  - Missing or malformed fields (e.g., invalid or empty email addresses)
  - Duplicate records
  - Incorrect or inconsistent data values

### 2. Correction Agent
- Fixes the issues identified by the Detection Agent:
  - Standardizes inconsistent values (e.g., name casing, date formats)
  - Removes duplicates
  - Corrects country names using fuzzy matching against a predefined list of valid countries

### 3. Enrichment Agent
- Enhances the dataset by:
  - Filling in missing values
  - Adding new, relevant attributes inferred from existing data

### 4. (Optional) UI Agent
- Provides a user-friendly interface to:
  - Upload a CSV file
  - View the cleaned and enriched data
  - Download the final dataset and logs

Each agent logs its actions (e.g., what was detected, corrected, or added), enabling transparency and traceability in the cleaning process.

## Repository Contents
- Source code for each agent
- Sample input CSV file (30–50 messy rows)
- Output cleaned CSV file
- Agent logs (CSV or TXT format)
