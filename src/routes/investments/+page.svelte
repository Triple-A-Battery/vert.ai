<script lang="ts">
	import StockListing from '$lib/components/StockListing.svelte';

	let listings = [
		{
			company: 'BBY',
			amount: 100,
			price_BUY: 55.5518035889,
			investment: 'BAD',
			ESG_ranking: 12.0
		},
		{
			company: 'BAC',
			amount: 15000,
			price_BUY: 18.6167488098,
			investment: 'GOOD',
			ESG_ranking: 26.3
		},
		{
			company: 'AXP',
			amount: 3000,
			price_BUY: 59.8622970581,
			investment: 'BAD',
			ESG_ranking: 19.8
		},
		{
			company: 'KSS',
			amount: 20000,
			price_BUY: 38.2167243958,
			investment: 'BAD',
			ESG_ranking: 6.0
		},
		{
			company: 'AAPL',
			amount: 500,
			price_BUY: 120.5518035889,
			investment: 'GOOD',
			ESG_ranking: 32.5
		},
		{
			company: 'GOOGL',
			amount: 800,
			price_BUY: 2800.6167488098,
			investment: 'GOOD',
			ESG_ranking: 45.2
		},
		{
			company: 'TSLA',
			amount: 300,
			price_BUY: 900.8622970581,
			investment: 'BAD',
			ESG_ranking: 15.7
		},
		{
			company: 'AMZN',
			amount: 1200,
			price_BUY: 3200.2167243958,
			investment: 'GOOD',
			ESG_ranking: 40.9
		},

		{
			company: 'BBY',
			amount: 100,
			price_BUY: 55.5518035889,
			investment: 'BAD',
			ESG_ranking: 12.0
		},
		{
			company: 'BAC',
			amount: 15000,
			price_BUY: 18.6167488098,
			investment: 'GOOD',
			ESG_ranking: 26.3
		},
		{
			company: 'AXP',
			amount: 3000,
			price_BUY: 59.8622970581,
			investment: 'BAD',
			ESG_ranking: 19.8
		},
		{
			company: 'KSS',
			amount: 20000,
			price_BUY: 38.2167243958,
			investment: 'BAD',
			ESG_ranking: 6.0
		}
	];
</script>

<div class="mt-14">
	<div class="grid grid-cols-8 h-[93.2vh]">
		<!-- main stuff -->
		<div class="col-span-6 p-3 flex flex-col gap-2">
			<div
				class="bg-accent bg-opacity-15 border-2 border-primary rounded-xl h-11 flex justify-between text-lg font-semibold p-1"
			>
				<div class="ml-4 mt-0.5">Name</div>
				<div class="flex gap-4 mr-4 mt-0.5">
					<div>Price</div>
					<div>gre</div>
				</div>
			</div>

			<div class="border-2 border-primary bg-accent bg-opacity-15 rounded-xl h-96"></div>

			<div class="grid grid-cols-2 gap-2">
				<div class="flex flex-col gap-2">
					<div
						class="bg-accent bg-opacity-15 border-2 border-primary rounded-xl h-10 flex justify-between text-lg font-semibold p-1"
					></div>
					<div
						class="bg-accent bg-opacity-15 border-2 border-primary rounded-xl h-[16.7rem] flex justify-between text-lg font-semibold p-1"
					></div>
				</div>
				<div class="flex flex-col gap-2">
					<div
						class="bg-accent bg-opacity-15 border-2 border-primary rounded-xl h-10 flex justify-between text-lg font-semibold p-1"
					></div>
					<div
						class="bg-accent bg-opacity-15 border-2 border-primary rounded-xl h-[16.7rem] flex justify-between text-lg font-semibold p-1"
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
						company={listing.company}
						amount={listing.amount}
						ESG_ranking={listing.ESG_ranking}
						price_BUY={listing.price_BUY}
						investment={listing.investment}
					/>
					<div class="border-t-2 border-primary border-opacity-15"></div>
				{/each}
			</div>
		</div>
	</div>
</div>
