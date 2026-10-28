export function initLeadForm() {
  const leadForm = document.getElementById('leadForm');
  const successMsg = document.getElementById('successMsg');

  if (!leadForm) return;

  leadForm.addEventListener('submit', async function (event) {
    event.preventDefault();

    const nameInput = document.getElementById('name').value;
    const phoneInput = document.getElementById('phone').value;

    const formData = {
      full_name: nameInput,
      phone: phoneInput
    };

    try {
      const response = await fetch('http://127.0.0.1:8000/api/applications/create/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formData)
      });

      if (response.ok) {
        leadForm.reset();
        if (successMsg) {
          successMsg.style.display = 'block';
        } else {
          alert('Заявка успешно отправлена!');
        }
      } else {
        alert('Ошибка при отправке. Проверьте данные.');
      }
    } catch (error) {
      console.error('Ошибка сети:', error);
      alert('Не удалось связаться с сервером.');
    }
  });
}