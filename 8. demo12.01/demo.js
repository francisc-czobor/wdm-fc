document.getElementById("head");

document.getElementsByClassName("c");

document.getElementsByTagName("h1");

for (var i = 0; i < document.getElementsByTagName("h1").length; ++i) {
   console.log(document.getElementsByTagName("h1")[i]);
}

// ---------------

var colouredHeader = document.querySelectorAll("h1.c")[1];

function randomColour() {
	var symbols = "0123456789ABCDEF";
	var colourCode = "#";

	for (var i = 0; i < 6; ++i) {
		colourCode += symbols[Math.floor(Math.random() * 16)];
	}

	return colourCode;
}

function colourShifter() {
	colouredHeader.style.color = randomColour();
}

setInterval(colourShifter, 500);

document.querySelectorAll("h1.c")[0].addEventListener("click", function () {
	this.style.color = randomColour();
});
