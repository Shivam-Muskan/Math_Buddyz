<script>
	import Header from '$lib/Components/Header.svelte';
	import API from "$lib/utils/api";
	import toast from "svelte-french-toast";

	const allBinaryCalc = {
		binary_to_decimal: {
			name: 'Binary to Decimal',
            inputValue: '0',
            answerValue: null,
            disabled: false,
            description: ''
        },
		binary_to_octal: {
			name: 'Binary to Octal',
			inputValue: 0,
			answerValue: null,
			disabled: false,
			description: ''
		},
		binary_to_hexadecimal: {
			name: 'Binary to Octal',
			inputValue: 0,
			answerValue: null,
			disabled: false,
			description: ''
		},
		decimal_to_binary: {
			name: 'Decimal to Binary',
			inputValue: 0,
			answerValue: null,
			disabled: false,
			description: ''
		},
		decimal_to_octal: {
			name: 'Decimal to Octal',
			inputValue: 0,
			answerValue: null,
			disabled: false,
			description: ''
		},
		decimal_to_hexadecimal: {
			name: 'Decimal to Octal',
			inputValue: 0,
			answerValue: null,
			disabled: false,
			description: ''
		},
    }

	async function handleCalculations(calculator) {
		allBinaryCalc[calculator].disabled = true;
		let response;
		try {
            response = await API.post(`/${calculator}/?num=${allBinaryCalc[calculator].inputValue}`, {})
		} catch (e) {
			allBinaryCalc[calculator].disabled = false;
			toast.error(`Unable to complete your request for ${allBinaryCalc[calculator].name}`)
            return;
		}
		if (response.error) {
			allBinaryCalc[calculator].disabled = false;
			allBinaryCalc[calculator].answerValue = null
            toast.error(response.message);
            return
		}
		console.log(response);
		allBinaryCalc[calculator].answerValue = response.result
		allBinaryCalc[calculator].disabled = false;
		toast.success(`Now you can see answer on screen.`)
		return;
	}
</script>

<Header heading="Binary Calculator" />

<section id="binaryCalculator" class="py-5">
    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div
                class="mx-auto mt-12 grid max-w-fit grid-cols-1 justify-between justify-items-start gap-y-12 gap-x-8 sm:mt-16 md:grid-cols-4"
        >
            {#each Object.keys(allBinaryCalc) as calculator}
                <div class="mx-auto">
                    <div>
                        <label for={calculator} class="text-sm font-medium capitalize text-gray-900"
                        >{allBinaryCalc[calculator].name}</label
                        >
                        <div class="relative">
                            <input
                                    type="number"
                                    id={calculator}
                                    bind:value={allBinaryCalc[calculator].inputValue}
                                    class="block w-full rounded-lg border border-gray-300 bg-gray-50 p-4 mr-32 text-sm text-gray-900 focus:border-blue-500 focus:ring-blue-500"
                                    placeholder={allBinaryCalc[calculator].description}
                                    required
                            />
                            <button
                                    type="submit"
                                    on:click={handleCalculations(calculator)}
                                    disabled={allBinaryCalc[calculator].disabled}
                                    class="absolute right-2.5 bottom-2.5 rounded-lg bg-blue-700 px-4 py-2 text-sm font-medium text-white hover:bg-blue-800 focus:outline-none focus:ring-4 focus:ring-blue-300"
                            >Calculate</button
                            >
                        </div>
                        {#if allBinaryCalc[calculator].error}
                            <p class="mt-1 text-sm font-medium text-red-500">
                                {allBinaryCalc[calculator].error}
                            </p>
                        {/if}
                        {#if allBinaryCalc[calculator].answerValue !== null}
                            <div class="mt-4 flex rounded-md bg-indigo-50 p-4 text-sm text-indigo-500">
                                <svg
                                        xmlns="http://www.w3.org/2000/svg"
                                        viewBox="0 0 20 20"
                                        fill="currentColor"
                                        class="mr-3 h-5 w-5 flex-shrink-0"
                                >
                                    <path
                                            fill-rule="evenodd"
                                            d="M19 10.5a8.5 8.5 0 11-17 0 8.5 8.5 0 0117 0zM8.25 9.75A.75.75 0 019 9h.253a1.75 1.75 0 011.709 2.13l-.46 2.066a.25.25 0 00.245.304H11a.75.75 0 010 1.5h-.253a1.75 1.75 0 01-1.709-2.13l.46-2.066a.25.25 0 00-.245-.304H9a.75.75 0 01-.75-.75zM10 7a1 1 0 100-2 1 1 0 000 2z"
                                            clip-rule="evenodd"
                                    />
                                </svg>
                                <div>
                                    <h4 class="font-bold">{allBinaryCalc[calculator].name} of {allBinaryCalc[calculator].inputValue} is </h4>
                                    <div class="mt-1">
                                        <p>{allBinaryCalc[calculator].answerValue}</p>
                                    </div>
                                </div>
                            </div>
                        {/if}
                    </div>
                </div>
            {/each}

        </div>
    </div>
</section>
