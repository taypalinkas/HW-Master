d3.json("samples.json").then((bb_data) => {
	// console.log(bb_data)
	var otus = bb_data.otu_ids;
	console.log(otus)
});