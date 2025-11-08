from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.llms import OpenAI

"""示例：使用 DeepSeek/OpenAI 兼容端点的 LangChain 调用。

说明：把 `your-deepseek-api-key` 替换为实际的 API Key；
如果使用 DeepSeek，请确保 `openai_api_base` 指向正确的 DeepSeek base URL。
该脚本对不同 LangChain 版本的调用做了小的兼容处理，以减少按版本出错的几率。
"""


def run_examples():
    # 初始化 DeepSeek Chat 模型（Chat 模型）
    chat_model = ChatOpenAI(
        model_name="deepseek-chat",
        openai_api_key="your-deepseek-api-key",
        openai_api_base="https://api.deepseek.com",
    )

    messages = [
        SystemMessage(content="你是一个有帮助的AI助手。"),
        HumanMessage(content="解释什么是LangChain?")
    ]

    # 对不同版本的 LangChain 做兼容调用（predict_messages, __call__, 或 inspect 返回结构）
    try:
        ai_msg = chat_model.predict_messages(messages)
        # predict_messages 返回一个 AIMessage
        print("Chat response:", ai_msg.content)
    except Exception:
        try:
            # 直接调用模型（一些版本支持 chat_model(messages)）
            result = chat_model(messages)
            # result 可能是 AIMessage 或 ChatResult
            if hasattr(result, "content"):
                print("Chat response:", result.content)
            elif hasattr(result, "generations"):
                gen = result.generations
                # 安全访问嵌套结构
                text = None
                try:
                    text = gen[0][0].text
                except Exception:
                    try:
                        text = gen[0].text
                    except Exception:
                        text = str(gen)
                print("Chat response:", text)
            else:
                print("Chat response (raw):", result)
        except Exception as e:
            print("Chat model call failed:", e)

    # 使用 LLM（文本输入/输出）
    llm = OpenAI(
        model_name="deepseek-chat",
        openai_api_key="your-deepseek-api-key",
        openai_api_base="https://api.deepseek.com",
    )

    # 多种接口兼容：__call__ 返回字符串；旧版可能有 generate/invoke
    prompt = "什么是机器学习?"
    try:
        res = llm(prompt)
        print("LLM result:", res)
    except Exception:
        try:
            gen = llm.generate([prompt])
            # 解析 generate 返回的结构
            try:
                print("LLM result:", gen.generations[0][0].text)
            except Exception:
                print("LLM result (raw generate):", gen)
        except Exception as e:
            print("LLM call failed:", e)


if __name__ == "__main__":
    run_examples()