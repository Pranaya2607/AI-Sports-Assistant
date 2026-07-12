# Presentation Content

## Abstract

This project presents an AI-Based Sports Equipment Recognition and Recommendation System using CNN and Generative AI. The system detects sports equipment from uploaded images using a MobileNetV3 Large convolutional neural network. After detection, the equipment name is used to retrieve relevant knowledge from a FAISS vector database. Google Gemini AI then generates intelligent explanations, maintenance tips, size guidance, accessories, safety recommendations, fake-product warning signs, and answers to user questions. The project combines computer vision, full-stack development, retrieval-augmented generation, and generative AI into one practical engineering application.

## Introduction

Sports equipment selection and maintenance are important for player performance, safety, and durability. Many beginners do not know the correct size, material, accessories, or care method for equipment. This project solves that problem by allowing users to upload an equipment image and receive detailed AI-powered guidance.

## Problem Statement

Users often struggle to identify equipment correctly, choose the right size, maintain it properly, and detect fake products. Normal search engines give scattered information. The proposed system provides a single AI platform for recognition and recommendation.

## Objectives

- Detect sports equipment using CNN.
- Recommend accessories and size guidance.
- Provide maintenance and safety information.
- Support fake equipment risk analysis.
- Build a RAG-powered AI assistant using FAISS and Gemini.
- Create a professional web application with React and FastAPI.

## Architecture

The user uploads an equipment image through the React frontend. FastAPI receives the image and preprocesses it. The CNN predicts the equipment class and confidence. The detected equipment is passed to the RAG system. FAISS retrieves relevant knowledge base chunks. Gemini AI uses those chunks to generate useful recommendations, which are displayed as frontend cards.

## Methodology

The CNN model is trained using transfer learning. MobileNetV3 Large is loaded with pretrained ImageNet weights. The final classifier layer is replaced with a 15-class output layer for sports equipment. The training pipeline uses data augmentation, validation, test evaluation, and model saving. For RAG, PDFs and text files are chunked, embedded using Sentence Transformers, stored in FAISS, and retrieved based on user queries. Gemini AI produces final explanations using retrieved context.

## Modules

1. Equipment Detection Module
2. Equipment Details Module
3. Accessories Recommendation Module
4. Size Recommendation Module
5. Maintenance Guide Module
6. Equipment Condition Checker
7. Fake Equipment Detector
8. AI Equipment Assistant
9. Dashboard and About Pages

## Technology Stack

Frontend: React, Vite, React Router, CSS  
Backend: FastAPI  
Deep Learning: PyTorch, Torchvision  
CNN: MobileNetV3 Large  
Generative AI: Google Gemini API  
RAG: FAISS and Sentence Transformers  
Knowledge Base: PDFs and markdown files

## Expected Results

The trained system should classify equipment into one of 15 classes and return confidence values. The recommendation modules should generate accurate and useful equipment-related advice based on the local knowledge base and Gemini AI.

## Advantages

- Detects equipment, not just sports categories.
- Combines CNN and Generative AI.
- RAG reduces generic responses by grounding answers in a knowledge base.
- Useful for students, players, coaches, and buyers.
- Modular and expandable architecture.

## Limitations

- Real prediction accuracy depends on dataset quality.
- Gemini requires an API key and internet connection.
- Fake detection is advisory and not a legal authentication result.
- The system currently classifies one main equipment item per image.

## Future Scope

Future versions can add webcam detection, YOLO-based multiple object detection, brand recognition, OCR serial verification, mobile app support, and real-time store price comparison.

## Conclusion

The project successfully integrates computer vision, RAG, generative AI, and full-stack development to create a useful sports equipment assistant. It is suitable as a final year engineering project because it demonstrates practical AI application development, model training, backend API design, and modern frontend design.
