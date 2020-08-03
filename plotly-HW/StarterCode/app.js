d3.json("samples.json").then((bb_data) => {
	console.log(bb_data)
	var sv = bb_data.samples[0].sample_values
	console.log(sv)
	var topten = sv.slice(0, 10)
	console.log(topten)
	var id = bb_data.samples[0].otu_ids
	var ids = id.slice(0, 10)
	console.log(ids)
	var label = bb_data.samples[0].otu_labels
	var labels = label.slice(0,10)
	console.log(labels);
	// bb_data.names.forEach(function(name) {
	// 	dropdown.append("option").text(name).property("value");
	// });
	// getPlots(bb_data.names[0]);
	// getDemoInfo(data.names[0]);


	var trace1 = {
		x: topten,
		y: ids,
		text: labels,
		type: "bar",
		orientation: "h",

	};
	var data1 = [trace1];

	var layout1 = {
		title: "Top 10 OTU",
		xaxis: {title: "OTU Count"},
		yaxis: {title: "OTU IDs"}
	};

	Plotly.newPlot("bar", data1, layout1);

	var trace2 = {
		x: id,
		y: sv,
		mode: 'markers',
		marker: {
			color: ids,
			size: sv,
		}
	};
	var data2 = [trace2];

	var layout2 = {
		title: "All OTU's",
		xaxis: {title: "OTU IDs"},
		yaxis: {title: "OTU Count"}
	};

	Plotly.newPlot("bubble", data2, layout2);
});

// function enterSample() {
// 	var newSample = d3.select("#selDataset")
