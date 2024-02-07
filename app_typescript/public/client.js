fetch('/api/time')
  .then(response => response.json())
  .then(data => {
    document.getElementById('time').innerText = data.time;
  })
  .catch(error => console.error('Error:', error));
