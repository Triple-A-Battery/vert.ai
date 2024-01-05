import { supabase } from '$lib/supabase';

export async function load() {
	const { data } = await supabase.from('STOCKS').select();
	return {
		STOCKS: data ?? []
	};
}
