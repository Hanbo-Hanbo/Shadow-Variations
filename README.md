# Shadow Variations
## A Multi-Dimensional AI Exploration of Hand Shadow Datasets

### 1. Introduction
Shadow Variations is a multi-dimensional project that transcends the boundaries of art, sociology, and medicine by utilizing hand shadows as an abstract medium. The project showcases the technical potential of Convolutional Neural Networks (CNNs) in feature extraction while reflecting the speculative value of computational arts in addressing real-world issues, such as privacy-preserving healthcare monitoring.

---

### 2. Dataset Overview
This dataset is a collection of hand shadow images featuring three distinct categories: Bird, Dog, and Snake. 

- __Sourcing__: All materials were sourced from original, self-captured photography.
- __Diversity__: Gestures were recorded under controlled single-source lighting, encompassing diverse hand sizes and projection angles.
- __Specifications__: Images were unified, grayscaled, and resized to 128 x 128 pixels as tensors for optimal feature extraction.
- __Automation__: A custom Python automation script was implemented to organize the repository into a professional Dataset_Final directory architecture.
- __Partitioning__: The data is physically partitioned into a 70% Training, 20% Validation, and 10% Testing split to ensure an unbiased evaluation environment.

---

### 3. Methodology Summary
I utilized two distinct methods to validate real-time camera interactions and train the recognition engine:

- __Method 1: Custom CNN (Keras Sequential API)__: By implementing three convolutional layers, I achieved hierarchical feature extraction from basic edges to complex silhouettes. The integration of pooling layers ensures spatial robustness.
- __Method 2: Google Teachable Machine__: A web-based platform utilized for rapid prototyping. This method provides an alternative model optimized for real-time camera interaction and quick validation.
- __Classification Logic__: For both methods, the visual signals are processed to output a probability distribution via the Softmax function, ensuring a rigorous and scientific classification.

$$P(y=i | x) = \frac{e^{z_i}}{\sum_{j=1}^{3} e^{z_j}}$$

---

### 4. Creative Applications
The project explores three speculative approaches for AI application:

- __Approach 1: Creative Interactive System__: An interactive educational theater that utilizes real-time AI to transform traditional hand shadows into a multi-sensory experience. When the model confidence exceeds a 0.8 threshold, the silhouette comes to life.
- __Approach 2: Critical Social Experiment__: While humans embrace ambiguity, the CNN is mathematically forced by its Softmax architecture to assign 100 percent probability. This critiques how AI simplifies complex realities into forced certainties.
- __Approach 3: Healthcare Speculation__: This proposal utilizes hand shadow edge-blur to derive an objective Stability Index to quantify fine motor skills. It offers a non-invasive solution for early screening of motor disorders like Parkinson's disease.

---

### 5. Project Structure
The repository is organized with the following files and directories:

- __shadow/__: Directory containing the raw source images for the categories and the split_data.py file that completes the classification data.
- __Method 2/__: Directory containing the model files generated via Google Teachable Machine for real-time validation.
- __Dataset_Final.zip__: Dataset.
- __Shadow Variations.pdf__: The comprehensive project report detailing the research findings.
- __shadow.ipynb__: The primary Jupyter Notebook used for model development and training.
- __shadow.py__: The Python source script containing the model architecture and core logic.
- __Model_link.txt__: A text file containing external links or credentials for the trained model weights.
- __test.jpg / test2.jpg / test3.jpg__: Independent sample images used for conducting inference tests.
- __README.md__: Documentation and project guide.

---

### 6. Authors & Acknowledgements
- __Authors__: Hanbo Zhan, Ethan Zhang.
- __Acknowledgements__: Powered by Python, TensorFlow/Keras, and Google Teachable Machine. Special thanks to DMLAP instructors for their guidance.