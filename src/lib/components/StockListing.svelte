<script lang="ts">
	import { createEventDispatcher } from 'svelte';

	export let company: string;
	export let stock_name: string;
	export let ESG_ranking: number;
	export let price_BUY: number;
	export let investment: boolean;
	export let peRatio: number;
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
		<div class="flex items-center justify-center font-bold col-span-2">{peRatio}</div>
		<div class="flex flex-col col-span-2 text-left">
			<div class="flex gap-2">
				{#if investment === true}
					<div class="text-green-900">
						<div class="font-bold text-lg">ESG:&nbsp;</div>
					</div>
					<div class="text-lg text-green-900">{ESG_ranking}</div>
				{:else}
					<div>
						<div class="font-bold text-lg text-red-900">ESG:&nbsp;</div>
					</div>
					<div class="text-lg text-red-900">{ESG_ranking}</div>
				{/if}
			</div>
			<div class="text-sm">${price_BUY}</div>
		</div>
	</button>
{:else}
	<button class="grid grid-cols-5 p-2 hover:bg-accent hover:bg-opacity-20" on:click={handleClick}>
		<div class="flex flex-col col-span-1 text-left w-full">
			<div class="text-lg">{company}</div>
			<div class="p-0.5 text-sm">{stock_name}</div>
		</div>
		<div class="flex items-center justify-center font-bold col-span-2">{peRatio}</div>
		<div class="flex flex-col col-span-2 text-left">
			<div class="flex gap-2">
				{#if investment === true}
					<div class="text-green-900">
						<div class="font-bold text-lg">ESG:&nbsp;</div>
					</div>
					<div class="text-lg text-green-900">{ESG_ranking}</div>
				{:else}
					<div>
						<div class="font-bold text-lg text-red-900">ESG:&nbsp;</div>
					</div>
					<div class="text-lg text-red-900">{ESG_ranking}</div>
				{/if}
			</div>
			<div class="text-sm">${price_BUY}</div>
		</div>
	</button>
{/if}
