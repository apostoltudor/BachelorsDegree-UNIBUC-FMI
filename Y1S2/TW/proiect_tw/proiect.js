document.querySelectorAll('h1').forEach(function(h1) {
    h1.style.backgroundColor = '#f6dfd0'; // Crem
    h1.style.border = '8px outset #5C4033'; // Maro
  
    // Adaugă un event listener pentru evenimentul 'mouseover'
    h1.addEventListener('mouseover', function() {
      h1.style.border = '8px outset white'; // Border devine alb
    });
  
    // Adaugă un event listener pentru evenimentul 'mouseout'
    h1.addEventListener('mouseout', function() {
      h1.style.border = '8px outset #5C4033'; // Revenire la border maro
    });
  });




// Selectează toate elementele h2
var headers = document.querySelectorAll('h2');

// Iterează prin toate elementele h2 și aplică stilul de subliniere
headers.forEach(function(header) {
  header.style.textDecoration = 'underline';
});






document.addEventListener('DOMContentLoaded', function() {
  // Creează un nou element de tip paragraf
  var paragraf = document.createElement('p');
  paragraf.textContent = 'Vă vom contacta telefonic și prin e-mail în cel mai scurt timp posibil în legătură cu cererea voastră. Între timp, v-aș ruga să ne sugerați pagina prietenilor și membrilor familiei care ar dori să adopte o pisică! ';

  // Modifică stilul paragrafului
  paragraf.style.fontSize = '220%'; // Schimbă dimensiunea fontului
  paragraf.style.border = '8px outset #5C4033'; // Adaugă un border cu o anumită culoare și mărime
  paragraf.style.textAlign = 'center'; // Centrează textul
  paragraf.style.marginLeft = 'auto'; // Centrează elementul pe orizontală
  paragraf.style.marginRight = 'auto';
  paragraf.style.display = 'block'; // Asigură-te că elementul poate fi centrat (nu este inline)
  paragraf.style.backgroundColor = '#f6dfd0';
  paragraf.style.padding = '4%';

  // Găsește elementul după ID
  var element = document.getElementById('js_create');

  // Adaugă paragraful în document după elementul găsit
  element.insertAdjacentElement('afterend', paragraf);

  // Funcție pentru a genera o culoare aleatorie
  function getRandomColor() {
      var letters = '0123456789ABCDEF';
      var color = '#';
      for (var i = 0; i < 6; i++) {
          color += letters[Math.floor(Math.random() * 16)];
      }
      return color;
  }

  // Schimbă culoarea borderului la fiecare secundă
  var intervalId = setInterval(function() {
      paragraf.style.borderColor = getRandomColor();
  }, 1000);

  // Oprește schimbarea culorii borderului după 10 secunde și setează culoarea la negru
  setTimeout(function() {
      clearInterval(intervalId);
      paragraf.style.borderColor = 'black';
  }, 10000);
});




// document.getElementById("adoptie").addEventListener("submit", function(event) {
//   event.preventDefault();
//   window.location.href="multumim.html";
// });




document.getElementById('adoptie').addEventListener('submit', function(event) {
  event.preventDefault();

  // Validare formular
  const name = document.getElementById('name').value;
  const age = document.getElementById('age').value;
  const email = document.getElementById('email').value;
  const phone = document.getElementById('phone').value;
  const city = document.getElementById('city').value;
  const housing = document.getElementById('housing').value;
  const pets = document.getElementById('pets').value;
  const cat = document.getElementById('cat').value;

  // Expresii regulate pentru validare
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

  // Salvarea datelor în localStorage
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

  // Redirecționarea către pagina "multumim.html"
  window.location.href = 'multumim.html';
});


// console.log(JSON.parse(localStorage.getItem('adoptionData')));   //pentru a vedea datele



document.querySelectorAll('.pisica').forEach(item => {
  item.addEventListener('click', function(event) {
      event.currentTarget.classList.toggle('highlight');
      console.log('Elementul clicat:', event.target);
  });    // adaugă un listener de evenimente pe fiecare element cu clasa .pisica. 
  // Când un element este clicat, clasa highlight este adăugată sau eliminată,
  // iar elementul clicat este afișat în consolă.
});


document.querySelectorAll('.pisica').forEach(item => {
  item.addEventListener('click', function(event) {
      event.stopPropagation(); // Oprirea propagării evenimentului
      var stiluri = window.getComputedStyle(event.currentTarget);
      console.log('Culoarea de fundal:', stiluri.backgroundColor);
  });
});


document.addEventListener('keydown', function(event) {
  if (event.key === 'n') {
      window.location.href = '/disponibile.html'; // Navighează la pagina cu pisici disponibile
  }
});








