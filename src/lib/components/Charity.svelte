<script lang="ts">
	export let name: string;
	export let description: string;
	export let link: string;
	export let progress: number;
</script>

<div class="p-2">
	<div
		class=" text-green-100 bg-opacity-15 p-4 flex flex-col rounded-2xl border-primary border-2 relative"
	>
		<div class="text-2xl font-semibold">{name}</div>
		<div>{description}</div>
		<div
			class="mt-2 bg-accent bg-opacity-25 border-2 border-primary w-fit p-2 rounded-xl text-sm font-semibold hover:scale-105 ml-auto"
		>
			<a href={link}>Read More</a>
		</div>
		<progress
			class="progress w-[75%] absolute h-full w-full top-0 left-0 z-[-1] bg-primary opacity-50"
			value={progress}
			max="100"
		></progress>
	</div>
</div>
