# Common Viva Questions and Detailed Answers

## 1. What is the main objective of your project?

The objective is to build an AI system that recognizes sports equipment from images using a CNN and then provides intelligent recommendations using Gemini AI and RAG. It helps users understand equipment details, accessories, size selection, maintenance, condition, and fake-product warning signs.

## 2. Does your model classify sports or equipment?

It classifies sports equipment only. The classes include cricket bat, football, basketball, tennis racket, badminton racket, shuttlecock, hockey stick, helmet, sports shoes, and other equipment. It does not classify sports activities.

## 3. Why did you use MobileNetV3 Large?

MobileNetV3 Large is efficient and accurate for image classification. It is suitable for transfer learning because it has already learned useful visual features from large image datasets. It gives a good balance between performance and computational cost.

## 4. What is transfer learning?

Transfer learning means using a model pretrained on a large dataset and adapting it to a new task. In this project, MobileNetV3 Large is loaded with pretrained weights, and the final classification layer is replaced with a 15-class layer for sports equipment recognition.

## 5. What preprocessing is applied to images?

Images are resized to 224×224 pixels, converted to tensors, and normalized using ImageNet mean and standard deviation. During training, augmentation such as rotation, flipping, color jitter, and affine transformation is applied.

## 6. What is RAG?

RAG stands for Retrieval-Augmented Generation. It first retrieves relevant information from a knowledge base and then sends that information to a generative AI model. This helps the AI answer using project-specific context instead of only generic knowledge.

## 7. Why did you use FAISS?

FAISS is used for efficient vector similarity search. It stores embeddings of knowledge base chunks and quickly retrieves the most relevant chunks for a user query or detected equipment.

## 8. What are Sentence Transformers used for?

Sentence Transformers convert text chunks and user queries into numerical embeddings. Similar meanings produce similar vectors, which allows FAISS to retrieve relevant information.

## 9. How does Gemini AI help?

Gemini AI generates human-readable explanations, maintenance tips, buying guides, safety advice, size recommendations, and answers to user questions. It uses retrieved RAG context to improve relevance.

## 10. What are the main backend routes?

The backend provides `/predict`, `/equipment-info`, `/recommend-accessories`, `/size-guide`, `/maintenance`, `/condition`, `/fake-detection`, `/ask-ai`, and `/rag-search`.

## 11. What happens if the model file is not trained yet?

The backend returns a clear message saying `sports_model.pth` is not available and asks the user to train the model using `backend/cnn/train.py`. This prevents false predictions.

## 12. What loss function is used?

CrossEntropyLoss is used because this is a multi-class classification problem with 15 possible equipment classes.

## 13. What optimizer is used?

AdamW is used because it is effective for deep learning and includes weight decay, which helps reduce overfitting.

## 14. How do you evaluate the model?

The model is evaluated using validation accuracy during training and final test metrics such as classification report and confusion matrix.

## 15. What is the advantage of this project?

The project combines image recognition and generative AI in one practical application. It provides not only prediction but also recommendations, maintenance guidance, and an AI assistant.

## 16. What are the limitations?

The accuracy depends on dataset quality. The model needs enough images per class. Gemini requires an API key. Fake detection is only advisory and cannot legally verify authenticity.

## 17. How can this project be improved?

It can be improved by adding YOLO object detection, real-time camera support, damage segmentation, brand recognition, OCR-based serial number verification, and mobile app support.

## 18. Why did you choose FastAPI?

FastAPI is fast, modern, easy to integrate with Python ML models, and automatically provides Swagger API documentation.

## 19. Why did you choose React?

React helps build a responsive and modular frontend. Components can be reused across pages such as detection, details, accessories, and AI assistant.

## 20. Is fake equipment detection fully accurate?

No. It provides a risk analysis based on visible observations, price, seller type, and known warning signs. Final authentication should be done through authorized dealers or official brand verification.
