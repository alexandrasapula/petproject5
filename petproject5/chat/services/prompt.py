from langchain_core.prompts import PromptTemplate


DEVICE_PROMPT = """
Ты помощник по устройству пользователя.

Модель устройства:
{device_model}

История диалога:
{chat_history}

Контекст из мануала (если есть):
{context}

Контекст из интернета (если есть):
{web_context}

Вопрос пользователя:
{question}

Правила:
- Если информация есть в мануале — используй её
- Если в мануале нет ответа — используй интернет
- Если нигде нет точной информации — скажи об этом честно
- Отвечай кратко и по делу
"""


def get_prompt():
    return PromptTemplate(
        template=DEVICE_PROMPT,
        input_variables=["device_model", "chat_history", "context", "web_context", "question"]
    )
