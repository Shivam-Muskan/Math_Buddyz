import MiniSearch from 'minisearch';

export const allCalculators: {
	id: number;
	name: string;
	route: string;
	def: string;
	keywords: string;
	image: string;
}[] = [
	{
		id: 0,
		name: 'General Calculator',
		route: '/general',
		def: `It's for all type of general calculations. Here you can add, subtract, divide and can do multiple calculations at a time.`,
		keywords: '',
		image: 'general.webp'
	},
	{
		id: 1,
		name: 'Binary Calculator',
		route: '/binary',
		def: `It's for all type of computer number system calculations.`,
		keywords: '',
		image: 'binary.webp'
	},
	{
		id: 2,
		name: 'Matrix Calculator',
		route: '/matrix',
		def: `It's for all type of matrix calculations.`,
		keywords: '',
		image: 'matrix.webp'
	},
	{
		id: 3,
		name: 'Fibonacci Calculator',
		route: '/fibonacci',
		def: `It's for all type of fibonacci calculations. Here you can calculate many things like nth place fibonacci number, sum of fibonacci list of a number and etc.`,
		keywords: '',
		image: 'fibonacci.webp'
	},
	{
		id: 4,
		name: 'Linear Algebra Calculator',
		route: '/linearAlgebra',
		def: `It's for all type of linear algebra calculations. Here you can calculate many things related to linear number system.`,
		keywords: '',
		image: 'linear.webp'
	}
];

export let miniSearch = new MiniSearch({
	fields: ['name', 'def', 'keywords'], // fields to index for full-text search
	storeFields: ['name', 'route', 'image', 'def'], // fields to return with search results
	searchOptions: {
		boost: { name: 2 },
		fuzzy: 0.2,
		prefix: true
	}
});

miniSearch.addAll(allCalculators);
