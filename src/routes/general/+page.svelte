<script>
	import toast from 'svelte-french-toast';
	import { parse, compile, evaluate } from 'mathjs';

	const calcPad = {
		rowOne: ['AC', 'C', '🔙', '/'],
		rowTwo: [1, 2, 3, '*'],
		rowThree: [4, 5, 6, '-'],
		rowFour: [7, 8, 9, '+']
	};
	const specialReplacement = {
		'/': '÷',
		'*': 'x'
	};
	const specialValues = ['%', '/', '*', '-', '+', '.'];
	let currentValues = '';
	let calculated = 0;

	const updateCurrentValues = async (item) => {
		if (item === '🔙') return (currentValues = currentValues.slice(0, -1)), await calculateValue();

		if (item === 'C') return (calculated = 0);
		if (item === 'AC') return (currentValues = ''), (calculated = 0);
		currentValues = currentValues + item.toString();
		return await calculateValue();
	};

	const calculateValue = async () => {
		if (specialValues.some((value) => currentValues.endsWith(value))) return;
		if (specialValues.some((value) => currentValues.startsWith(value)))
			return toast.error('Please check your input');
		if (currentValues === '') return (calculated = 0);
		try {
			const parsedValues = parse(currentValues);
			const compiledValues = parsedValues.compile();
			calculated = compiledValues.evaluate();
		} catch (e) {
			console.log(e);
		}
	};
</script>

<div class="min-w-screen flex max-h-screen items-center justify-center bg-gray-100 pt-32">
	<div
		class="relative mx-auto w-full overflow-hidden rounded-xl bg-gray-100 text-gray-800 shadow-xl"
		style="max-width:300px"
	>
		<div
			class="flex h-40 w-full flex-col items-end bg-gradient-to-b from-gray-800 to-gray-700 text-right"
		>
			<div class="w-full py-5 px-6 text-sm font-thin text-white">{currentValues}</div>
			<div class="w-full py-5 px-6 text-6xl font-thin text-white">{calculated}</div>
		</div>
		<div class="w-full bg-gradient-to-b from-amber-400 to-amber-500">
			{#each Object.keys(calcPad) as row}
				<div class="flex w-full">
					{#each calcPad[row] as item}
						<div class="w-1/4 border-r border-b border-amber-400">
							<button
								on:click={async () => {
									await updateCurrentValues(item);
								}}
								class="h-16 w-full text-xl font-light text-white text-opacity-50 outline-none hover:bg-amber-700 hover:bg-opacity-20 focus:outline-none"
							>
								{#if Object.keys(specialReplacement).includes(item)}
									{specialReplacement[item]}
								{:else}
									{item}
								{/if}
							</button>
						</div>
					{/each}
				</div>
			{/each}
			<div class="flex w-full">
				<div class="w-1/4 border-r border-amber-400">
					<button
						on:click={async () => {
							await updateCurrentValues('0');
						}}
						class="h-16 w-full text-xl font-light text-white outline-none hover:bg-amber-700 hover:bg-opacity-20 focus:outline-none"
						>0</button
					>
				</div>
				<div class="w-1/4 border-r border-amber-400">
					<button
						on:click={async () => {
							await updateCurrentValues('.');
						}}
						class="h-16 w-full text-xl font-light text-white outline-none hover:bg-amber-700 hover:bg-opacity-20 focus:outline-none"
						>.</button
					>
				</div>
				<div class="w-2/4 border-r border-amber-400">
					<button
						on:click={calculateValue}
						class="h-16 w-full bg-amber-700 bg-opacity-30 text-xl font-light text-white outline-none hover:bg-opacity-40 focus:outline-none"
						>=</button
					>
				</div>
			</div>
		</div>
	</div>
</div>

<style>
	@import url(https://cdnjs.cloudflare.com/ajax/libs/MaterialDesign-Webfont/5.3.45/css/materialdesignicons.min.css);
</style>
