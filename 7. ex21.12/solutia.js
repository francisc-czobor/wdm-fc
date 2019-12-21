var roster = [];

function addNew() {
  var newName = prompt('Ce nume doresti sa adaugi?');
  roster.push(newName);
}

function remove() {
  var remName = prompt('Ce nume doresti sa stergi?');
  var index = roster.indexOf(remName);
  if (index !== -1) {
    roster.splice(index, 1);
  }
}

function display() {
  console.log(roster);
}

var start = prompt('Pornim aplicatia? y/n');
var request = '';

if (start === 'y') {
  while (request !== 'quit') {
    request = prompt('Selecteaza o actiune: add, remove, display sau quit.')
    if (request === 'add') {
      addNew();
    } else if (request === 'display') {
      display();
    } else if (request === 'remove') {
      remove();
    }
  }
}
alert('Doamne ajuta si drum bun!');
