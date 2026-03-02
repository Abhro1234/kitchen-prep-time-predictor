let chart;

let labels = [];

let dataPoints = [];

function initChart() {

const ctx = document.getElementById('prepChart').getContext('2d');

chart = new Chart(ctx, {

type: 'line',

data: {

labels: labels,

datasets: [{

label: 'Prep Time',

data: dataPoints,

borderColor: '#e23744',

backgroundColor: 'rgba(226,55,68,0.2)',

borderWidth: 3,

tension: 0.3,

fill: true

}]

},

options: {

responsive: true

}

});

}

async function predict() {

const data = {

orders_in_queue: parseInt(document.getElementById("orders").value),

avg_prep_time: parseFloat(document.getElementById("prep").value),

peak_hour: document.getElementById("peak").value === "true",

weekend: document.getElementById("weekend").value === "true"

};

const res = await fetch("/predict", {

method: "POST",

headers: {

"Content-Type": "application/json"

},

body: JSON.stringify(data)

});

const result = await res.json();

document.getElementById("prepTime").innerText = result.prep_time + " mins";

document.getElementById("kitchenLoad").innerText = result.kitchen_load;

document.getElementById("confidence").innerText = result.confidence + "%";

updateChart(result.prep_time);

}

function updateChart(value) {

labels.push(new Date().toLocaleTimeString());

dataPoints.push(value);

if(labels.length > 10){

labels.shift();

dataPoints.shift();

}

chart.update();

}

window.onload = initChart;