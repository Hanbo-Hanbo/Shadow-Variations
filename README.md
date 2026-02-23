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
The project utilizes two methods to validate real-time camera interactions and train the recognition engine:

- __Google Teachable Machine__: A web-based platform utilized for rapid prototyping and validating real-time camera interactions.
- __CNN Built with Keras Sequential API__: By implementing three convolutional layers, the model achieves hierarchical feature extraction from basic edges to complex silhouettes.
- __Spatial Robustness__: The integration of pooling layers ensures spatial robustness, allowing for accurate recognition despite positional shifts.
- __Classification Logic__: Finally, the visual signals are converted into a probability distribution via the Softmax function, ensuring a rigorous and scientific classification.

$$P(y=i | x) = \frac{e^{z_i}}{\sum_{j=1}^{3} e^{z_j}}$$

---

### 4. Creative Applications
The project explores three speculative approaches for AI application:

- __Approach 1: Creative Interactive System__: An interactive educational theater that utilizes real-time AI to transform traditional hand shadows into a multi-sensory experience. When the model Softmax confidence exceeds a 0.8 threshold, the silhouette comes to life with audio-visual feedback.
- __Approach 2: Critical Social Experiment__: While humans embrace ambiguity, the CNN is mathematically forced by its Softmax architecture to assign 100 percent probability across predefined classes. This critiques the reductive nature of AI, which simplifies complex realities into forced certainties.
- __Approach 3: Healthcare Speculation__: This proposal utilizes hand shadow edge-blur to derive an objective Stability Index to quantify fine motor skills. It offers a non-invasive solution for early screening of motor disorders like Parkinson's disease by processing abstract silhouettes to preserve privacy.

---

### 5. Project Structure
The repository is organized as follows:

- __shadow/__: Directory containing the raw source images for the categories.
- __Dataset_Final.zip__: A compressed archive of the finalized and partitioned dataset.
- __Shadow Variations.pdf__: The comprehensive project report detailing the research findings.
- __shadow.ipynb__: The Jupyter Notebook used for model development and training.
- __shadow.py__: The Python source script containing the model architecture.
- __Model_link.txt__: A text file containing external links for the trained model.
- __test.jpg / test2.jpg / test3.jpg__: Sample images used for inference testing.
- __README.md__: Project documentation.

---

### 6. Authors & Acknowledgements
- __Authors__: Hanbo Zhan, Ethan Zhang.
- __Acknowledgements__: Powered by Python, TensorFlow/Keras, and Google Teachable Machine. Special thanks to DMLAP instructors for their guidance.