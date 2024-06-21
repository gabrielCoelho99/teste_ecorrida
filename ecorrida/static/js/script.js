// static/js/script.js

document.getElementById('cadastrarForm').addEventListener('submit', function(event) {
  event.preventDefault();

  const username = document.getElementById('nome').value;
  const email = document.getElementById('email').value;
  const password = document.getElementById('password').value;
  const age = document.getElementById('idade').value;

  fetch('/register', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ username, email, age, password })
  })
  .then(response => response.json())
  .then(data => {
    console.log('Success:', data);
    alert('Usuário cadastrado com sucesso!');
    window.location.replace('/login');
  })
  .catch((error) => {
    console.error('Error:', error);
    alert('Erro ao cadastrar usuário.');
  });
});
