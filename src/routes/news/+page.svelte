<script lang="ts">
	import { onMount } from 'svelte';

	let loading = true;
	let news = [];

	onMount(async () => {
		news = await (await fetch('http://na.tripe.one:7777/news')).json();
		loading = false;
	});
</script>

<span class="loading loading-spinner loading-md"></span>
<div class="mt-14 mx-[20%]">
	<div class="p-4 text-lg font-semibold text-center">
		Discover a selection of eco-conscious charities committed to environmental care and sustainable
		development scraped from all over the internet. Explore their missions, projects, and contribute
		to building a greener, healthier planet.
	</div>
	{#each news as c}
		<div class="p-2">
			<div
				class="bg-accent bg-opacity-15 p-4 flex flex-col rounded-2xl border-primary border-2 relative"
			>
				<div class="text-2xl font-semibold">{c.title}</div>
				<div>{c.description}</div>
				<div
					class="mt-2 bg-accent bg-opacity-25 border-2 border-primary w-fit p-2 rounded-xl text-sm font-semibold hover:scale-105 ml-auto"
				>
					<a href={c.url}>Read More</a>
				</div>
			</div>
		</div>
	{/each}
</div>
