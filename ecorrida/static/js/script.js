// static/js/script.js

document.getElementById('cadastrarForm').addEventListener('submit', function(event) {
  event.preventDefault();

  const username = document.getElementById('username').value;
  const email = document.getElementById('email').value;
  const age = document.getElementById('age').value;
  const password = document.getElementById('password').value;

  fetch('/register', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username, email, age, password })
  })
  .then(response => {
      if (!response.ok) {
          throw new Error('Erro ao cadastrar usuário.');
      }
      return response.json();
  })
  .then(data => {
      console.log('Success:', data);
      alert('Usuário cadastrado com sucesso!');
      window.location.replace('/login'); // Redireciona para a página de login
  })
  .catch(error => {
      console.error('Error:', error.message);
      alert('Erro ao cadastrar usuário.');
  });
});
