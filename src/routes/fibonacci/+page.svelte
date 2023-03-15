<script>
	import Header from '$lib/Components/Header.svelte';
	import API from '$lib/utils/api';
	import toast from 'svelte-french-toast';
	import { fade } from 'svelte/transition';

	const fibonacciCalc = {
		nth_fib: {
			name: 'Find nth fibonacci number',
			url: 'n_th_fibonacci/',
			inputValue: 0,
			answerValue: null,
			previousInputValue: null,
			error: null,
			disabled: false,
			returnInt: true,
			fixCount: true
		},
		calc_sum: {
			name: 'Find sum of first n fibonacci numbers',
			url: 'calculate_sum/',
			inputValue: 0,
			answerValue: null,
			previousInputValue: null,
			error: null,
			disabled: false,
			returnInt: true,
			fixCount: true
		},
		is_fib: {
			name: 'Find if number is fibonacci',
			url: 'is_fibonacci_number/',
			inputValue: 0,
			answerValue: null,
			previousInputValue: null,
			error: null,
			disabled: false,
			returnInt: false,
			fixCount: false
		},
		gen_fib: {
			name: 'Generate fibonacci series from 0',
			url: 'fibonacci_series/',
			inputValue: 0,
			answerValue: null,
			previousInputValue: null,
			error: null,
			disabled: false,
			returnInt: false,
			fixCount: true
		}
	};

	async function findWithIntReturn(key) {
		fibonacciCalc[key].answerValue = null;
		fibonacciCalc[key].error = null;
		fibonacciCalc[key].disabled = true;
		fibonacciCalc[key].previousInputValue = fibonacciCalc[key].inputValue;
		if (fibonacciCalc[key].inputValue !== 0 && fibonacciCalc[key].fixCount) {
			fibonacciCalc[key].previousInputValue = fibonacciCalc[key].inputValue - 1
		}

		let response;
		try {
			response = await API.post(
				`${fibonacciCalc[key].url}?num=${fibonacciCalc[key].previousInputValue}`,
				{}
			);
		} catch (e) {
			fibonacciCalc[key].disabled = false;
			fibonacciCalc[
				key
			].error = `We are unable to complete your request for ${fibonacciCalc[key].name}`;
			toast.error(`${fibonacciCalc[key].error}`);
			return;
		}
		if (response.error) {
			fibonacciCalc[key].disabled = false;
			fibonacciCalc[key].error = response.message;
			toast.error(`${fibonacciCalc[key].error}`);
			return;
		}
		fibonacciCalc[key].answerValue = `Answer is ${response.result}`;
		toast.success(`Look what we found for you on screen.`);
		fibonacciCalc[key].disabled = false;
		return;
	}
</script>

<Header heading="Fibonacci Calculator" />

<section id="binaryCalculator" class="py-5 px-2">
	<div
		class="mx-auto grid max-w-7xl grid-cols-1 justify-items-center space-y-4 md:grid-cols-2"
	>
		{#each Object.keys(fibonacciCalc) as key}
			<div class="form-control">
				<label class="label">
					<span class="label-text">{fibonacciCalc[key].name}</span>
				</label>
				<label class="input-group">
					<input
						bind:value={fibonacciCalc[key].inputValue}
						type="number"
						placeholder="0.01"
						class="input-bordered input text-white"
					/>
					<button
						class="btn"
						on:click={async () => {
							await findWithIntReturn(key);
						}}>Find</button
					>
				</label>
				{#if fibonacciCalc[key].answerValue !== null}
					<div class="alert alert-success shadow-lg mt-2 max-w-sm" transition:fade>
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
							<span>{fibonacciCalc[key].answerValue} </span>
						</div>
					</div>
				{/if}

				{#if fibonacciCalc[key].error !== null}
					<div class="alert alert-error shadow-lg mt-2 max-w-sm" transition:fade>
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
							<span>{fibonacciCalc[key].error}</span>
						</div>
					</div>
				{/if}
			</div>
		{/each}
	</div>
</section>
