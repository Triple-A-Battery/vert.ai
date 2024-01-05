import { supabase } from '$lib/supabase';

export async function load() {
	const { data: stocks } = await supabase.from('STOCKS').select();
	const { data: history } = await supabase.from('HISTORY').select();
	return {
		STOCKS: stocks ?? [], HISTORY: history ?? []
	};
}

