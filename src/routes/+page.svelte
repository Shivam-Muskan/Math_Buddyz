<script lang="ts">
	import { allCalculators, miniSearch } from '$lib/utils/searchCalculator.js';
	import { slide } from 'svelte/transition';

	let calculatorSearchValue = '';
	let searchedCalculators = [];
	const handleSearch = async () => {
		if (calculatorSearchValue.length > 1) {
			return (searchedCalculators = miniSearch.search(calculatorSearchValue));
		}
		return (searchedCalculators = []);
	};
</script>

<div class="">
	<section class="relative py-6 xl:pb-0">
		<div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
			<div class="mx-auto max-w-3xl text-center">
				<p
					class="font-pj inline-flex rounded-full border border-[#D8B61C] px-4 py-2 text-base text-gray-900"
				>
					Made by Students, for Students
				</p>
				<h1
					class="font-pj mt-5 text-4xl font-bold leading-tight text-gray-900 sm:text-5xl sm:leading-tight lg:text-6xl lg:leading-tight"
				>
					A math companion for everyone
				</h1>
				<p class="font-inter mx-auto mt-6 max-w-md text-base leading-7 text-gray-600">
					You can solve everything if you choose right a path for it.
				</p>
				<div title="Change result" class={`dropdown dropdown-open`}>
					<div class="group relative my-10 inline-flex flex-col">
						<div
							class="animate-tilt absolute -inset-px mb-2 rounded-xl bg-gradient-to-r from-[#D8B61C] via-[#d3e645] to-[#78D43A] opacity-70 blur-lg transition-all duration-1000 group-hover:-inset-1 group-hover:opacity-100 group-hover:duration-200"
						/>

						<input
							on:input={async () => {
								await handleSearch();
							}}
							bind:value={calculatorSearchValue}
							class="font-pj hover::ring-offset-2 relative inline-flex items-center justify-center rounded-xl bg-gray-100 px-8 py-4 text-lg font-bold text-gray-900 transition-all duration-200 hover:ring-2 hover:ring-gray-900 focus:outline-none"
							role="button"
							placeholder="Search calculator"
						/>
					</div>
					{#if searchedCalculators.length > 0}
						<div
							class={`sc dropdown-content rounded-t-box rounded-b-box top-px mt-28 h-fit max-h-[30vh] w-72 overflow-y-auto text-base-content shadow-2xl`}
						>
							<div class="grid grid-cols-1 gap-3 p-3" tabindex="0" transition:slide>
								{#each searchedCalculators as result}
									<div
										class="overflow-hidden rounded-lg outline outline-2 outline-offset-2 outline-base-content"
									>
										<div
											data-result={result.id}
											class="w-full cursor-pointer bg-base-100 font-sans text-base-content"
										>
											<a class="grid grid-cols-5 grid-rows-3" href={result.route}>
												<div class="col-span-5 row-span-3 row-start-1 flex gap-1">
													<div class="flex-grow text-sm font-bold capitalize">
														<img src={result.image} alt={result.name} class="rounded" />
													</div>
												</div>
											</a>
										</div>
									</div>
								{/each}
							</div>
						</div>
					{/if}
				</div>
			</div>
		</div>
	</section>
</div>
<section class="-z-10 py-6">
	<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
		<div class="mx-auto max-w-lg text-center">
			<h2 class="text-3xl font-bold text-gray-900 sm:text-4xl">One For All</h2>
			<p class="mx-auto mt-5 max-w-md text-base font-normal leading-7 text-gray-500">
				Ready to use general maths solver
			</p>
		</div>

		<div
			id="#calculators"
			class="mx-auto mt-7 grid max-w-md snap-end grid-cols-1 gap-y-8 gap-x-8 sm:mt-16 md:max-w-none md:grid-cols-3"
		>
			{#each allCalculators as calculator}
				<a data-sveltekit-preload-data="hover" href={calculator.route}>
					<div class="group flex flex-col">
						<a
							href={calculator.route}
							title=""
							class="aspect-w-16 aspect-h-9 flex shrink-0 overflow-hidden rounded-lg"
						>
							<img
								class="h-full w-full transform rounded-lg object-cover transition-all duration-500 group-hover:scale-75"
								src={calculator.image}
								alt=""
							/>
						</a>
						<a href={calculator.route} title="" class="flex flex-1 flex-col">
							<p class="mt-6 text-2xl font-bold text-gray-900">{calculator.name}</p>
							<p class="mt-4 text-sm leading-6 text-gray-500 line-clamp-1">
								{calculator.def}
							</p>
						</a>
					</div>
				</a>
			{/each}
		</div>
	</div>
</section>

<style>
	/* Hide scrollbar for Chrome, Safari and Opera */
	.sc::-webkit-scrollbar {
		display: none;
	}

	/* Hide scrollbar for IE, Edge and Firefox */
	.sc {
		-ms-overflow-style: none; /* IE and Edge */
		scrollbar-width: none; /* Firefox */
	}
</style>
