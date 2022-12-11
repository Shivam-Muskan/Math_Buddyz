<script>
	import '../app.css';
	import Navigation from '$lib/Components/Navigation.svelte';
	import { Toaster } from 'svelte-french-toast';
</script>

<div class="min-h-screen max-w-[100vw] bg-gray-100">
	<Toaster />
	<Navigation />
	<slot />
</div>
