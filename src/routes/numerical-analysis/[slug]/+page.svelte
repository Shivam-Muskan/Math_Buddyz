<script>
	import { page } from '$app/stores';
	import { PUBLIC_BASE_API } from '$env/static/public';
	import Header from '$lib/Components/Header.svelte';
	import API from '$lib/utils/api';
	import toast from 'svelte-french-toast';

	let answers = null;
	const numericalMethodsCalc = {
		'bisection-method': {
			url: 'bisection_method/',
			name: 'Bisection Method',
			fields: [
				{ name: 'Polynomial Equation', key: 'p', inputValue: 'x**3-5*x-9' },
				{ name: 'Lower Limit', key: 'a', inputValue: 2 },
				{ name: 'Upper Limit', key: 'b', inputValue: 3 },
				{ name: 'No. of Iterations', key: 'n', inputValue: 1 }
			]
		},
		'regula-falsi-method': {
			url: 'regula_falsi/',
			name: 'Regula-Falsi Method',
			fields: [
				{ name: 'Polynomial Equation', key: 'p', inputValue: 'x**3-5*x-9' },
				{ name: 'Lower Limit', key: 'a', inputValue: 2 },
				{ name: 'Upper Limit', key: 'b', inputValue: 3 },
				{ name: 'No. of Iterations', key: 'n', inputValue: 1 }
			]
		},
		'newton-raphson-method': {
			url: 'newton_raphson/',
			name: 'Newton-Raphson Method',
			fields: [
				{ name: 'Polynomial Equation', key: 'p', inputValue: 'x**3-5*x-9' },
				{ name: 'Value for x0', key: 'x0', inputValue: 2 },
				{ name: 'No. of Iterations', key: 'n', inputValue: 1 }
			]
		},
		'secant-method': {
			url: 'secant/',
			name: 'Secant Method',
			fields: [
				{ name: 'Polynomial Equation', key: 'p', inputValue: 'x**3-5*x-9' },
				{ name: 'Lower Limit', key: 'a', inputValue: 2 },
				{ name: 'Upper Limit', key: 'b', inputValue: 3 },
				{ name: 'No. of Iterations', key: 'n', inputValue: 1 }
			]
		},
		'fixed-point-iteration-method': {
			url: 'fixed_point_iteration/',
			name: 'Fixed Point Iteration Method',
			fields: [
				{ name: 'Polynomial Equation', key: 'p', inputValue: 'cbrt((2*x + 5)/2)' },
				{ name: 'Value for x0', key: 'x0', inputValue: 1.5 },
				{ name: 'No. of Iterations', key: 'n', inputValue: 1 }
			]
		}
	};

	const handleCalculation = async () => {
		answers = null;
		const url = new URL(numericalMethodsCalc[$page.params.slug].url, PUBLIC_BASE_API);
		const params = url.searchParams;
		numericalMethodsCalc[$page.params.slug].fields.forEach((field) => {
			params.set(field.key, field.inputValue);
		});
		url.search = params.toString();
		let response;
		try {
			response = await API.post(url.toString(), {});
		} catch (e) {
			console.log(e);
			toast.error('Unable to complete your request.');
			return;
		}
		if (response.error) {
			toast.error(response.message);
			return;
		}
		answers = response.roots;
		toast.success(response.message);
		return;
	};
</script>

<Header heading={numericalMethodsCalc[$page.params.slug].name} />

<section id="binaryCalculator" class="bg-gray-100 py-5 px-2">
	<div class="mx-auto flex max-w-7xl flex-col justify-items-center space-y-4">
		<div class="mx-auto">
			<div class="space-y-5">
				{#each numericalMethodsCalc[$page.params.slug].fields as field}
					<div class="grid grid-cols-3 items-center space-x-2">
						<label for={field.key} class="col-span-1 block text-sm font-medium text-gray-700"
							>{field.name}</label
						>
						<div class="col-span-2">
							<input
								bind:value={field.inputValue}
								type="text"
								id={field.key}
								class="my-3 rounded px-2 py-1 text-gray-50"
							/>
						</div>
					</div>
				{/each}
			</div>
		</div>
	</div>
	<div class="flex flex-col">
		<div class="mx-auto mt-5">
			<button
				on:click={async () => handleCalculation()}
				type="button"
				class="items-center rounded-md border border-transparent bg-indigo-600 px-6 py-3 text-sm font-semibold leading-5 text-white transition-all duration-200 hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-600 focus:ring-offset-2"
				>Calculate using {numericalMethodsCalc[$page.params.slug].name}</button
			>
		</div>
	</div>

	{#if answers !== null}
		<div class="mx-auto mt-5 max-w-xl px-4 py-2">
			<div class="flex rounded-md bg-green-50 p-4 text-sm text-green-500">
				<svg
					xmlns="http://www.w3.org/2000/svg"
					viewBox="0 0 20 20"
					fill="currentColor"
					class="mr-3 h-5 w-5 flex-shrink-0"
				>
					<path
						fill-rule="evenodd"
						d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.857-9.809a.75.75 0 00-1.214-.882l-3.483 4.79-1.88-1.88a.75.75 0 10-1.06 1.061l2.5 2.5a.75.75 0 001.137-.089l4-5.5z"
						clip-rule="evenodd"
					/>
				</svg>
				<div>
					<h4 class="font-bold">Calculated Iterations</h4>
					<div class="mt-1">
						<ul class="list-inside list-disc">
							{#each Object.keys(answers) as answer}
								<li>{answer}: {answers[answer]}</li>
							{/each}
						</ul>
					</div>
				</div>
			</div>
		</div>
	{/if}
</section>
