# Lab 03 – Developing a Tiny Transformer Language Model

**Module:** PUSL 3205 – Large Language Models and Generative AI

## 1. Objective

The objective of this laboratory session is to develop a small Transformer-based language model from scratch using the TinyStories dataset.

This practical explores character-level tokenization, positional embeddings, masked multi-head self-attention, feed-forward networks, residual connections, layer normalization, next-token prediction, language model evaluation and text generation.

## 2. Tools and Technologies

- Python
- Visual Studio Code
- Jupyter Notebook
- PyTorch
- Hugging Face Datasets
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Gradio
- GitHub

## 3. Dataset

The roneneldan/TinyStories dataset from Hugging Face contains short stories written using relatively simple vocabulary.

A small subset was selected using streaming mode to reduce computational and storage requirements.

| Dataset | Number of Stories |
|---|---:|
| Training | 500 |
| Validation | 100 |
| Total | 600 |

Dataset source: https://huggingface.co/datasets/roneneldan/TinyStories

## 4. Tasks and Implementation

### 4.1 Dataset Loading and Exploration

The TinyStories dataset was loaded using Hugging Face Datasets. Sample stories were displayed, and their character counts, word counts and length distributions were analyzed.

### 4.2 Text Preprocessing and Tokenization

Character-level tokenization was implemented by creating a vocabulary from the training dataset.

Encoding and decoding functions were developed to convert text into numerical token IDs and reconstruct text from those IDs.

Punctuation, capitalization and whitespace were preserved to support natural text generation.

### 4.3 Training Data Preparation

Input and target sequences were created using randomly sampled text segments.

The target sequences were shifted by one character to support autoregressive next-token prediction.

### 4.4 Transformer Architecture

The decoder-only Transformer architecture consists of:

- Token embeddings
- Positional embeddings
- Masked multi-head self-attention
- Feed-forward networks
- Residual connections
- Layer normalization
- Dropout
- Linear language model head

### 4.5 Model Configuration

| Hyperparameter | Value |
|---|---:|
| Context Length | 64 |
| Batch Size | 16 |
| Embedding Dimension | 64 |
| Attention Heads | 4 |
| Transformer Layers | 2 |
| Dropout | 0.1 |
| Learning Rate | 0.0003 |
| Epochs | 3 |
| Steps per Epoch | 100 |
| Optimizer | AdamW |
| Loss Function | Cross-Entropy |

Update this table if different settings were used during training.

### 4.6 Model Training

The model was trained from scratch using next-token prediction.

The training process involved forward propagation, cross-entropy loss calculation, backpropagation, gradient clipping and parameter optimization using AdamW.

Training and validation losses were recorded across epochs.

### 4.7 Model Evaluation

The model was evaluated using validation loss and perplexity.

| Metric | Result |
|---|---|
| Total Parameters | TBD |
| Training Loss | TBD |
| Validation Loss | TBD |
| Validation Perplexity | TBD |

Perplexity was calculated by applying the exponential function to the validation cross-entropy loss.

### 4.8 Story Generation

The trained model was used to generate stories from starting prompts.

Example prompts:

- Once upon a time
- One day, a little boy
- There was a little girl
- The little dog
- In a beautiful forest

Temperature and top-k sampling were used to control the randomness and diversity of generated text.

**Generated story:**

[Insert an actual generated story from the notebook.]

### 4.9 Hyperparameter Experiments

Different Transformer configurations were investigated to understand the effects of model architecture and training duration.

| Experiment | Layers | Heads | Epochs | Validation Loss | Perplexity |
|---|---:|---:|---:|---|---|
| Baseline | 2 | 4 | 3 | TBD | TBD |
| Fewer Layers | 1 | 4 | 3 | TBD | TBD |
| Fewer Heads | 2 | 2 | 3 | TBD | TBD |
| Fewer Epochs | 2 | 4 | 2 | TBD | TBD |

Best validation-performing configuration: [Insert actual result.]

### 4.10 Model Saving and Loading

The trained model parameters, model configuration, training settings and tokenizer vocabulary were saved as a PyTorch checkpoint.

The checkpoint was reloaded to verify that the model could generate text without retraining.

### 4.11 Gradio Interface

An optional Gradio chat-style interface was developed to allow users to enter story prompts and receive generated text from the trained Transformer.

## 5. Results and Supporting Evidence

- [Jupyter Notebook](notebooks/lab03_tiny_transformer.ipynb)
- [Story Length Distribution](results/story_length_distribution.png)
- [Training History](results/training_history.csv)
- [Training and Validation Loss](results/loss_curves.png)
- [Perplexity Curve](results/perplexity_curve.png)
- [Model Evaluation](results/evaluation.csv)
- [Generated Stories](results/generated_stories.csv)
- [Temperature Experiments](results/temperature_experiments.csv)
- [Experiment Results](results/experiments.csv)
- [Experiment Comparison](results/experiment_comparison.png)
- [Experiment Perplexity](results/experiment_perplexity.png)
- [Trained Model](models/tiny_transformer.pt)
- [Screenshots](screenshots/)

## 6. Performance Improvement Mechanisms

The Transformer implements several mechanisms to improve learning and generation performance.

Multi-head attention enables the model to capture different contextual relationships. Residual connections improve gradient flow, while layer normalization supports stable training.

Dropout helps reduce overfitting, and gradient clipping controls excessively large gradients. AdamW is used to optimize model parameters.

Temperature and top-k sampling control the diversity of generated text.

## 7. Observations and Reflection

[Discuss the actual training and validation loss trends.]

[Explain which experimental model performed better and provide supporting numerical results.]

[Compare generated stories and discuss repetition, spelling mistakes, sentence structure and coherence.]

[Describe any challenges encountered during implementation and training.]

## 8. Limitations

- Limited training dataset size.
- Limited computational resources.
- Short context length.
- Character-level tokenization.
- Potential repetition and grammatical errors.
- Limited understanding of long-range dependencies.

## 9. Learning Outcomes

Through this laboratory session, I developed practical knowledge of:

- Loading datasets from Hugging Face.
- Implementing character-level tokenization.
- Preparing next-token prediction sequences.
- Understanding Transformer architecture.
- Implementing masked multi-head self-attention.
- Training a language model using PyTorch.
- Evaluating language models using loss and perplexity.
- Generating text using autoregressive sampling.
- Conducting hyperparameter experiments.
- Saving and reloading trained models.
- Developing an interactive Gradio interface.

## 10. Future Improvements

- Increase the training dataset size.
- Train the model for additional epochs.
- Increase the embedding dimension and context length.
- Implement subword tokenization.
- Experiment with learning rate scheduling.
- Explore more advanced Transformer architectures.

## 11. Conclusion

## 11. Conclusion

This practical provided hands-on experience in developing a Tiny Transformer language model from scratch using PyTorch. Through the implementation, I gained a better understanding of character-level tokenisation, embeddings, positional encoding, self-attention, Transformer architecture, and autoregressive text generation.

The experiments allowed me to investigate how different hyperparameter settings affect training loss, validation loss, perplexity, computational time, and generated text quality. Evaluating these metrics helped me understand the relationship between model complexity, predictive performance, and computational requirements.

Developing this Tiny Transformer improved my understanding of the fundamental principles behind modern Large Language Models (LLMs). It also highlighted the importance of training data, model architecture, hyperparameter optimisation, and computational resources.

Although a small Transformer has limited language generation capabilities compared to large pretrained models, this practical established a strong foundation for understanding more advanced language models. Future improvements could include increasing the training duration, expanding the dataset, optimising hyperparameters, and using GPU acceleration to improve training efficiency and model performance.

## 12. References

- TinyStories Dataset: https://huggingface.co/datasets/roneneldan/TinyStories
- PyTorch Documentation: https://pytorch.org/docs/stable/
- Hugging Face Datasets: https://huggingface.co/docs/datasets/
- Attention Is All You Need: https://arxiv.org/abs/1706.03762
- Gradio Documentation: https://www.gradio.app/docs