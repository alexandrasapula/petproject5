const chatForm = document.getElementById('chat-form');
const chatInput = document.getElementById('chat-input');
const chatMessages = document.getElementById('chat-messages');

chatForm.onsubmit = async (e) => {
    e.preventDefault();
    if (!currentDeviceId) return;

    const message = chatInput.value.trim();
    if (!message) return;

    addMessage('You', message, false);

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
        addMessage('Gleep', data.answer, true);
    }

    chatInput.value = '';
};


function addMessage(author, text, isBot = false) {
    const div = document.createElement('div');
    div.classList.add('chat-message');
    div.textContent = `${author}:\n${text}`;
    div.style.whiteSpace = 'pre-line';

    if (isBot) {
        div.classList.add('bot');
    } else {
        div.classList.add('user');
    }

    chatMessages.appendChild(div);
    chatMessages.scrollTop = chatMessages.scrollHeight;
}


async function fetchMessages(deviceId) {
    if (!deviceId) return;

    const res = await fetch(`/chat/send/?device_id=${deviceId}`);
    if (!res.ok) return;
    if (deviceId !== currentDeviceId) return;

    const messages = await res.json();
    const chatMessages = document.getElementById('chat-messages');
    chatMessages.innerHTML = '';
    messages.forEach(msg => {
        addMessage(msg.is_bot ? 'Gleep' : 'You', msg.content, msg.is_bot);
    });
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

function closeChat() {
    currentDeviceId = null;
    chatSidebar.classList.add('hidden');
    chatMessages.innerHTML = '';
}

function openChat(deviceId) {
    currentDeviceId = deviceId;
    chatSidebar.classList.remove('hidden');
    fetchMessages(deviceId);
}
