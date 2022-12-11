<script lang="ts">
	let all_calculators: { name: string; route: string; def: string; image: string }[] = [
		{
			name: 'General Calculator',
			route: '/general',
			def: `It's for all type of general calculations.`,
			image: 'matrix.jpeg'
		},
		{
			name: 'Matrix Calculator',
			route: '/matrix',
			def: `It's for all type of matrix calculations.`,
			image: 'matrix.jpeg'
		}
	];
</script>

<div class="overflow-x-hidden">
	<section class="relative py-12 sm:py-16 lg:pt-20 xl:pb-0">
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

				<div class="group relative my-10 inline-flex">
					<div
						class="animate-tilt absolute -inset-px mb-2 rounded-xl bg-gradient-to-r from-[#D8B61C] via-[#d3e645] to-[#78D43A] opacity-70 blur-lg transition-all duration-1000 group-hover:-inset-1 group-hover:opacity-100 group-hover:duration-200"
					/>

					<a
						href="/"
						title=""
						class="font-pj relative inline-flex items-center justify-center rounded-xl bg-gray-900 px-8 py-4 text-lg font-bold text-white transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-gray-900 focus:ring-offset-2"
						role="button"
					>
						Check all the resources
					</a>
				</div>
			</div>
		</div>
	</section>
</div>
<section class="py-12 sm:py-16 lg:py-20">
	<div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
		<div class="mx-auto max-w-lg text-center">
			<h2 class="text-3xl font-bold text-gray-900 sm:text-4xl">One For All</h2>
			<p class="mx-auto mt-5 max-w-md text-base font-normal leading-7 text-gray-500">
				Ready to use general maths solver
			</p>
		</div>

		<div
			class="mx-auto mt-12 grid max-w-md grid-cols-1 gap-y-12 gap-x-8 sm:mt-16 md:max-w-none md:grid-cols-3"
		>
			{#each all_calculators as calculator}
				<a data-sveltekit-prefetch href={calculator.route}>
					<div class="group flex flex-col">
						<a
							href={calculator.route}
							title=""
							class="aspect-w-16 aspect-h-9 flex shrink-0 overflow-hidden"
						>
							<img
								class="h-full w-full transform object-cover transition-all duration-200 group-hover:scale-110"
								src={calculator.image}
								alt=""
							/>
						</a>
						<a href={calculator.route} title="" class="flex flex-1 flex-col">
							<p class="mt-6 text-2xl font-bold text-gray-900">{calculator.name}</p>
							<p class="line-clamp-2 mt-4 text-sm leading-6 text-gray-500">
								{calculator.def}
							</p>
						</a>
					</div>
				</a>
			{/each}
		</div>
	</div>
</section>
