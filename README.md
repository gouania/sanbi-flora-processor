# SANBI Flora Processor 

This repository contains a Python pipeline designed to make the **SANBI e-Flora of South Africa** interactive using Large Language Models (LLMs). 

## 📖 The Problem
The SANBI e-Flora is a massive dataset (25M+ tokens). Standard LLM interfaces cannot process a file of this size in a single prompt. Furthermore, the data is stored in a structured Darwin Core Archive (DwC-A) where species names and morphological descriptions are kept in separate files, linked only by IDs.

## 🛠 The Solution
This script performs three critical tasks:
1. **Relational Merge:** It joins the `taxon.txt` (names) and `description.txt` (data) files from the DwC-A.
2. **Multilingual Labeling:** It preserves and labels descriptions in English, Latin, and German.
3. **Optimized Chunking:** It splits the merged data into "Notebook-ready" text files that stay under the 500,000-word limit required by interfaces like NotebookLM.

## 🚀 Interactive Flora
Using this processed data, I have created a grounded "Source of Truth" interface. You can use it to generate bespoke dichotomous keys, compare species morphology, and query habitat data.

> [!IMPORTANT]
> **Access the Interactive Flora here:** [Interactive SANBI e-Flora (NotebookLM)](https://notebooklm.google.com/notebook/d37c2db7-8bdb-4a73-94d7-f08e263a8bcf)  
> *(Requires Google Login. Set to Viewer Mode.)*

## ⚖️ Data & Licensing
- **Data Source:** [SANBI e-Flora of South Africa](https://ipt.sanbi.org.za/resource?r=flora_descriptions&v=1.36).
- **License:** This project leverages open-access biodiversity data shared under CC BY 4.0.
- **Disclaimer:** AI-generated keys are experimental. Always verify against the primary descriptions provided in the citations.

## 👤 Author
**Daniel Cahen, PhD**  
Botanist at the Royal Botanic Gardens, Kew.
