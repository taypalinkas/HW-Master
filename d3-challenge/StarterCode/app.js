var margin = {top: 10, right: 30, bottom: 50, left: 60},
    width = 700 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

var svg = d3.select("body")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");


d3.csv("data.csv").then(function(data_health) {
	console.log(data_health);

	var x = d3.scaleLinear()
    .domain([8, 24])
    .range([ 0, width ]);
  svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));

  var y = d3.scaleLinear()
    .domain([0, 28])
    .range([ height, 0]);
  svg.append("g")
	.call(d3.axisLeft(y));
	
	svg.append('g')
    .selectAll("dot")
    .data(data_health)
    .enter()
    .append("circle")
      .attr("cx", function (d) { return x(d.poverty); } )
      .attr("cy", function (d) { return y(d.healthcare); } )
      .attr("r", 15)
      .text(function(d) {return d.abbr;})
      .style("fill", "#69b3a2");
  svg.append("text")             
    .attr("transform",
         "translate(" + (width/2) + " ," + 
                        (height + margin.top + 25) + ")")
    .style("text-anchor", "middle")
    .text("In Poverty (%)");
  svg.append("text")
    .attr("transform", "rotate(-90)")
    .attr("y", 10 - margin.left)
    .attr("x",0 - (height / 2))
    .attr("dy", "1em")
    .style("text-anchor", "middle")
    .text("Lacks Healthcare (%)");
  svg.append("text")
    .attr("dx", function(d) {return -20})
    .text(function(d) {return d.abbr})
});
