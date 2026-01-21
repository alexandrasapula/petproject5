const chatForm = document.getElementById('chat-form');
const chatInput = document.getElementById('chat-input');
const chatMessages = document.getElementById('chat-messages');

chatForm.onsubmit = async (e) => {
    e.preventDefault();
    if (!currentDeviceId) return;

    const message = chatInput.value.trim();
    if (!message) return;

    addMessage(`You: ${message}`);

    const res = await fetch('/chat/send/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken
        },
        body: JSON.stringify({
            device_id: currentDeviceId,
            message: message
        })
    });

    const data = await res.json();

    if (data.answer) {
        addMessage(`Gleep: ${data.answer} ${data.device_model}`);
    }

    chatInput.value = '';
};


function addMessage(text) {
    const div = document.createElement('div');
    div.textContent = text;
    div.classList.add('chat-message');
    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

async function fetchMessages(deviceId) {
    if (!deviceId) return;

    const res = await fetch(`/chat/send/?device_id=${deviceId}`);
    if (!res.ok) return;

    const messages = await res.json();
    const chatMessages = document.getElementById('chat-messages');
    chatMessages.innerHTML = '';
    messages.forEach(msg => {
        const div = document.createElement('div');
        div.textContent = `${msg.is_bot ? 'Gleep' : 'You'}: ${msg.content}`;
        div.classList.add('chat-message');
        chatMessages.appendChild(div);
    });
    chatMessages.scrollTop = chatMessages.scrollHeight;
}
