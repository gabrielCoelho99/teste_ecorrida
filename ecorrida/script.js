// static/js/script.js

document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();
  
    const username = document.getElementById('username').value;
    const email = document.getElementById('email').value;
    const age = document.getElementById('age').value;
  
    fetch('/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json' // Corrected content type
      },
      body: JSON.stringify({ username, email, age })  // Use JSON for data
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      alert('Usuário cadastrado com sucesso!');
      window.location.replace('/login'); // Redireciona para a página de login
    })
    .catch((error) => {
      console.error('Error:', error);
      alert('Erro ao cadastrar usuário.');
    });
  });
  
  document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
  
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
  
    fetch('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json' // Corrected content type
      },
      body: JSON.stringify({ email, password })  // Use JSON for data
    })
    .then(response => response.json())
    .then(data => {
      console.log('Success:', data);
      alert('Login realizado com sucesso!');
      // Aqui você pode redirecionar o usuário para a página desejada após o login
    })
    .catch((error) => {
      console.error('Error:', error);
      alert('Erro ao fazer login.');
    });
  });
  