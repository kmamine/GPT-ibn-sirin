# GPT-ibn-sirin
A ChatGPT App for dream interpretation based on ibn sisrin book "The interpretation of Dreams".

---
# Dream Interpreter Application Project Plan

## Overview

This project aims to create a dream interpretation application based on the Ibn Sirin method. The application will leverage modern AI technologies to provide users with personalized and insightful dream interpretations.

## Tech Stack

1. LLM: ChatGPT Agents
2. Backend: Flask, LangChain
3. RAG: SQLite-vector for knowledge base retrieval
4. Frontend: Streamlit

## User Story

**Input**: The user provides a detailed description of their dream.
**Information Extraction**: The AI agent extracts key details and themes from the dream description.
**Knowledge Base Query**: Relevant segments are retrieved from the Ibn Sirin knowledge base using RAG (SQLite-vector).
**Response Generation**: The agent formulates a response by combining retrieved information and insights.
**Refinement**: If required, the agent asks the user for additional life details to refine the interpretation.
**Output**: The final interpretation and explanations are presented to the user.

## Components and Workflow

- ### Frontend (Streamlit)
Simple and intuitive user interface for dream input and interpretation display.
Integration with the backend API for seamless interaction.

- ### Backend (Flask and LangChain)
**Flask**:
Handles API endpoints for communication between frontend and backend.
Manages user inputs and triggers the LangChain pipeline.

**LangChain**:
Orchestrates the LLM for information extraction and response generation.
Integrates with the SQLite-vector knowledge base for relevant segment retrieval.
- ### RAG System (SQLite-vector)
**Knowledge Base**:
Contains indexed dream interpretations and related content based on the Ibn Sirin method.
**Retrieval**:
Uses vector similarity to find relevant segments based on extracted dream themes.

- ### LLM (ChatGPT Agents)
Extracts key details from user input.
Generates coherent, insightful, and contextually accurate interpretations.
Dynamically adjusts responses by incorporating additional user-provided details.

---

# Project Milestones

## Phase 1: Planning and Setup
- Define the structure of the Ibn Sirin knowledge base.
- Set up development environment and tools.
- Prepare initial dataset for knowledge base.

## Phase 2: Backend Development
- Develop Flask API endpoints for communication.
- Integrate LangChain for orchestrating LLM and RAG components.

## Phase 3: Knowledge Base Construction
- Format and index Ibn Sirin dream interpretations in SQLite-vector.
- Test retrieval efficiency and accuracy.

## Phase 4: Frontend Development
- Design and implement the Streamlit user interface.
- Connect the frontend to backend APIs.

## Phase 5: Testing and Refinement
- Test the full pipeline with various dream inputs.
- Refine interpretations and ensure consistency.

## Phase 6: Deployment
- Deploy the application on a cloud platform (e.g., AWS, GCP, or Azure).
- Ensure scalability and performance under user load.

--- 
# Implementation Details

## Knowledge Base Structure

### Table Name: dream_knowledge_base

Columns:

+ **id**: Unique identifier
+ **text**: Dream interpretation text
+ **tags**: Relevant themes and keywords

### embedding: 
Vectorized representation for retrieval

### API Endpoints
#### POST /interpret-dream
+ Input: Dream description (JSON format)
+ Output: Dream interpretation and explanations

#### Streamlit Features

+ Input text box for dream description.
+ Display area for dream interpretation.
+ Option for the user to provide additional details if requested.

## Resources

Ibn Sirin Knowledge Base: Digitized and formatted dream interpretations.

Pre-trained Models: ChatGPT for NLP tasks.

Vector Embedding Model: OpenAI embeddings for indexing and retrieval.

Success Metrics

High relevance of retrieved interpretations.

User satisfaction based on feedback.

Efficient system performance with minimal latency.

Potential Challenges

Ensuring accurate and culturally sensitive interpretations.

Balancing simplicity and depth in the user interface.

Maintaining the quality of responses with diverse input scenarios.
