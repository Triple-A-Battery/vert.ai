<script lang="ts">
	export let company: string;
	export let amount: number;
	export let ESG_ranking: number;
	export let price_BUY: number;
	export let investment: string;

	export let selected: boolean = false;
</script>

{#if selected}
	<div class="grid grid-cols-5 p-2 bg-accent bg-opacity-20">
		<div class="flex flex-col col-span-1">
			<div class="text-lg">{company}</div>
			<div class="flex">
				<div class="p-0.5 font-semibold text-sm">amount:</div>
				<div class="p-0.5 text-sm">{amount}</div>
			</div>
		</div>
		{#if investment === 'GOOD'}
			<div class="flex items-center justify-center text-green-900 font-bold col-span-2">GOOD</div>
		{:else}
			<div class="flex items-center justify-center text-red-900 font-bold col-span-2">BAD</div>
		{/if}
		<div class="flex flex-col col-span-2">
			<div class="flex">
				<div>
					<div class="font-bold text-lg">ESG:&nbsp;</div>
				</div>
				<div class="text-lg">{ESG_ranking}</div>
			</div>
			<div class="text-sm">${price_BUY}</div>
		</div>
	</div>
{:else}
	<div class="grid grid-cols-5 p-2 hover:bg-accent hover:bg-opacity-20">
		<div class="flex flex-col col-span-1">
			<div class="text-lg">{company}</div>
			<div class="flex">
				<div class="p-0.5 font-semibold text-sm">amount:</div>
				<div class="p-0.5 text-sm">{amount}</div>
			</div>
		</div>
		{#if investment === 'GOOD'}
			<div class="flex items-center justify-center text-green-900 font-bold col-span-2">GOOD</div>
		{:else}
			<div class="flex items-center justify-center text-red-900 font-bold col-span-2">BAD</div>
		{/if}
		<div class="flex flex-col col-span-2">
			<div class="flex">
				<div>
					<div class="font-bold text-lg">ESG:&nbsp;</div>
				</div>
				<div class="text-lg">{ESG_ranking}</div>
			</div>
			<div class="text-sm">${price_BUY}</div>
		</div>
	</div>
{/if}
