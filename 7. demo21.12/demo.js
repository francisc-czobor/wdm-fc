// ----- FUNCTIONS -----

// function nume([params[=default], ...]) {
// 	 ... cod ...
// }

function hello() {
	console.log('Hello world!');
}

function helloYou(name='Franci') {
  console.log('Hello, ' + name + '!');
}

function add(num1=0, num2=0) {
  return num1 + num2;
}

var chestie = 'ceva';

function procesare(a) {
  console.log(a);
  a = a + ' bau';
  console.log(a);
}

function procesare2(chestie) {
  console.log(chestie);
  chestie = chestie + ' bau';
  console.log(chestie);
}

function procesare3(a) {
  console.log(a);
  chestie = a + ' bau';
  console.log(a);
}

function procesare4(a) {
  console.log(a);
  a = a + b;
  console.log(a);
}

// ----- ARRAYS -----

// [elem1, elem2, ...]

var list = [1, 2, 3, 4, 5];

// for (var i = 0; i < list.length; ++i) {
//   console.log(list[i]);
// }

// console.log('----');

// for (elem of list) {
//   console.log(elem);
// }

// ----- OBJECTS -----

// {key='value', ...}

var masina = {
    marca: 'Volkswagen',
    an: 2007,
    model: 'Golf',
    motor: 'tdi',
    culoare: 'rosu',
    porneste: function vroom() {
      console.log('Masina porneste: saaaarpiliiii!');
    },
    vopseste: function paint(newColour) {
      console.log('Masina a fost ' + this.culoare);
      this.culoare = newColour;
      console.log('Masina acum este ' + this.culoare);
      this.porneste();
    },
    func1: function func1() {
      this.porneste = function vroom() {
        console.log('Masina porneste: vaaamoooos!');
      }
    },
    func2: function func2() {
      this.func2 = 'gata hai acasa!';
    },
    func3: function func3() {
      this.proprietar = 'Franci';
    }
}

for (attr in masina) {
  console.log(masina[attr]);
}
