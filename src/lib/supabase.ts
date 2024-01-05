import { createClient } from '@supabase/supabase-js';

const VITE_SUPABASE_URL = 'https://eobauqgsolxvyamddpjl.supabase.co';
const VITE_SUPABASE_KEY =
	'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVvYmF1cWdzb2x4dnlhbWRkcGpsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MDQzNzc4OTcsImV4cCI6MjAxOTk1Mzg5N30.hJx5GMmCS6PWnRio9hOJB04ZkoO5Cf-WD_O1zjc7yRI';

export const supabase = createClient(VITE_SUPABASE_URL, VITE_SUPABASE_KEY);
