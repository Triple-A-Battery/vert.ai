<script lang="ts">
	import Charity from '$lib/components/Charity.svelte';
	import charities from './charities.json';
</script>

<div class="mt-14 mx-[20%]">
	<div class="p-4 text-lg font-semibold text-center">
		Discover a selection of eco-conscious charities committed to environmental care and sustainable
		development scraped from all over the internet. Explore their missions, projects, and contribute
		to building a greener, healthier planet.
	</div>
	{#each charities as charity}
		<Charity name={charity.name} description={charity.description} link={charity.link} />
	{/each}
</div>
