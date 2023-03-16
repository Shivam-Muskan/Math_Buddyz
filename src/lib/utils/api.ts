import axios from 'axios';
import { baseAPI } from './constants';
import { page } from '$app/stores';

const axiosAPI = axios.create({
	baseURL: baseAPI
});

const apiRequest = (method: string, url: string, request: any) => {
	const headers = {
		'Referrer-Policy': 'no-referrer'
	};
	return axiosAPI({
		method,
		url,
		data: request,
		headers
	})
		.then((res) => {
			return Promise.resolve(res.data);
		})
		.catch((err) => {
			return Promise.reject(err);
		});
};

const get = (url: string, request: any) => apiRequest('get', url, request);

const deleteRequest = (url: string, request: any) => apiRequest('delete', url, request);

const post = (url: any, request: any) => apiRequest('post', url, request);

const put = (url: string, request: any) => apiRequest('put', url, request);

const patch = (url: string, request: any) => apiRequest('patch', url, request);

const API = {
	get,
	delete: deleteRequest,
	post,
	put,
	patch
};
export default API;
