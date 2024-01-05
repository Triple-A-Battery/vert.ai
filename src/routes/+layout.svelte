<script>
	import '../app.css';
	import Navbar from '$lib/components/Navbar.svelte';
</script>

<div class="flex flex-col bg-accent bg-opacity-15">
	<Navbar />
	<slot />
</div>
