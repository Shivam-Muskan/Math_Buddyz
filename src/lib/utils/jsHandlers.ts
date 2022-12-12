export const scrollToBottom = async (node: string) => {
	const el = document.getElementById(node);
	if (!el) return;
	el.scrollIntoView({
		behavior: 'smooth'
	});
};

export const sleep = async (ms: number) => {
	return new Promise((resolve) => setTimeout(resolve, ms));
};

export const extractNumbersAndAlphabet = async (currentString: string) => {
	const numbers = currentString.match(/\d+/g);
	const alphabet = currentString.match(/[a-zA-Z]/g);
	return { numbers, alphabet }
}
