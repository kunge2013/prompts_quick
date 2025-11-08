from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.tools import tool
from langchain.agents import create_agent
import json 
# 创建 LLM 实例
llm = ChatOpenAI(
    temperature=0.7,
    model="glm-4.6",
    openai_api_key="xxx",
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)


@tool
def search(query: str) -> str:
    """Search for information."""
    return f"Results for: {query}"

@tool
def get_weather(location: str) -> str:
    """Get weather information for a location."""
    return f"Weather in {location}: Sunny, 72°F"

agent = create_agent(llm, tools=[search, get_weather])


# The system prompt will be set dynamically based on context
result = agent.invoke(
    {"messages": [{"role": "user", "content": "Explain machine learning"}]},
    context={"user_role": "expert"}
)
print(json.dumps(result))
print(json.dumps(result))
# {'messages': [HumanMessage(content='Explain machine learning', additional_kwargs={}, response_metadata={}, id='46d47e74-1450-4a06-91e2-324697e96f95'), AIMessage(content='\nMachine learning is a subset of artificial intelligence that enables computer systems to learn and improve from experience without being explicitly programmed. Here\'s a comprehensive explanation:\n\n## What is Machine Learning?\n\nMachine learning involves training algorithms to recognize patterns in data and make predictions or decisions based on those patterns. Instead of writing explicit rules for every possible scenario, you provide the system with data and let it "learn" the underlying relationships.\n\n## How It Works\n\n1. **Data Collection**: Gather relevant data for the problem you want to solve\n2. **Model Training**: Feed the data to an algorithm that learns patterns\n3. **Validation**: Test the model on new data to evaluate performance\n4. **Deployment**: Use the trained model to make predictions on real-world data\n5. **Monitoring**: Continuously evaluate and update the model as needed\n\n## Types of Machine Learning\n\n### 1. Supervised Learning\n- **What it is**: Learning from labeled data (input-output pairs)\n- **Examples**: \n  - Classification: Spam detection, image recognition\n  - Regression: Predicting house prices, stock market trends\n- **Common algorithms**: Linear regression, decision trees, neural networks\n\n### 2. Unsupervised Learning\n- **What it is**: Finding patterns in unlabeled data\n- **Examples**:\n  - Clustering: Customer segmentation, document grouping\n  - Dimensionality reduction: Feature extraction, data visualization\n- **Common algorithms**: K-means, hierarchical clustering, PCA\n\n### 3. Reinforcement Learning\n- **What it is**: Learning through trial and error with rewards/penalties\n- **Examples**: Game playing (Chess, Go), robotics, self-driving cars\n- **Key concept**: Agent takes actions in an environment to maximize cumulative reward\n\n## Key Concepts\n\n- **Features**: Individual measurable properties or characteristics of the data\n- **Labels**: The output or target variable you\'re trying to predict\n- **Training set**: Data used to train the model\n- **Test set**: Data used to evaluate the model\'s performance\n- **Overfitting**: When a model learns training data too well and performs poorly on new data\n- **Underfitting**: When a model is too simple to capture the underlying patterns\n\n## Common Applications\n\n- **Healthcare**: Disease diagnosis, drug discovery, personalized treatment\n- **Finance**: Fraud detection, credit scoring, algorithmic trading\n- **E-commerce**: Recommendation systems, demand forecasting, customer service\n- **Transportation**: Self-driving cars, traffic prediction, route optimization\n- **Natural Language Processing**: Translation, chatbots, sentiment analysis\n- **Computer Vision**: Face recognition, object detection, medical imaging\n\n## Benefits\n\n- **Automation**: Reduces manual effort in repetitive tasks\n- **Scalability**: Can process vast amounts of data quickly\n- **Accuracy**: Often outperforms human judgment in specific domains\n- **Adaptability**: Can learn and improve over time\n- **Personalization**: Enables customized experiences\n\n## Challenges\n\n- **Data Quality**: Requires large amounts of clean, relevant data\n- **Bias**: Can perpetuate or amplify existing biases in training data\n- **Interpretability**: Some models are "black boxes" with unclear decision-making processes\n- **Computational Resources**: Training complex models can be expensive\n- **Security**: Vulnerable to adversarial attacks\n\nMachine learning continues to evolve rapidly, with advances in deep learning, transfer learning, and edge computing expanding its capabilities and applications across virtually every industry.', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 823, 'prompt_tokens': 209, 'total_tokens': 1032, 'completion_tokens_details': None, 'prompt_tokens_details': {'audio_tokens': None, 'cached_tokens': 43}}, 'model_provider': 'openai', 'model_name': 'glm-4.6', 'system_fingerprint': None, 'id': '20251108224704aefb77d14d524aa9', 'finish_reason': 'stop', 'logprobs': None}, id='lc_run--5c070a3f-8509-4f57-a555-63a2127591c1-0', usage_metadata={'input_tokens': 209, 'output_tokens': 823, 'total_tokens': 1032, 'input_token_details': {'cache_read': 43}, 'output_token_details': {}})]}