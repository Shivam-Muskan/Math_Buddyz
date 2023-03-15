<script>
	import Header from '$lib/Components/Header.svelte';
	import API from '$lib/utils/api';
	import toast from 'svelte-french-toast';
	import { fade } from 'svelte/transition';

	const CNSCalculator = {
		binary: {
			disabled: false,
			name: 'Binary Number'
		},
		decimal: {
			disabled: false,
			name: 'Decimal Number'
		},
		octal: {
			disabled: true,
			name: 'Octal Number'
		},
		hexadecimal: {
			disabled: true,
			name: 'Hexadecimal Number'
		}
	};

	const allKeysCalc = Object.keys(CNSCalculator);
	const randomKey = (excludeKey) => {
		let randomIndex;
		do {
			randomIndex = Math.floor(Math.random() * allKeysCalc.length);
		} while (allKeysCalc[randomIndex] === excludeKey);
		return allKeysCalc[randomIndex];
	};

	const selections = {
		inputValue: 0,
		previousInputValue: null,
		answerValue: null,
		error: null,
		disableCalc: false,
		from: 'binary',
		to: 'decimal'
	};
	const openDropDown = {
		from: false,
		to: false
	};

	async function handleCalculations() {
		selections.error = null;
		selections.answerValue = null;
		selections.disableCalc = true;
		selections.previousInputValue = selections.inputValue;
		let response;
		try {
			response = await API.post(
				`/${selections['from']}_to_${selections['to']}/?num=${selections.previousInputValue}`,
				{}
			);
		} catch (e) {
			selections.disableCalc = false;
			toast.error(
				`Unable to complete your request for conversion ${
					CNSCalculator[selections['from']].name
				} to ${CNSCalculator[selections['to']].name}`
			);
			return;
		}
		if (response.error) {
			selections.disableCalc = false;
			selections.answerValue = null;
			selections.error = response.message;
			toast.error(response.message);
			return;
		}
		selections.answerValue = response.result;
		selections.disableCalc = false;
		toast.success(`Now you can see answer on screen.`);
		return;
	}
</script>

<Header heading="Binary Calculator" />

<section id="binaryCalculator" class="py-5 px-2">
	<div class="mx-auto grid max-w-7xl justify-items-center space-y-4">
		<div class="form-control">
			<label
				class="input-group grid flex-wrap items-center justify-center justify-between space-y-2 md:flex md:space-y-0"
			>
				<div class="dropdown">
					<button tabindex="0" class="btn md:rounded-r-none"
						>From: {CNSCalculator[selections['from']].name}</button
					>
					<ul
						tabindex="0"
						class="dropdown-content menu rounded-box mt-1 w-52 bg-gray-200 px-1.5 py-3 shadow"
					>
						{#each allKeysCalc as calc}
							<button
								disabled={selections.disableCalc}
								class="rounded-box p-2 text-start {selections['from'] === calc
									? 'bg-gray-400'
									: ''}"
								on:click={() => {
									selections['from'] = calc;
									if (selections['from'] === selections['to']) {
										selections['to'] = randomKey(calc);
									}
								}}>{CNSCalculator[calc].name}</button
							>
						{/each}
					</ul>
				</div>
				<input
					bind:value={selections['inputValue']}
					type="text"
					placeholder="e.g. 10, 1001, 4A"
					class="rounded-lg px-2 py-2 text-gray-100 md:input"
				/>
				<div class="dropdown dropdown-bottom dropdown-end">
					<label tabindex="0" class="btn md:rounded-l-none"
						>To: {CNSCalculator[selections['to']].name}</label
					>
					<ul
						tabindex="0"
						class="dropdown-content menu rounded-box mt-1 w-52 bg-gray-200 px-1.5 py-3 shadow"
					>
						{#each allKeysCalc as calc}
							{#if calc !== selections['from']}
								<button
									disabled={selections.disableCalc}
									class="rounded-box p-2 text-end {selections['to'] === calc ? 'bg-gray-400' : ''}"
									on:click={() => {
										selections['to'] = calc;
									}}>{CNSCalculator[calc].name}</button
								>
							{/if}
						{/each}
					</ul>
				</div>
			</label>
		</div>
		<button
			class="btn mt-4"
			on:click={() => {
				handleCalculations();
			}}
			>Convert {CNSCalculator[selections['from']].name} to {CNSCalculator[selections['to']]
				.name}</button
		>
		{#if selections.answerValue !== null}
			<div class="alert alert-success shadow-lg" transition:fade>
				<div>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-6 w-6 flex-shrink-0 stroke-current"
						fill="none"
						viewBox="0 0 24 24"
						><path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
						/></svg
					>
					<span
						>From {CNSCalculator[selections['from']].name} to {CNSCalculator[selections['to']].name}
						of {selections.previousInputValue} is {selections.answerValue}
					</span>
				</div>
			</div>
		{/if}

		{#if selections.error !== null}
			<div class="alert alert-error shadow-lg" transition:fade>
				<div>
					<svg
						xmlns="http://www.w3.org/2000/svg"
						class="h-6 w-6 flex-shrink-0 stroke-current"
						fill="none"
						viewBox="0 0 24 24"
						><path
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
						/></svg
					>
					<span>{selections.error}</span>
				</div>
			</div>
		{/if}
	</div>
</section>
