import { supabase } from '$lib/supabase';

export async function load() {
	const { data: history } = await supabase.from('HISTORY').select('*');
	const { data: stocks } = await supabase.from('STOCKS').select('*');

	return { HISTORY: history ?? [], STOCKS: stocks ?? [] };
}
