function doOnLoad() {
  showTable();
}

function showTable() {
  fetch(
    "https://raw.githubusercontent.com/Byczax/lista-organizacji-studenckich/master/data/results.json"
  )
    .then((response) => response.json())
    .then((data) => createTable(data));
}

function createTable(data) {
  var table = '<table id="main_table" border=1> <col span="1" class="wide">';

  table += `<tr>
        <th>Lp.</th>
        <th>Nazwa organizacji</th>
        <th>Opis</th>
        <th>Tagi</th>
        <th>Kontakt</th>
      </tr>`;
  var tr = "";

  for (let i = 0; i < data.length; i++) {
    tr += "<tr>";
    tr += `<td>${i + 1}</td>`;
    tr += `<td>${data[i].name}</td>`;
    tr += `<td>${data[i].description}</td>`;
    tr += "<td>";
    for (var key in data[i].tags) {
      tr += `<button class=tag onClick=addTagToList(this)>${data[i].tags[key]}</button>`;
    }
    tr += "</td>";
    tr += "<td>";

    if (data[i].email != null) {
      email = data[i].email.split(":").slice(1).join(":").trim();
      tr += `<p>Email: <a href="mailto:${email}">${email}</a></p>`;
    }

    if (data[i].facebook != null) {
      fb_link = data[i].facebook.split(":").slice(1).join(":").trim();
      tr += `<p>Facebook: <a href="https://${fb_link}" target="_blank">${fb_link}</a></p>`;
    }

    if (data[i].website != null) {
      website_link = data[i].website.split(":").slice(1).join(":").trim();
      tr += `<p>Strona internetowa: <a href="https://${website_link}" target="_blank">${website_link}</a><p>`;
    }
    tr += "</td>";
    tr += "</tr>";
  }
  table += tr + "</table>";

  document.body.innerHTML += table;
  loadTagHelp();
}

function searchFunction() {
  var filter, table, row;
  filter = document.getElementById("search-field").value.toUpperCase();
  tags = document.getElementsByClassName("filter-tag");
  filter_tags = [];
  for (const tag of tags) {
    filter_tags.push(
      tag.innerHTML.replace('<i class="fa fa-close"></i>', "").trim()
    );
  }

  table = document.getElementById("main_table").getElementsByTagName("tr");

  for (var i = 1; i < table.length; i++) {
    row = table[i];

    if (
      row.innerHTML.toUpperCase().indexOf(filter) > -1 &&
      filter_tags.every(
        (tag) => row.innerHTML.toUpperCase().indexOf(tag.toUpperCase()) > -1
      )
    ) {
      table[i].style.display = "";
    } else {
      table[i].style.display = "none";
    }
  }
}

function selectRandom() {
  var table, random_number;
  table = document.getElementById("main_table").getElementsByTagName("tr");
  random_number = Math.floor(Math.random() * (table.length - 1)) + 1;

  for (var i = 1; i < table.length; i++) {
    table[i].style.display = "none";
  }
  table[random_number].style.display = "";
}

function resetTable() {
  var table = document.getElementById("main_table").getElementsByTagName("tr");

  for (var i = 1; i < table.length; i++) {
    table[i].style.display = "";
  }
  document.getElementById("search-field").value = "";
}

function loadTagHelp() {
  var tags = document.getElementsByClassName("tag");

  var tags_set = new Set();
  for (const tag of tags) {
    tags_set.add(tag.innerHTML);
  }
  tag_help_list = [];

  for (const tag of tags_set) {
    tag_construction = `<option value="${tag}">${tag}</option>`;
    tag_help_list.push(tag_construction);
  }
  tag_help_list.sort();

  for (const tag of tag_help_list) {
    document.getElementById("tags-list-help").innerHTML += tag;
  }
  console.log("TAGS LOADED");
}

function removeTagFromList(button) {
  button.remove();
  searchFunction();
}

function addTagToList(button) {
  handleAddAndSearch(button.innerHTML);
}

function handleAddTag() {
  var tag = document.getElementById("tags-list-help").value;
  handleAddAndSearch(tag);
}

function handleAddAndSearch(text) {
  var tag_list = document.getElementById("active-filter-tags");
  var tag_construction = `<button class="filter-tag" onclick="removeTagFromList(this)"><i class="fa fa-close"></i> ${text}</button>`;
  if (tag_list.innerHTML.indexOf(tag_construction) > -1) {
    return;
  }
  tag_list.innerHTML += tag_construction;
  searchFunction();
}

function removeTagFromSelect(text) {
  var tag_list = document.getElementById("tags-list-help");
  var tag_construction = `<option value="${text}">${text}</option>`;
  tag_list.innerHTML = tag_list.innerHTML.replace(tag_construction, "");
}

function clearTags() {
  document.getElementById("active-filter-tags").innerHTML = "";
  searchFunction();
}
