require('./server.js');

app.get('/admin/volunteers', async (req, res) => {
  const { data, error } = await supabase
    .from('volunteers')
    .select('*')
    .order('created_at', { ascending: false });

  if (error) {
    return res.status(400).json({ success: false, error });
  }

  res.json({ success: true, volunteers: data });
});

