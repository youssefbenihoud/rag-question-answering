# RAG-Based Question Answering System

Dieses Projekt demonstriert eine einfache Implementierung einer Retrieval-Augmented Generation (RAG) Pipeline für Frage-Antwort-Systeme.

## Inhaltsverzeichnis
- [Projektbeschreibung](#projektbeschreibung)
- [Installation](#installation)
- [Verwendung](#verwendung)
- [Beispiele](#beispiele)

## Projektbeschreibung
Die Pipeline verwendet ein vortrainiertes RAG-Modell (`facebook/rag-sequence-nq`) von Hugging Face, um Fragen basierend auf einem Korpus zu beantworten. Das Modell kombiniert Retrieval und Generierung, um präzise Antworten zu liefern.

## Installation
1. Klonen Sie das Repository:
   ```bash
   git clone https://github.com/DEIN_USERNAME/rag-question-answering.git
   cd rag-question-answering

2. Installieren Sie die benötigten Bibliotheken:
    ```bash
    pip install -r requirements.txt

## Verwendung
Führen Sie das Skript aus, um die Pipeline zu testen:
    ```bash
    python src/rag_pipeline.py

## Beispiele
Frage: "What is the capital of France?"
Antwort: "The capital of France is Paris."