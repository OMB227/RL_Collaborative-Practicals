# RL Collaborative Practicals

This repository contains some Jupyter notebooks designed by Dr Mehrdad Ghaziasgar as practical exercises for AIMS SA students for understanding and implementing key concepts in Reinforcement Learning (RL).

## Background

Reinforcement Learning (RL) is a branch of machine learning concerned with how agents take actions in an environment to maximize cumulative rewards. Unlike supervised learning, where models learn from labeled data, RL relies on interactions with the environment and receives feedback in the form of rewards or penalties. The core mathematical framework behind RL is based on Markov Decision Processes (MDPs), which provide a formalism for modeling decision-making problems.

### Key Concepts and Equations

- **Agent**: The entity making decisions.
- **Environment**: The system in which the agent operates.
- **State (`s`)**: A representation of the environment at a given time.
- **Action (`a`)**: The choice made by the agent.
- **Reward (`r`)**: The feedback signal guiding the learning process.
- **Policy (`π`)**: A strategy mapping states to actions.
- **Value Function (`V(s)`)**: The expected reward from a state following a given policy.
- **Q-Function (`Q(s,a)`)**: The expected reward for taking an action in a given state.

The learning process in RL revolves around optimizing the policy `π` to maximize long-term rewards. This is often done through methods like Value Iteration, Policy Gradient, and Q-Learning.

#### Key Equations:

1. **Bellman Equation for State Value Function:**
   ```math
   V(s) = \sum_{a} \pi(a|s) \sum_{s', r} p(s', r|s, a) [ r + \gamma V(s') ]
   ```

2. **Bellman Equation for Action-Value Function:**
   ```math
   Q(s, a) = \sum_{s', r} p(s', r|s, a) [ r + \gamma \sum_{a'} \pi(a'|s') Q(s', a') ]
   ```

3. **Policy Gradient Theorem:**
   ```math
   \nabla J(\theta) = \mathbb{E}_{\pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a|s) Q^{\pi_\theta}(s, a) \right]
   ```

## What You Will Find in This Repository

The repository consists of Jupyter notebooks covering:

1. **Introduction to Reinforcement Learning**
   - Definition and motivation
   - Examples of RL applications
   - Comparison with other machine learning paradigms

2. **Markov Decision Processes (MDPs)**
   - Understanding states, actions, and rewards
   - Bellman equations and value iteration

3. **Dynamic Programming for RL**
   - Policy evaluation and improvement
   - Value iteration and policy iteration algorithms

4. **Monte Carlo Methods**
   - Estimating returns
   - First-visit and every-visit Monte Carlo methods

5. **Temporal Difference Learning**
   - TD(0) and TD(`λ`)
   - SARSA and Q-Learning

6. **Deep Reinforcement Learning**
   - Introduction to function approximation
   - Deep Q-Networks (DQN) and policy gradient methods

Each notebook contains explanations, mathematical formulations, and Python implementations of RL algorithms. They also include exercises to reinforce understanding.

## Getting Started

To explore the notebooks, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/OMB227/RL_Collaborative-Practicals.git
   ```

2. Navigate to the project directory:
   ```bash
   cd RL_Collaborative-Practicals
   ```

3. Install the required dependencies (preferably inside a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```

4. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

## How to Cite This Work

If you use these materials in your work, please provide proper acknowledgment using the following citation format:

```
Author: Oumarou Moussa Bola & Dishanan Jayprokash  
Title: RL Collaborative Practicals  
Institution: AIMS SA 
Instructor: Mehrdad Ghaziasgar, University of the Western Cape
Year: 2024 
Repository: https://github.com/OMB227/RL_Collaborative-Practicals  
```

## Contributions

As this repository is primarily for educational purposes, contributions in the form of improvements or additional examples are welcome. Feel free to submit pull requests with suggestions or enhancements.

## References

For further reading, the following resources are recommended:
- **Sutton & Barto (2018)**: Reinforcement Learning: An Introduction
- **David Silver's RL Course**: Available on YouTube
- **OpenAI Spinning Up**: A guide to Deep RL

---
