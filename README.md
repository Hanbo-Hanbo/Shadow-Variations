# Shadow Variations
## A Multi-Dimensional AI Exploration of Hand Shadow Datasets

### 1. Introduction
[cite_start]Shadow Variations is a multi-dimensional project that transcends the boundaries of art, sociology, and medicine by utilizing hand shadows as an abstract medium[cite: 51, 52]. [cite_start]The project showcases the technical potential of Convolutional Neural Networks (CNNs) in feature extraction while reflecting the speculative value of computational arts in addressing real-world issues, such as privacy-preserving healthcare monitoring[cite: 52].

---

### 2. Dataset Overview
[cite_start]This dataset is a collection of hand shadow images featuring three distinct categories: Bird, Dog, and Snake[cite: 5]. 

- [cite_start]__Sourcing__: All materials were sourced from original, self-captured photography[cite: 5].
- [cite_start]__Diversity__: Gestures were recorded under controlled single-source lighting, encompassing diverse hand sizes and projection angles[cite: 8].
- [cite_start]__Specifications__: Images were unified, grayscaled, and resized to 128 x 128 pixels as tensors for optimal feature extraction[cite: 10].
- [cite_start]__Automation__: A custom Python automation script was implemented to organize the repository into a professional Dataset_Final directory architecture[cite: 6].

---

### 3. Methodology Summary
[cite_start]I developed this CNN model using the Keras Sequential API to validate real-time camera interactions and train the recognition engine[cite: 13]:

- [cite_start]__Hierarchical Feature Extraction__: By implementing three convolutional layers, I achieved feature extraction ranging from basic edges to complex silhouettes[cite: 14].
- [cite_start]__Spatial Robustness__: The integration of pooling layers ensures spatial robustness, allowing for accurate recognition despite positional shifts[cite: 15].
- [cite_start]__Classification Logic__: Finally, the visual signals are converted into a probability distribution via the Softmax function, ensuring a rigorous and scientific classification[cite: 16].

$$P(y=i | x) = \frac{e^{z_i}}{\sum_{j=1}^{3} e^{z_j}}$$

---

### 4. Creative Applications
The project explores three speculative approaches for AI application:

- [cite_start]__Approach 1: Creative Interactive System__: This project speculates on an interactive educational theater that utilizes real-time AI to transform traditional hand shadows into a multi-sensory experience[cite: 21].
- [cite_start]__Approach 2: Critical Social Experiment__: While humans embrace ambiguity, the CNN is mathematically forced by its Softmax architecture to assign 100 percent probability[cite: 29]. [cite_start]This critiques how AI simplifies complex realities into forced certainties[cite: 30].
- [cite_start]__Approach 3: Healthcare Speculation__: This proposal utilizes hand shadow edge-blur to derive an objective Stability Index to quantify fine motor skills[cite: 43, 44]. [cite_start]It offers a non-invasive solution for early screening of motor disorders like Parkinson's disease[cite: 48].

---

### 5. Project Structure
Based on the current workspace, the project contains the following files and directories:

- __shadow/__: Directory containing the raw source images for the Bird, Dog, and Snake categories.
- __Dataset_Final.zip__: A compressed archive of the finalized, grayscaled, and partitioned dataset (70/20/10 split).
- [cite_start]__Shadow Variations.pdf__: The comprehensive project report detailing the multidimensional exploration and research findings[cite: 1].
- __shadow.ipynb__: The primary Jupyter Notebook used for model development, training logs, and performance visualizations.
- __shadow.py__: The Python source script containing the model architecture and core logic.
- __Model_link.txt__: A text file containing external links or access credentials for the trained model weights.
- __test.jpg / test2.jpg / test3.jpg__: Independent sample images used for conducting inference tests on the trained model.
- __README.md__: Documentation and project guide.

---

### 6. Authors & Acknowledgements
- [cite_start]__Authors__: Hanbo Zhan, Ethan Zhang[cite: 18].
- [cite_start]__Acknowledgements__: Powered by Python, TensorFlow/Keras, and Google Teachable Machine[cite: 55]. [cite_start]Special thanks to DMLAP instructors for their guidance[cite: 55].