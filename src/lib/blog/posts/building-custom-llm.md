---
title: Building a Custom LLM
date: 2025-02-23
published: false
---

In an effort to understanding better how LLMs work I'm going to attempt to create a custom LLM running on my own
hardware.

If possible I'd like to run a 'self-hosted' LLM on a local machine or one I have control over and use a open source
base model trained on my specific dataset. My data should not be "shared" with whoever trained the original model
and once it has been trained I should be able to ask questions and get accurate responses based on the data provided
to the model.

### What is an LLM?
An LLM is a neural network trained to predict the next word in a sequence given an input context. To do so they use:
* **Tokenization** - Breaking text into numerical representations.
* **Transformer Architectures** - Consists of an encoder and decoder. The encoder reads and processes the input text.
The decoder generates coherent responses by predicting the next word in the sequence.
* **Self-supervised learning** - Use vast amounts of unstructured text data to do the supervised learning.
* **Fine-tuning** - Adapt the LLm to specific tasks like a chatbot or code generation.
#### Tokenization
#### Transformers
#### Self-Supervised Learning
#### Fine Tuning

### Core Functionality my LLM will have.

This LLM will take in minutes from meetings and then answer questions when asked about the meetings.


### How to Create your own LLM
