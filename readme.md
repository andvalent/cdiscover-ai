# CDiscover-AI: A Context-Aware Classical Music Discovery Engine

**A sophisticated, end-to-end RAG (Retrieval-Augmented Generation) system designed to provide nuanced, context-aware classical music recommendations by understanding the rich, descriptive text within thousands of expert-written CD liner notes.**

This project moves beyond shallow metadata (e.g., composer, title) to answer subjective user queries like *"Find me a recording of Baroque music that conveys a sense of grandeur and ceremonial dignity"* or *"Suggest some mysterious music for solo piano."*

## The Vision & Problem Statement

Standard classical music recommendation systems often fail because they rely on simple tags. They can find you *Beethoven's 5th Symphony*, but they can't answer *why* you should listen to a particular recording or what emotional journey it will take you on.

The real expertise lies in the thousands of pages of liner notes written by musicologists—an underutilized source of high-quality data. This project leverages this data to create a true "Discovery Engine" that understands not just *what* a piece of music is, but *what it feels like*.

The core technical goal was to build this system in a **cost-optimized** manner, using foundational AWS services and avoiding expensive, proprietary vector databases.

## Architecture & Technical Stack

This project is a complete, cloud-native application deployed on AWS and managed entirely with Infrastructure as Code (IaC) via Terraform. The architecture is a scalable, event-driven pipeline designed for data processing, vectorization, and serving a live API.

