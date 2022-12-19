function showTable() {
  fetch("../data/results.json")
    .then((response) => response.json())
    .then((data) => createTable(data));
}

function createTable(data) {
  var table = "<table id='main_table' border=1>";

  table += `<tr>
        <th>Nazwa organizacji</th>
        <th>Opis</th>
        <th>Tagi</th>
        <th>Kontakt</th>
      </tr>`;
  var tr = "";
  for (let i = 0; i < data.length; i++) {
    tr += "<tr>";
    tr += `<td>${data[i].name}</td>`;
    tr += `<td>${data[i].description}</td>`;
    tr += "<td>";
    for (var key in data[i].tags) {
      tr += `<p>${data[i].tags[key]}</p>`;
    }
    tr += "</td>";
    tr += "<td>";
    if (data[i].email != null) {
      tr += `<p>${data[i].email}</p>`;
    }
    if (data[i].facebook != null) {
      tr += `<p>${data[i].facebook}</p>`;
    }
    if (data[i].website != null) {
      tr += `<p>${data[i].website}</p>`;
    }
    tr += "</td>";
    tr += "</tr>";
  }
  table += tr + "</table>";

  document.body.innerHTML += table;
}

function searchFunction() {
  var filter, table, row;
  filter = document.getElementById("search-field").value.toUpperCase();
  table = document.getElementById("main_table").getElementsByTagName("tr");
  for (var i = 1; i < table.length; i++) {
    row = table[i];
    if (row.innerHTML.toUpperCase().indexOf(filter) > -1) {
      table[i].style.display = "";
    } else {
      table[i].style.display = "none";
    }
  }
}

function selectRandom() {
  var table, random_number;
  table = document.getElementById("main_table").getElementsByTagName("tr");
  random_number = Math.floor(Math.random() * (table.length-1))+1;
  for (var i = 1; i < table.length; i++) {
      table[i].style.display = "none";
  }
  table[random_number].style.display = "";
}

function resetTable() {
  var table;
  table = document.getElementById("main_table").getElementsByTagName("tr");
  for (var i = 1; i < table.length; i++) {
      table[i].style.display = "";
  }
  document.getElementById("search-field").value = "";
}
