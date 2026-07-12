# Architecture Diagram

```text
+-------------------+
|       User        |
+---------+---------+
          |
          v
+-------------------+
|  React Frontend   |
|  Vite + Router    |
+---------+---------+
          |
          | REST API
          v
+-------------------+
| FastAPI Backend   |
+---------+---------+
          |
  +-------+-------------------+
  |                           |
  v                           v
+-------------------+   +------------------+
| Image Processing  |   | RAG Query Engine |
| PIL + Torchvision |   | FAISS Search     |
+---------+---------+   +---------+--------+
          |                       |
          v                       v
+-------------------+   +------------------+
| CNN Model         |   | Knowledge Base   |
| MobileNetV3 Large |   | PDFs + Text      |
+---------+---------+   +---------+--------+
          |                       |
          +----------+------------+
                     v
             +---------------+
             | Gemini AI API |
             +-------+-------+
                     |
                     v
             +---------------+
             | UI Cards      |
             | Recommendations |
             +---------------+
```
