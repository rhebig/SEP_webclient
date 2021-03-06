var ROOT = "ROOT";
var filesystem;
var current_folder = "ROOT";

function exists(id) {
	return filesystem.hasOwnProperty(id);
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
function getFolder() {
	return current_folder;
}
function setFolder(id) {
	var id = id || getFolder();
	if (!exists(id)) {
		return;
	}
	if (filesystem[id].type != "folder") {
		return false;
	}
	current_folder = id;
	RenderBreadCrumbPath(id);
   	displayList(id, getChildren(id));

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
function refreshFilesystem(id) {
	$.ajax({
		url:"/filesystem",
		method:"GET",
		dataType:"JSON",
		success:function(data) {
			if (!data.success) {
				alert("Error collecting filesystem");
				return;
			}
			//Here we should set root if root is not statically defined by searching through
			//the file system and finding the element with no parent
			filesystem = data.filesystem;
			setFolder(id);
		}
	});		
}
$(document).ready(function() {
	refreshFilesystem();
});