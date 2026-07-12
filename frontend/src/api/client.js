const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

async function handleResponse(response) {
  const data = await response.json().catch(() => ({}));
  if (!response.ok) {
    throw new Error(data.detail || data.message || 'Request failed');
  }
  return data;
}

export async function predictEquipment(file) {
  const formData = new FormData();
  formData.append('file', file);
  const response = await fetch(`${API_BASE_URL}/predict`, {
    method: 'POST',
    body: formData,
  });
  return handleResponse(response);
}

export async function getEquipmentInfo(equipment = '') {
  const url = equipment
    ? `${API_BASE_URL}/equipment-info?equipment=${encodeURIComponent(equipment)}`
    : `${API_BASE_URL}/equipment-info`;
  const response = await fetch(url);
  return handleResponse(response);
}

export async function recommendAccessories(equipment) {
  const response = await fetch(`${API_BASE_URL}/recommend-accessories?equipment=${encodeURIComponent(equipment)}`);
  return handleResponse(response);
}

export async function postJson(path, payload) {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  return handleResponse(response);
}
