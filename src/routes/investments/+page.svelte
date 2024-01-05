<script lang="ts">
	import StockListing from '$lib/components/StockListing.svelte';

	export let data;

	let listings = data.STOCKS;

	let selectedName = listings[0].company;
	let selectedPrice = listings[0].open;
	let selectedESG = listings[0].esg_rating;

	function handleStock(event) {
		listings[listings.findIndex((obj) => obj.company === selectedName)].selected = false;
		selectedName = event.detail.company;
		selectedPrice = event.detail.price_BUY;
		selectedESG = event.detail.ESG_ranking;
		listings[listings.findIndex((obj) => obj.company === selectedName)].selected = true;
	}
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

			<div class="border-2 border-primary bg-accent bg-opacity-15 rounded-xl h-96"></div>

			<div class="grid grid-cols-2 gap-2">
				<div class="flex flex-col gap-2">
					<div
						class="bg-accent bg-opacity-15 border-2 border-primary rounded-xl h-10 flex justify-between text-lg font-semibold p-1"
					></div>
					<div
						class="bg-accent bg-opacity-15 border-2 border-primary rounded-xl h-full flex justify-between text-lg font-semibold p-1"
					></div>
				</div>
				<div class="flex flex-col gap-2">
					<div
						class="bg-accent bg-opacity-15 border-2 border-primary rounded-xl h-10 flex justify-between text-lg font-semibold p-1"
					></div>
					<div
						class="bg-accent bg-opacity-15 border-2 border-primary rounded-xl h-full flex justify-between text-lg font-semibold p-1"
					></div>
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
						selected={listing.selected}
					/>
					<div class="border-t-2 border-primary border-opacity-15"></div>
				{/each}
			</div>
		</div>
	</div>
</div>