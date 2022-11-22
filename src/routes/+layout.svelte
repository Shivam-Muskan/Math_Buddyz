<script>
	import '../app.css';
	import Navbar from '$lib/Navbar.svelte';
</script>

<div class="bg-gray-100">
	<Navbar />
	<slot />
</div>
