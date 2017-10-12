var ROOT = "b";
var filesystem  = {
	"a": {
		"id":"a",
		"parent": "b",
		"type": "folder",
		"name": "Folder-A",
		"lastModified": 1507211462,
		"children": ["f"]
	},
	"b": {
		"id":"b",
		"parent": null,
		"type": "folder",
		"name": "Folder-B",
		"lastModified": 1507211462,
		"children": ["a", "c", "d"]
	},
	"d": {
		"id":"d",
		"parent": "b",
		"type": "folder",
		"name": "Folder-D",
		"lastModified": 1507211462,
		"children": []
	},
	"f": {
		"id":"f",
		"parent": "a",
		"type": "file",
		"name": "File-F",
		"lastModified": 1507211462,
		"children": []
	},
	"c": {
		"id":"c",
		"parent": "b",
		"type": "file",
		"name": "File-C",
		"lastModified": 1507211462,
		"children": []
	},
		"g": {
		"id":"g",
		"parent": "a",
		"type": "folder",
		"name": "Folder-G",
		"lastModified": 1507211462,
		"children": []
	}
}

function getChildren(id) {
	var children = [];
	$.each(filesystem[id].children, function(index, value) {
		children.push(filesystem[value]);
	});
	return children;
}

function getParent(id) {
	if (!filesystem[id].parent) {
		return filesystem[id];
	}
	return filesystem[filesystem[id].parent];
}
function setFolder(id) {
	var id = id || ROOT;
	if (!filesystem[id]) {
		return;
	}
	if (filesystem[id].type != "folder") {
		return;
	}
	console.log(filesystem[id]);
	RenderBreadCrumbPath(id);
	drawJSONexplorer(id, getChildren(id));
   	displayTable(id, getChildren(id));
   	
}
function el(name, options) {
	var el = document.createElement(name);
	if (!options) {
		return el;
	}
	if (options.id) {
		el.id = options.id;
	}
	if (options.class) {
		el.className = options.class;
	}
	if (options.html) {
		el.innerHTML = options.html;
	}
	$.each(options, function(key, value) {
		el.setAttribute(key, value);
	});
	return el;
}
$(document).ready(function() {
	setFolder(ROOT);
});
