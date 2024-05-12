// Spruce is a logging library for all your favorite languages
// by Constantin Volke (aka Wervice)

// Include this into your code by copying the lines bellow, by using eval() or using npm

const fs = require("fs");

function getUTCDateTime() {
	const now = new Date();

	// Get UTC components
	const utcHours = String(now.getUTCHours()).padStart(2, "0");
	const utcMinutes = String(now.getUTCMinutes()).padStart(2, "0");
	const utcSeconds = String(now.getUTCSeconds()).padStart(2, "0");
	const utcMilliseconds = String(now.getUTCMilliseconds()).padStart(3, "0");
	const utcDay = String(now.getUTCDate()).padStart(2, "0");
	const utcMonth = String(now.getUTCMonth() + 1).padStart(2, "0"); // Months are zero-based
	const utcYear = String(now.getUTCFullYear());

	// Construct the template
	const template = `${utcHours}:${utcMinutes}:${utcSeconds}:${utcMilliseconds} ${utcMonth}/${utcDay}/${utcYear}`;

	return template;
}

function colorText(text, color) {
	const colors = {
		dimmed: "\x1b[2m",
		red: "\x1b[31m",
		green: "\x1b[32m",
		yellow: "\x1b[33m",
		blue: "\x1b[34m",
		cyan: "\x1b[36m",
	};

	const reset = "\x1b[0m";

	if (colors[color]) {
		return colors[color] + text + reset;
	} else {
		return text; // Return text without color if color not found
	}
}

function spruce(level, message) {
	if (level == "verb" || level == "verbose" || level == 0 || level == "V") {
		if (spruce_verbose == true) {
			console.log(
				colorText(`[VERBOSE] @ ${getUTCDateTime()} | ${message}`, "blue"),
			);
		fs.appendFileSync(
			spruce_path,
			`[VERBOSE]\t${getUTCDateTime()}\t${message}\n`,
		);
		}
	} else if (
		level == "succ" ||
		level == "success" ||
		level == 1 ||
		level == "S"
	) {
		console.log(
			colorText(`[SUCCESS] @ ${getUTCDateTime()} | ${message}`, "green"),
		);
		fs.appendFileSync(
			spruce_path,
			`[SUCCESS]\t${getUTCDateTime()}\t${message}\n`,
		);
	} else if (
		level == "warn" ||
		level == "warning" ||
		level == 2 ||
		level == "W"
	) {
		console.log(
			colorText(`[WARNING] @ ${getUTCDateTime()} | ${message}`, "yellow"),
		);
		fs.appendFileSync(
			spruce_path,
			`[WARNING]\t${getUTCDateTime()}\t${message}\n`,
		);
	} else if (
		level == "erro" ||
		level == "error" ||
		level == 3 ||
		level == "E"
	) {
		console.log(colorText(`[ERROR] @ ${getUTCDateTime()} | ${message}`, "red"));
		fs.appendFileSync(
			spruce_path,
			`[ERROR]\t\t${getUTCDateTime()}\t${message}\n`,
		);
	} else if (
		level == "fata" ||
		level == "fatal" ||
		level == 4 ||
		level == "F"
	) {
		console.log(
			colorText(
				`\x1b[1m[FATAL ERROR] @ ${getUTCDateTime()} | ${message}\x1b[0m`,
				"red",
			),
		);
		fs.appendFileSync(
			spruce_path,
			`[FATAL ERROR]\t${getUTCDateTime()}\t${message}\n`,
		);
	} else {
		throw new Error("Spruce does not know this type of logging level");
	}
}

if (typeof spruce_path == "undefined") {
	throw new Error(
		"Spruce file path is not set.\nPlease define the variable spruce_path",
	);
}

if (typeof spruce_verbose == "undefined") {
	spruce_verbose = true;
}

if (!fs.existsSync(spruce_path))
	fs.writeFileSync(spruce_path, "Level\t\tTime\t\t\tMessage\n");
