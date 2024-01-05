<script lang="ts">
	import StockListing from '$lib/components/StockListing.svelte';
	import Chart from 'chart.js/auto';
	import { onMount } from 'svelte';
	import Radial from '$lib/components/Radial.svelte';

	export let data;

	let history = data.HISTORY;

	const listings = data.STOCKS.filter((obj1) =>
		history.some((obj2) => obj2.company === obj1.company)
	);

	let selectedName = listings[0].company;
	let selectedPrice = listings[0].open;
	let selectedESG = listings[0].esg_rating;
	let selectedTicker = history.filter((obj) => obj.company === selectedName)[0].ticker;
	let tickerData = {};

	listings[0].selected = true;

	let chart; // Variable to hold the chart instance

	const getTickerData = async (ticker) => {
		try {
			const response = await fetch(`http://na.tripe.one:7777/fetch_info/${ticker}`, {
				headers: {
					accept: 'application/json'
				}
			});
			if (!response.ok) {
				throw new Error('Network response was not ok');
			}
			return response.json();
		} catch (error) {
			console.error('Fetch error:', error);
			return [];
		}
	};

	async function updateChart(selectedCompany) {
		const filteredHistory = history.filter((item) => item.company === selectedCompany);
		tickerData = (await getTickerData(selectedTicker))[0];
		console.log(tickerData);

		UN = await (await fetch('http://na.tripe.one:7777/environment/' + tickerData.country)).json();

		if (chart) {
			chart.destroy(); // Destroy the previous chart instance
		}

		const graph = document.getElementById('graph');
		chart = new Chart(graph, {
			type: 'line',
			data: {
				labels: filteredHistory.map((item) => item.date), // Assuming 'date' is a property in history items
				datasets: [
					{
						label: `Price History: ${selectedName}`,
						data: filteredHistory.map((item) => item.open), // Replace 'price' with the correct property
						borderWidth: 2,
						backgroundColor: 'rgba(97, 80, 6, 0.2)',
						borderColor: 'rgba(97, 80, 6, 1)'
					}
				]
			},

			options: {
				maintainAspectRatio: false,
				responsive: true,
				onResize(chart, size) {},
				scales: {
					y: {
						ticks: {
							min: Math.min(...filteredHistory.map((item) => item.open)) - 10,
							max: Math.max(...filteredHistory.map((item) => item.open)) + 10,
							stepSize: 5
						}
					},
					x: {
						ticks: {
							min: 1,
							max: 14,
							stepSize: 1
						}
					}
				}
			}
		});
	}

	let currentListing = {};

	async function handleStock(event) {
		listings[listings.findIndex((obj) => obj.company === selectedName)].selected = false;
		selectedName = event.detail.company;
		selectedPrice = event.detail.price_BUY;
		selectedESG = event.detail.ESG_ranking;
		listings[listings.findIndex((obj) => obj.company === selectedName)].selected = true;
		selectedTicker = history.filter((obj) => obj.company === selectedName)[0].ticker;

		currentListing = event.detail;
		console.log(currentListing);

		tickerData = await getTickerData(selectedTicker);

		updateChart(selectedName); // Call to update the chart
	}

	let angle = 0;
	const maxAngle = 180;

	function updateAngle(event) {
		angle = event.target.value;
	}

	onMount(() => {
		updateChart(selectedName); // Initial chart rendering
	});

	let UN;
</script>

<div class="mt-14">
	<div class="grid grid-cols-8 h-[93.2vh]">
		<!-- main stuff -->
		<div class="col-span-6 p-3 flex flex-col gap-2">
			<div
				class="bg-accent bg-opacity-15 border-2 border-primary rounded-xl h-11 flex justify-between text-lg font-semibold p-1"
			>
				<div class="ml-4 mt-0.5">{selectedName}</div>
				<div class="flex gap-4 mr-4 mt-0.5">
					<div>${selectedPrice}</div>
					<div>ESG: {selectedESG}</div>
				</div>
			</div>

			<div class="border-2 border-primary bg-accent bg-opacity-15 rounded-xl">
				<div class="h-[40vh]">
					<canvas id="graph"></canvas>
				</div>
			</div>

			<div class="grid grid-cols-2 gap-2">
				<div class="flex flex-col gap-2">
					<div
						class="bg-accent bg-opacity-15 border-2 border-primary rounded-xl h-10 text-center text-xl font-bold p-2"
					>
						Information
					</div>
					<div
						class="bg-accent bg-opacity-15 border-2 border-primary rounded-xl h-full flex flex-col justify-between text-lg font-semibold p-4"
					>
						{#if tickerData}
							{#each Object.entries(tickerData) as [key, value]}
								<div class="flex flex-row justify-between">
									<p>{key}:</p>
									<p>{value}</p>
								</div>
							{/each}
						{/if}
					</div>
				</div>
				<div class="flex flex-col gap-2">
					<!-- <div -->
					<!-- 	class="bg-accent bg-opacity-15 border-2 border-primary rounded-xl h-10 flex justify-between text-lg font-semibold p-1" -->
					<!-- > -->
					<!-- 	 -->
					<!-- </div> -->
					<div
						class="bg-accent bg-opacity-15 border-2 border-primary rounded-xl h-full justify-center items-center text-lg font-semibold p-1"
					>
						<p>UN SDG rating</p>
						<div class="">
							<Radial progress={UN}></Radial>
						</div>

						<h2>{UN}</h2>
					</div>
					<div
						class="bg-accent bg-opacity-15 border-2 border-primary rounded-xl h-full flex flex-col justify-between text-lg font-semibold p-4"
					>
						{#if currentListing}
							{#each Object.entries(currentListing) as [key, value]}
								<div class="flex flex-row justify-between">
									<p>{key}:</p>
									<p>{value}</p>
								</div>
							{/each}
						{/if}
					</div>
				</div>
			</div>
		</div>

		<!-- right side stuff -->

		<div class="col-span-2 flex flex-col gap-2 h-[90vh] mt-3 mr-2">
			<div class="border-2 border-primary rounded-xl bg-accent bg-opacity-15">
				<div class="flex items-center rounded-full w-full bg-dark-text p-2">
					<div class="text-background mr-2">
						<i class="fa-solid fa-magnifying-glass"></i>
					</div>
					<div class="absolute bottom-0 left-0 gauge-background"></div>
					<input
						type="text"
						placeholder="Search stocks"
						class="rounded-full bg-transparent text-background w-full focus:outline-none"
					/>
				</div>
			</div>
			<div class="border-2 border-primary overflow-y-auto bg-accent bg-opacity-15 rounded-xl">
				{#each listings as listing}
					<StockListing
						on:click={handleStock}
						company={listing.company}
						stock_name={listing.stock_name}
						ESG_ranking={listing.esg_rating}
						price_BUY={listing.open}
						investment={listing.investment_check}
						peRatio={listing.pe_ratio}
						selected={listing.selected}
					/>
					<div class="border-t-2 border-primary border-opacity-15"></div>
				{/each}
			</div>
		</div>
	</div>
</div>

<style>
	.gauge-background {
		@apply rounded-full;
		background: conic-gradient(from 90deg at 50% 50%, red 0%, green 80%);
	}
</style>
