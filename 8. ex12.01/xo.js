var tds = document.querySelectorAll("td");

for (var i = 0; i < tds.length; ++i) {
	tds[i].addEventListener("click", function () {
		var tc = this.textContent;

		if (tc === "X") {
			this.textContent = "O";
		} else if (tc === "O") {
			this.textContent = "";
		} else {
			this.textContent = "X";
		}
	});
}

function clear(elem) {
	elem.textContent = "";
}

document.querySelector("button").addEventListener("click", function () {
	for (var i = 0; i < tds.length; ++i) {
		clear(tds[i]);
	}
});
