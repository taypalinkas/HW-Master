// from data.js
var tableData = data;

// YOUR CODE HERE!

d3.select("tbody")
  .selectAll("tr")
  .data(tableData)
  .enter()
  .append("tr")
  .html(function(d) {
    return `<td>${d.datetime}</td><td>${d.city}</td><td>${d.state}</td><td>${d.country}</td><td>${d.shape}</td><td>${d.durationMinutes}</td>><td>${d.comments}</td>`;
  });

d3.selectAll("#filter-btn").on("click", doSearch);

function doSearch() {
    d3.event.preventDefault();
    var searchElement = d3.select("#datetime");
    var searchValue = searchElement.property("value");
    var filteredData = tableData.filter(dates => dates.datetime === searchValue);
    console.log(searchValue);

    d3.select("tbody").html("");
    d3.select("tbody")
    .selectAll("tr")
    .data(filteredData)
    .enter()
    .append("tr")
    .html(function(d) {
        return `<td>${d.datetime}</td><td>${d.city}</td><td>${d.state}</td><td>${d.country}</td><td>${d.shape}</td><td>${d.durationMinutes}</td>><td>${d.comments}</td>`;
     });

};

/* funcitons for object oriented programming