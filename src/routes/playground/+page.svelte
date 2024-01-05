<script lang="ts">
	import { Chart } from 'chart.js/auto';
	import { onMount } from 'svelte';

	let formData = {
		price: '',
		high: '',
		low: '',
		volume: ''
	};

	function handleChange(event, field) {
		formData[field] = event.target.value.replace(/[^0-9]/g, '');
	}

	const getFuture = async (graphOpen, graphHigh, graphLow, graphVol) => {
		try {
			const response = await fetch(
				`http://na.tripe.one:7777/future?open=${graphOpen}&high=${graphHigh}&low=${graphLow}&volume=${graphVol}&days=14`,
				{
					headers: {
						accept: 'application/json'
					}
				}
			);
			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
			return response.json();
		} catch (error) {
			console.error('Fetch error:', error);
			return [];
		}
	};

	let graphContext;
	let chart;

	async function makeGraph() {
		let prediction = await getFuture(formData.price, formData.high, formData.low, formData.volume);
		console.log(prediction);

		if (chart) {
			chart.destroy();
		}

		chart = new Chart(graphContext, {
			type: 'line',
			data: {
				labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
				datasets: [
					{
						label: 'Price Prediction',
						data: prediction,
						borderWidth: 2,
						backgroundColor: 'rgba(97, 80, 6, 0.2)',
						borderColor: 'rgba(97, 80, 6, 1)'
					}
				]
			},
			options: {
				maintainAspectRatio: false,
				responsive: true,
				scales: {
					y: {
						beginAtZero: true,
						ticks: {
							// Auto-calculate min and max
							autoSkip: true
						}
					},
					x: {
						beginAtZero: true,
						ticks: {
							autoSkip: true
						}
					}
				}
			}
		});
	}

	onMount(() => {
		graphContext = document.getElementById('predict-graph').getContext('2d');
	});
</script>

<div class="grid grid-cols-8 mt-14 h-[93.2vh]">
	<div class="col-span-6 p-3">
		<div class="border-2 border-primary bg-accent bg-opacity-15 rounded-xl">
			<div class="h-[90vh]">
				<canvas id="predict-graph"></canvas>
			</div>
		</div>
	</div>
	<div class="col-span-2">
		<div class="flex flex-col gap-2 p-3 mt-[13rem]">
			<div
				class="bg-accent bg-opacity-15 border-2 border-primary rounded-xl h-10 flex font-semibold p-1"
			>
				<div class="text-center w-full text-xl font-semibold">Tweak Some Values</div>
			</div>
			<div
				class="bg-accent bg-opacity-15 border-2 border-primary rounded-xl h-full flex flex-col gap-4 text-lg font-semibold p-2"
			>
				<div class="flex justify-between">
					<div class="text-md font-semibold p-1">Price</div>
					<input
						name="price"
						type="text"
						placeholder="enter a number"
						bind:value={formData.price}
						on:input={(e) => handleChange(e, 'price')}
						class="rounded-xl bg-transparent text-background w-fit focus:outline-none border-2 border-primary p-1 text-sm"
					/>
				</div>
				<div class="flex justify-between">
					<div class="text-md font-semibold p-1">High</div>
					<input
						name="high"
						type="text"
						placeholder="enter a number"
						bind:value={formData.high}
						on:input={(e) => handleChange(e, 'high')}
						class="rounded-xl bg-transparent text-background w-fit focus:outline-none border-2 border-primary p-1 text-sm"
					/>
				</div>
				<div class="flex justify-between">
					<div class="text-md font-semibold p-1">Low</div>
					<input
						name="low"
						type="text"
						placeholder="enter a number"
						bind:value={formData.low}
						on:input={(e) => handleChange(e, 'low')}
						class="rounded-xl bg-transparent text-background w-fit focus:outline-none border-2 border-primary p-1 text-sm"
					/>
				</div>
				<div class="flex justify-between">
					<div class="text-md font-semibold p-1">Volume</div>
					<input
						name="volume"
						type="text"
						placeholder="enter a number"
						bind:value={formData.volume}
						on:input={(e) => handleChange(e, 'volume')}
						class="rounded-xl bg-transparent text-background w-fit focus:outline-none border-2 border-primary p-1 text-sm"
					/>
				</div>
				<div class="w-full flex justify-center self-center">
					<button
						class="bg-accent bg-opacity-25 border-2 border-primary rounded-lg p-1 text-sm w-fit"
						on:click={makeGraph}>submit</button
					>
				</div>
			</div>
		</div>
	</div>
</div>
