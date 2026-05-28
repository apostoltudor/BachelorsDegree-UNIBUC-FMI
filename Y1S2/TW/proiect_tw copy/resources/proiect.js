document.querySelectorAll('h1').forEach(function(h1) {
    h1.style.backgroundColor = '#f6dfd0'; 
    h1.style.border = '8px outset #5C4033'; 
  
    h1.addEventListener('mouseover', function() {
      h1.style.border = '8px outset white'; 
    });
  
    h1.addEventListener('mouseout', function() {
      h1.style.border = '8px outset #5C4033'; 
    });
  });




var headers = document.querySelectorAll('h2');

headers.forEach(function(header) {
  header.style.textDecoration = 'underline';
});






document.addEventListener('DOMContentLoaded', function() {
  var paragraf = document.createElement('p');
  paragraf.textContent = 'Vă vom contacta telefonic și prin e-mail în cel mai scurt timp posibil în legătură cu cererea voastră. Între timp, v-aș ruga să ne sugerați pagina prietenilor și membrilor familiei care ar dori să adopte o pisică! ';

  paragraf.style.fontSize = '220%'; 
  paragraf.style.border = '8px outset #5C4033'; 
  paragraf.style.textAlign = 'center';
  paragraf.style.marginLeft = 'auto';
  paragraf.style.marginRight = 'auto';
  paragraf.style.display = 'block'; 
  paragraf.style.backgroundColor = '#f6dfd0';
  paragraf.style.padding = '4%';

  var element = document.getElementById('js_create');

  element.insertAdjacentElement('afterend', paragraf);

  function getRandomColor() {
      var letters = '0123456789ABCDEF';
      var color = '#';
      for (var i = 0; i < 6; i++) {
          color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
  }

  var intervalId = setInterval(function() {
      paragraf.style.borderColor = getRandomColor();
  }, 1000);

  setTimeout(function() {
      clearInterval(intervalId);
      paragraf.style.borderColor = 'black';
  }, 10000);
});






document.getElementById('adoptie').addEventListener('submit', function(event) {
  event.preventDefault();

  const name = document.getElementById('name').value;
  const age = document.getElementById('age').value;
  const email = document.getElementById('email').value;
  const phone = document.getElementById('phone').value;
  const city = document.getElementById('city').value;
  const housing = document.getElementById('housing').value;
  const pets = document.getElementById('pets').value;
  const cat = document.getElementById('cat').value;

  const nameRegex = /^[a-zA-Z\s]+$/;
  const ageRegex = /^[0-9]+$/;
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const phoneRegex = /^[0-9]{10}$/;
  const cityRegex = /^[a-zA-Z\s]+$/;

  if (!nameRegex.test(name)) {
      alert('Numele nu este valid');
      return;
  }
  if (!ageRegex.test(age) || age <= 0) {
      alert('Vârsta nu este validă');
      return;
  }
  if (!emailRegex.test(email)) {
      alert('Email-ul nu este valid');
      return;
  }
  if (!phoneRegex.test(phone)) {
      alert('Numărul de telefon nu este valid');
      return;
  }
  if (!cityRegex.test(city)) {
      alert('Orașul nu este valid');
      return;
  }

  const adoptionData = {
      name: name,
      age: age,
      email: email,
      phone: phone,
      city: city,
      housing: housing,
      pets: pets,
      cat: cat,
      timestamp: new Date().toLocaleString()
  };

  localStorage.setItem('adoptionData', JSON.stringify(adoptionData));

  window.location.href = '/multumim';
});



document.addEventListener('DOMContentLoaded', function() {
  var selectInput = document.getElementById('recommendSelect');

  selectInput.addEventListener('change', function(event) {
      var selectedValue = event.target.value;
      if (selectedValue) {
          console.log('Ne-ați recomanda unui prieten?:', selectedValue);
      } else {
          console.log('Nicio opțiune selectată');
      }
  });
});



document.addEventListener('DOMContentLoaded', function() {
  var adoptie = document.getElementById('adoptie');
  if (adoptie) {
      adoptie.addEventListener('submit', function(event) {
          event.preventDefault(); 
          var button = event.target.querySelector('button');
          button.classList.add('button-clicked');
          
          setTimeout(function() {
              window.location.href = '/multumim';
          }, 500);
      });
  }

  document.querySelectorAll('nav a').forEach(function(navItem) {
      navItem.addEventListener('click', function(event) {
          console.log('Elementul care a declanșat evenimentul:', event.target);
      });
  });

  var main = document.querySelector('main');
  if (main) {
      main.addEventListener('click', function(event) {
          console.log('Elementul la care este atașat ascultătorul de evenimente:', event.currentTarget);
          console.log('Elementul care a declanșat evenimentul:', event.target);
      });
  }
});

