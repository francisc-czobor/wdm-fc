var firstName = prompt('Prenume?');
var lastName = prompt('Nume de familie?');
var age = prompt('Varsta?');
var height = prompt('Inaltime in cm?');
var momName = prompt('Numele de fecioara al mamei tale?');

alert('Merci si doamne ajuta');

var nameCond = false;
var ageCond = false;
var heightCond = false;
var momCond = false;

if (firstName[0] === lastName[0]) {
  nameCond = true;
}

if (age > 15 && age < 25) {
  ageCond = true;
}

if (height >= 180) {
  heightCond = true;
}

if (momName[momName.length - 1] === 'a') {
  momCond = true;
}

if (nameCond && ageCond && heightCond && momCond) {
  console.log('Esti un caine adevarat!');
} else {
  console.log('Pleaca stelistule!');
}
