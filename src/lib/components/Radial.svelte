<script>
	export let progress = 0; // Progress value passed as a prop

	// Calculate the stroke properties
	const radius = 20; // Radius of the circle
	const circumference = 2 * Math.PI * radius;
	let strokeDashoffset = circumference - (progress / 100) * circumference;
	let strokeColor = progress > 40 ? 'green' : 'red';
</script>

<svg width="50" height="50">
	<circle
		class="progress-circle"
		stroke={strokeColor}
		stroke-width="5"
		fill="transparent"
		r={radius}
		cx="25"
		cy="25"
		stroke-dasharray={circumference}
		stroke-dashoffset={strokeDashoffset}
	/>
</svg>

<style>
	.progress-circle {
		transform: rotate(-90deg);
		transform-origin: 50% 50%;
		transition:
			stroke-dashoffset 0.6s ease,
			stroke 0.6s ease;
	}
</style>
