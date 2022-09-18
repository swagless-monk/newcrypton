// Automatic removal of alerts after X seconds
const alert = document.querySelector('.alert');

const removeAlert = () => {
  setInterval(() => {
      alert.style.display = 'none';
  }, 3500);
}

if (alert) {
  removeAlert();
} else {
}
