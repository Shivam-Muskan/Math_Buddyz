<script>
	import { createEventDispatcher } from 'svelte';
	import { onMount } from 'svelte';

	const dispatch = createEventDispatcher();
	export let isOpen = false;
	// by default Drawer opens from right. Make left-0 for left opening
	export let placement = 'right-0';
	// max size of content section
	export let maxScreenSize = 'max-w-xl';

	const handleClickAway = () => {
		dispatch('clickAway');
		isOpen = !isOpen;
	};

	let mounted = false;
	// scrolllock for content underneath drawer
	function scrollLock(isOpen) {
		if (mounted) {
			const body = document.querySelector('body');
			body.style.overflow = isOpen ? 'hidden' : 'auto';
		}
	}
	$: scrollLock(isOpen);

	onMount(() => {
		mounted = true;
		scrollLock(isOpen);
	});
</script>

<aside>
	<div class="fixed inset-0 z-50 h-full w-full overflow-hidden {isOpen ? 'visible' : 'invisible'}">
		<div
			class="h-full w-screen cursor-pointer overflow-hidden bg-gray-500 transition-opacity duration-500 {isOpen
				? 'opacity-50'
				: 'opacity-0'}"
			on:click={handleClickAway}
			role="presentation"
		/>
		<div
			class="absolute {placement} top-0 h-full overflow-y-auto rounded rounded-tl-lg bg-white pb-5 shadow-xl transition-all duration-500 ease-in-out {maxScreenSize} {isOpen
				? 'w-screen'
				: 'w-0'}"
		>
			<slot />
		</div>
	</div>
</aside>
