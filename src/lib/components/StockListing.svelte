<script lang="ts">
	import { createEventDispatcher } from 'svelte';

	export let company: string;
	export let stock_name: string;
	export let ESG_ranking: number;
	export let price_BUY: number;
	export let investment: boolean;
	export let selected: boolean | unknown;

	const dispatch = createEventDispatcher();

	function handleClick() {
		selected = true;
		const data = { company, price_BUY, ESG_ranking, selected };
		dispatch('click', data);
	}
</script>

{#if selected}
	<button class="grid grid-cols-5 p-2 bg-accent bg-opacity-20" on:click={handleClick}>
		<div class="flex flex-col col-span-1 text-left w-full">
			<div class="text-lg">{company}</div>
			<div class="p-0.5 text-sm">{stock_name}</div>
		</div>
		{#if investment === true}
			<div class="flex items-center justify-center text-green-900 font-bold col-span-2">GOOD</div>
		{:else}
			<div class="flex items-center justify-center text-red-900 font-bold col-span-2">BAD</div>
		{/if}
		<div class="flex flex-col col-span-2 text-left">
			<div class="flex gap-2">
				<div>
					<div class="font-bold text-lg">ESG:&nbsp;</div>
				</div>
				<div class="text-lg">{ESG_ranking}</div>
			</div>
			<div class="text-sm">${price_BUY}</div>
		</div>
	</button>
{:else}
	<button class="grid grid-cols-5 p-2 hover:bg-accent hover:bg-opacity-20" on:click={handleClick}>
		<div class="flex flex-col col-span-1 text-left">
			<div class="text-lg">{company}</div>
			<div class="p-0.5 text-sm">{stock_name}</div>
		</div>
		{#if investment === true}
			<div class="flex items-center justify-center text-green-900 font-bold col-span-2">GOOD</div>
		{:else}
			<div class="flex items-center justify-center text-red-900 font-bold col-span-2">BAD</div>
		{/if}
		<div class="flex flex-col col-span-2 text-left">
			<div class="flex gap-2">
				<div>
					<div class="font-bold text-lg">ESG:&nbsp;</div>
				</div>
				<div class="text-lg">{ESG_ranking}</div>
			</div>
			<div class="text-sm">${price_BUY}</div>
		</div>
	</button>
{/if}
