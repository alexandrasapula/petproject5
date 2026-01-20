const deviceList = document.getElementById('device-list');
const addDeviceBtn = document.getElementById('add-device-btn');

const deviceDetails = document.getElementById('device-details');
const deviceFormSection = document.getElementById('device-form-section');
const emptyState = document.getElementById('empty-state');

const deviceTitle = document.getElementById('device-title');
const deviceNameEl = document.getElementById('device-name');
const deviceModelEl = document.getElementById('device-model');
const deviceSerialEl = document.getElementById('device-serial');
const deviceStartDateEl = document.getElementById('device-start-date');
const deviceWorkedEl = document.getElementById('device-worked');
const manualLink = document.getElementById('device-manual');

const editBtn = document.getElementById('edit-device-btn');
const deleteBtn = document.getElementById('delete-device-btn');

const form = document.getElementById('device-form');
const formTitle = document.getElementById('form-title');
const cancelFormBtn = document.getElementById('cancel-form-btn');

const chatSidebar = document.getElementById('chat-sidebar');

if (chatSidebar) {
    chatSidebar.classList.add('hidden');
}

const csrfToken = document.querySelector('meta[name="csrf-token"]').content;

let currentDeviceId = null;

function hideAll() {
    deviceDetails.classList.add('hidden');
    deviceFormSection.classList.add('hidden');
    emptyState.classList.add('hidden');
}

function calculateWorkedDays(startDate) {
    if (!startDate) return '-';
    const start = new Date(startDate);
    const today = new Date();
    const diff = today - start;
    return Math.floor(diff / (1000 * 60 * 60 * 24));
}

async function loadDevices() {
    const res = await fetch('/devices/');
    const devices = await res.json();

    deviceList.innerHTML = '';

    devices.forEach(device => {
        const li = document.createElement('li');
        li.textContent = device.name || device.model;
        li.onclick = () => showDevice(device.id);
        deviceList.appendChild(li);
    });
}


async function showDevice(id) {
    const res = await fetch(`/device/${id}/`);
    const device = await res.json();

    currentDeviceId = device.id;

    hideAll();
    deviceDetails.classList.remove('hidden');

    const title = device.name || device.model;

    deviceTitle.textContent = title;
    deviceNameEl.textContent = device.name || '-';
    deviceModelEl.textContent = device.model;
    deviceSerialEl.textContent = device.serial_number || '-';
    deviceStartDateEl.textContent = device.start_date || '-';
    deviceWorkedEl.textContent = calculateWorkedDays(device.start_date);

    manualLink.href = device.manual;
    manualLink.style.display = device.manual ? 'inline' : 'none';

    const manualStatus = document.getElementById('manual-status');

    if (device.manual) {
        manualStatus.textContent = '';
    } 
    else {
        manualStatus.textContent = 'No manual';
    }
    chatSidebar.classList.remove('hidden');
}

addDeviceBtn.onclick = () => {
    currentDeviceId = null;
    form.reset();

    hideAll();
    deviceFormSection.classList.remove('hidden');
    formTitle.textContent = 'Add device';
    if (chatSidebar) {
        chatSidebar.classList.add('hidden');
    }
};


editBtn.onclick = async () => {
    const res = await fetch(`/device/${currentDeviceId}/`);
    const device = await res.json();

    form.name.value = device.name || '';
    form.model.value = device.model;
    form.serial_number.value = device.serial_number || '';
    form.start_date.value = device.start_date || '';

    hideAll();
    deviceFormSection.classList.remove('hidden');
    formTitle.textContent = 'Edit device';
};

form.onsubmit = async (e) => {
    e.preventDefault();

    // const data = {
    //     name: form.name.value || null,
    //     model: form.model.value,
    //     serial_number: form.serial_number.value || null,
    //     start_date: form.start_date.value || null
    // };
    const formData = new FormData(form);

    const url = currentDeviceId
        ? `/device/${currentDeviceId}/update/`
        : `/devices/`;

    const method = currentDeviceId ? 'PUT' : 'POST';

    // await fetch(url, {
    //     method,
    //     headers: {
    //         'Content-Type': 'application/json',
    //         'X-CSRFToken': csrfToken
    //     },
    //     body: formData
    // });

    await fetch(url, {
        method,
        headers: {
            'X-CSRFToken': csrfToken
        },
        body: formData
    });


    hideAll();
    emptyState.classList.remove('hidden');
    loadDevices();
};

deleteBtn.onclick = async () => {
    if (!confirm('Delete this device?')) return;

    await fetch(`/device/${currentDeviceId}/delete/`, {
        method: 'DELETE',
        headers: { 'X-CSRFToken': csrfToken }
    });

    hideAll();
    emptyState.classList.remove('hidden');
    loadDevices();
};

cancelFormBtn.onclick = () => {
    hideAll();
    emptyState.classList.remove('hidden');
    if (chatSidebar) {
        chatSidebar.classList.add('hidden');
    }
};

hideAll();
emptyState.classList.remove('hidden');
loadDevices();
