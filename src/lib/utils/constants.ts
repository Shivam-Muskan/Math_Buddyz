import { env } from '$env/dynamic/public';

export const baseAPI: string = env.PUBLIC_BASE_API || 'http://127.0.0.1:8080/';
