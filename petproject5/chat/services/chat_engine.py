from langchain_google_genai import ChatGoogleGenerativeAI
from .retriever import get_device_retriever
from .prompt import get_prompt
from .web_search import web_search
from django.conf import settings


def built_chat_history(messages, limit=10):
    history = []
    for msg in messages.order_by("-timestamp")[:limit][::-1]:
        role = "Assistent" if msg.is_bot else "User"
        history.append(f"{role}: {msg.content}")
    return "\n".join(history)


def chat_engine(device, user_message, messages_queryset):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=settings.GOOGLE_API_KEY,
        temperature=0,
    )

    retriever = get_device_retriever(device.id)
    prompt = get_prompt()

    chat_history = built_chat_history(messages_queryset)

    context = ""
    needs_web = False

    if retriever:
        docs = retriever.invoke(user_message)
        if docs:
            top_doc = docs[0]
            context = "\n".join(doc.page_content for doc in docs)
            if hasattr(top_doc, "score") and top_doc.score < 0.6:
                needs_web = True
        else:
            needs_web = True
    else:
        needs_web = True

    if context and not needs_web:
        check_prompt = (
            f"Вопрос: {user_message}\n"
            f"Контекст: {context}\n"
            f"Есть ли прямой ответ в этом контексте? Ответь только 'ДА' или 'НЕТ'."
        )
        check_response = llm.invoke(check_prompt)
        if "НЕТ" in check_response.content.upper():
            needs_web = True

    web_context = ""
    if needs_web:
        web_context = web_search(f"{device.model} {user_message}")

    final_prompt = prompt.format(
        device_model=device.model,
        chat_history=chat_history,
        context=context,
        web_context=web_context,
        question=user_message,
    )

    response = llm.invoke(final_prompt)

    return response.content
