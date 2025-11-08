from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

# 创建 LLM 实例
llm = ChatOpenAI(
    temperature=0.7,
    model="glm-4.6",
    openai_api_key="xxx",
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)

# 创建消息
messages = [
    SystemMessage(content="你是一个有用的 AI 助手"),
    HumanMessage(content="请介绍一下人工智能的发展历程")
]

# 调用模型
response = llm.invoke(messages)
print(response.content)