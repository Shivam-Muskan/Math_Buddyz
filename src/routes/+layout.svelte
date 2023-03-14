<script>
	import '../app.css';
	import Navigation from '$lib/Components/Navigation.svelte';
	import { Toaster } from 'svelte-french-toast';
</script>

<div
	class="min-h-screen scroll-smooth bg-gray-100 text-gray-900 selection:bg-gray-800 selection:text-gray-100"
>
	<Toaster />
	<Navigation />
	<slot />
</div>
