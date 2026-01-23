function clearForm(form) {
    form.reset();
}

function getCsrfToken(form) {
    const csrfInput = form.querySelector('[name=csrfmiddlewaretoken]');
    return csrfInput ? csrfInput.value : '';
}

function clearMessage() {
    message.textContent = '';
    message.style.color = '';
}

const loginTab = document.getElementById('login-tab');
const registerTab = document.getElementById('register-tab');

const loginForm = document.getElementById('login-form');
const registerForm = document.getElementById('register-form');

const message = document.getElementById('message');
// const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

loginTab.onclick = () => {
    loginForm.classList.remove('hidden');
    registerForm.classList.add('hidden');
    loginTab.classList.add('active');
    registerTab.classList.remove('active');
    clearForm(registerForm);
    clearMessage();   
};

registerTab.onclick = () => {
    registerForm.classList.remove('hidden');
    loginForm.classList.add('hidden');
    registerTab.classList.add('active');
    loginTab.classList.remove('active');
    clearForm(loginForm);
    clearMessage();
};

loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const csrftoken = getCsrfToken(loginForm); 
    const response = await fetch('/auth/api/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            username: document.getElementById('login-username').value,
            password: document.getElementById('login-password').value
        })
    });

    const data = await response.json();
    if (response.ok) {
        window.location.href = data.redirect || '/';
    } 
    else {
        message.style.color = 'red';
        message.textContent = data.error || 'Login error';
    }
});

registerForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const csrftoken = getCsrfToken(registerForm);
    const response = await fetch('/auth/api/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            username: document.getElementById('reg-username').value,
            email: document.getElementById('reg-email').value,
            password: document.getElementById('reg-password').value
        })
    });

    const data = await response.json();
    if (response.ok) {
        window.location.href = data.redirect || '/';
    } 
    else {
        message.style.color = 'red';
        message.textContent = JSON.stringify(data);
    }
});
